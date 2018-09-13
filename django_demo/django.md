# django 2.1

## Command 

1. 用模板创建项目


    $ django-admin.py startproject foo --template=project_name

## 相关库
- [django_compressor](https://pypi.org/project/django-compressor/)压缩工具.

## Tips
Django被称为模型 - 模板 - 视图（MTV）框架。 视图部分通常检查传入的HTTP请求，并查询或构造发送到表示层的必要数据。

Web服务器网关接口（WSGI）是Web服务器如何与Django等应用程序框架进行通信的规范，由PEP 333定义并在PEP 3333中进行了改进。
对于使用WSGI的Web服务器有很多选择，包括Apache通过mod_wsgi ，Gunicorn，uWSGI，CherryPy，Tornado和Chaussette。
这些服务器中的每一个都需要使用正确定义的WSGI应用程序。 Django有一个简单的界面，可以通过get_wsgi_application创建这个应用程序。
    
    $ gunicorn xxx --log-file=-

HTTP本身是无状态协议，这意味着每个到服务器的请求都独立于先前的请求。 如果需要特定状态，则必须在应用程序层添加。 
像Django这样的框架使用cookie和其他机制将同一客户端发出的请求联系在一起。

URL Patterns
placeholder URL模式。我们还需要一条到我们刚刚创建的占位符视图的路径。
占位符视图的存根将采用两个参数：宽度和高度。如前所述，这些参数将被URL捕获并传递给视图。
由于它们只是整数，我们希望确保通过URL强制执行它们。 
由于Django中的URL模式使用正则表达式来匹配传入的URL，因此我们将能够轻松传递这些参数。
捕获的模式组作为位置参数传递给视图，命名组作为关键字参数传递。
使用?P语法捕获命名组，并使用[0-9]匹配任何数字字符。

### USE_ETAGS
Django默认使用进程本地内存缓存，但您可以通过配置CACHES设置使用不同的后端（如Memcached或文件系统）。
补充方法是关注客户端行为并使用浏览器的内置缓存。
Django包含一个etag装饰器，用于为视图生成和使用ETag标头。
装饰器接受一个参数，该参数是从请求和视图参数生成ETag标头的函数。
有了这个装饰器，服务器将需要在浏览器第一次请求它时生成图像。
在后续请求中，如果浏览器使用匹配的ETag发出请求，则浏览器将收到图像的304 Not Modified响应。
浏览器将使用缓存中的图像并节省带宽和时间来重新生成HttpResponse。
如果启用了USE_ETAGS设置，则在MIDDLEWARE_CLASSES设置中启用的django.middleware.common.CommonMiddleware也支持生成和使用ETag。
但是，中间件和装饰器的工作方式有所不同。 中间件将根据响应内容的md5哈希计算ETag。 
这需要视图执行所有工作以生成内容以便计算哈希值。结果相同，浏览器将收到304 Not Modified响应，并且将保存带宽。
使用etag装饰器具有在调用视图之前计算ETag的优点，这也将节省处理时间和资源。