最近出现了构建实时Web应用程序或将实时组件集成到现有应用程序中的趋势。
但是，Django主要针对短期HTTP请求/响应周期进行优化，并且大多数Python Web服务器不是为处理支持实时应用程序所需的大量并发和长期连接而设计的。
Node.js的兴起以及在Python标准库中包含asyncio使许多开发人员使用协作多任务和事件循环来解决高并发性问题。
但是，该解决方案要求以这种协作方式编写整个堆栈，以确保不会阻止循环。没有简单的方法可以将其放入现有的Django应用程序中。
除了低效的长轮询之外，没有明显的解决方案可以为Django应用程序添加实时功能。
在本章中，我们将探讨如何将实时功能集成到基于Django的REST API支持的同一个任务板应用程序中。
实时功能将由使用Tornado编写的新服务器处理，该服务器使用异步I/O来处理大量并发连接。我们将学习如何有效和安全地允许Django将更新推送到客户端。
首先，我们将检查HTML5中定义的新Web API集，以便更好地理解这种方法。

## bulid Commands

### HTML5实时API
我们将实时更新添加到我们的应用程序中，以便用户查看任务移动状态和更改顺序。 
对于我们的应用程序，REST API已经很好地定义了客户端更新协议。
但是，有一些客户端更新有助于了解，但不需要存储，例如当用户开始移动任务时。
这将允许应用程序通知查看sprint的其他客户端，以查找另一个用户正在更改它的任务。
由于客户端 - 服务器通信存在一些双向性，我们将使用websockets实现此功能。

实时Web已经从早期的长轮询和Comet方法演变为HTML5中的新Web标准，包括websockets，服务器发送事件（server-sent events SSE）和Web实时通信（WebRTC）。
它们中的每一个都适合不同的用例，并且具有不同的扩展需求和当前的浏览器支持。

**WebSockets**

Websockets是浏览器和服务器之间双向通信的规范。
此连接是持久的，这意味着服务器必须能够同时处理大量打开的连接。
必须注意服务器中的连接不要使用可能受限的其他资源。例如，如果每个Web服务器连接打开与数据库的连接，则连接数将受到限制，不一定是Web服务器可以保存的连接数，而是受数据库连接数的限制。
Websockets是最常见的HTML5标准，并且具有最佳的浏览器支持。
最流行的桌面浏览器的最新版本都支持websockets。移动浏览器的支持正在改善。

**SSE**

与websockets一样，服务器发送的事件需要长期的服务器连接。但是，与websockets不同，这不是双向连接。服务器发送的事件连接允许服务器将新事件推送到客户端。
正如您所料，客户端和服务器端API都比websocket协议简单得多。您可以通过启动新的HTTP请求来处理来自客户端的任何更新。从11.0开始的Internet Explorer不支持SSE，但支持websocket。


**WebRTC**

与前两个规范不同，WebRTC是一种浏览器到浏览器的通信协议。虽然通常需要服务器来发现其他客户端和初始握手，但一旦建立连接，服务器就看不到通信。
最初支持用于客户端之间的流式音频和视频通道，但最近支持发送任意数据。这适用于客户端需要在彼此之间同步大量状态的用例，这不是服务器的关注点。
WebRTC可以与其他协议结合使用，以实现服务器之间以及客户端之间的实时更新。这是HTML5标准中最不成熟的，并且浏览器支持最少，Internet Explorer 11.0和Safari 8.0都缺乏它。 移动支持也基本上不存在。

**集合自定义**
* 默认情况下，Backbone期望在我们的API响应中将所有模型列为数组。
API实现的分页包含对象列表，其中包含有关页面和总计数的元数据。
为了使这与Backbone一起使用，我们需要更改每个集合的解析方法。
与模型一样，这可以使用models.js中的基本集合类来处理。

### 基于Tornado的Websockets
使用Tornado编写websocket服务器，Tornado是一个异步网络库和用Python编写的小型Web框架。它在基于select/epoll的单线程事件循环上运行，可以处理大量同时连接，占用内存较少。
核心网络功能和Web框架都简单易读，并且有可靠的文档和示例。目前，它拥有异步Python框架最成熟的Python 3支持。

[Tornado official documentation](http://www.tornadoweb.org/en/stable/)

为什么我们不将所有这些功能构建到一个Django服务器中。首先，Django主要基于WSGI规范，该规范不适用于处理长期连接。大多数WSGI服务器通过多线程处理大并发，但这种方法无法很好地扩展到大量长期连接。
I/O绑定的多线程Python应用程序偶尔会遇到Global Interpreter Lock（GIL）的问题。

有些人尝试过使用轻量级或“绿色”线程代替本机线程的方法。这种方法有其优点，但其核心工作方式与单线程事件循环非常相似。这是合作的多任务处理。
如果应用程序的某些部分在执行I/O时不会产生事件循环，则会阻止所有连接。隐式异步框架，例如gevent和eventlet，Python标准库中的monkey-patch I/O库，例如套接字库。
执行网络操作的C扩展无法以这种方式修补。跟踪与在这些隐式异步框架中被阻止的循环相关的错误可能难以调试以及难以解决或难以解决。

为websocket提供单独服务器的另一个原因是关注点的分离。Django期望连接是短暂的，对于这个REST API，完全无状态。 websocket连接将是长寿的并且可能是有状态的。
这些有助于解决不同的扩展问题。此外，该应用程序的实时功能比应用程序的功能更具核心。可能存在客户端启用它们不可行或不合理的情况，例如旧浏览器或动力不足的移动设备。
通过在单独的进程中容纳这些连接，实时服务器可能会失败，仍然可以使用应用程序的核心。这需要Django应用程序和实时服务器尽可能少地共享。所有需要共享的信息都将通过定义良好的API完成。
Tornado不是您此服务器的唯一选择。实时服务器可以用Node，Erlang，Haskell或任何最适合该任务的语言或框架编写。如果正确实现，如果Django方面稍后换掉了其他语言或框架，则不应对其进行任何更改。
其中重要的部分是两个服务器之间的分离和明确定义的通信。

**Tornado简介**
使用Tornado构建我们的实时服务器组件。可以使用pip从PyPi安装Tornado。

    hostname $ pip install Tornado

从版本3.2开始，Tornado包含一个可选的C扩展，可以提高websocket连接的性能。但是，它需要一个工作的C编译器来安装。如果在安装时在系统上找到C编译器，它将自动构建扩展。
Tornado 4.0添加了certifi作为依赖。
对于许多Web应用程序，您不需要深入了解Tornado提供的低级网络部分，而是可以专注于Tornado内置的Web框架。 该框架围绕两个主要类构建：RequestHandler和Application。
RequestHandler正如其名称所暗示的那样，并且具有类似于Django的View类的API，该类是所有基于类的视图的基础。应用程序不直接映射到Django中的任何一个概念。
它涵盖了与Django的根URL conf和Django的设置相同的功能; 也就是说，Application将URL映射到RequestHandler类，以及处理全局配置或共享资源。
Tornado通过子类化tornado.websocket.WebSocketHandler内置了对处理websocket连接的支持。

从4.0开始，Tornado默认通过check_origin拒绝交叉原始的websocket连接。前面的服务器将在4.0之前的Tornado上运行，但不会强制执行此检查。

* 用于处理给定sprint更新的Tornado服务器为watercooler.py
* 服务器在端口8080上运行。执行脚本将启动服务器。


    hostname $ python3 watercooler.py
    
* 停止Tornado服务器的更多详细信息，访问https://groups.google.com/forum/#!topic/python-tornado/VpHp3kXHP7s和https://gist.github.com/mywaiting/4643396。
* 服务器可以在调试模式下运行，具有更多输出和更优雅的退出。
    
    
    hostname $ python3 watercooler.py --debug
    
**消息订阅**

当新客户端连接到http//localhost:8080/1/时，将调用SprintHandler.open，将值1作为sprint传递。URL使用正则表达式进行路由，并将命名组转换为参数。
可以通过write_message方法随时向客户端发送新消息。服务器需要订阅客户端以获取与sprint相关的任何更新以及何时更新此sprint中的任务。 对于第一个实现，可以在服务器应用程序中跟踪订阅。 

* 在创建一个Application子类ScrumApplication，它包含字典中每个sprint的订阅者列表。
* 每个处理程序都可以通过其application属性访问应用程序实例。
* 当新客户端连接时，处理程序应注册客户端以获取有关相关sprint的更新。
* 客户端关闭连接，则应从订户列表中删除客户端。

### Client Communication

**最小的例子**

对于客户端，websocket是一个相对简单的API。通过创建一个新的WebSocket来建立新的连接，并通过这些回调函数处理套接字操作：
onopen /onmessage /onclose /onerror


    var socket = new WebSocket('ws://localhost:8080/123'); socket.onopen = function () {
          console.log('Connection is open!');
          socket.send('ping');
      };
    socket.onmessage = function (message) { console.log('New message: ' + message.data); if (message.data == 'ping') {
              socket.send('pong');
          }
    };

由于服务器当前不验证传递的sprint，因此该示例仅使用123的硬编码值。要测试连接请确保watercooler.py服务器已启动并正在运行：
    
    hostname $ python watercooler.py

然后打开http://localhost:8080。您可以通过将脚本粘贴到浏览器的开发人员工具控制台Console中来进行测试。
