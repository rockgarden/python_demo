

## bulid Commands

### 发现API

**获取API**
* 从models.js文件的API根目录中获取可用资源的URL

**模型定制**
* 在Backbone中，模型URL将从集合URL构造，默认情况下不包括尾部斜杠。
虽然这是Java脚本框架的正常模式，但是django-rest-framework期望将一个尾部斜杠附加到URL。
在models.js完成将其合并到我们的URL结构中。
此外，API将在链接值中返回模型的URL。
如果此值已知，则应使用它而不是构造URL。

* 在服务器上在构造路由器时更改trailing_slash选项。 
我们还可以通过在board / urls.py中添加尾部斜杠BaseModel.url函数来处理这个问题。

* API还希望用户名而不是id引用用户。我们可以使用models.js中的idAttribute模型选项来配置它。

**集合自定义**
* 默认情况下，Backbone期望在我们的API响应中将所有模型列为数组。
API实现的分页包含对象列表，其中包含有关页面和总计数的元数据。
为了使这与Backbone一起使用，我们需要更改每个集合的解析方法。
与模型一样，这可以使用models.js中的基本集合类来处理。

### 建立主页

**显示当前Sprint**
* views.js中处理HomepageView
* 主页Underscore模板index.html现在需要更新，以便在sprint可用时和它们仍在加载时进行处理。
* board.css中添加一些CSS来实现一些基本样式。

**创建新的Sprint**
* 创建新sprint的逻辑将由子视图处理以呈现表单。这可以使用FormView，类似于LoginView，如views.js所示。
* 在xx/templates/xx/index.html中为视图创建一个模板来包含这个表单。
* 由HomepageView（在/js/views.js中）渲染视图和模板，它将添加绑定到自定义方法的事件。
* 添加CSS来清楚地定义列表中的表单

### 路由Sprint详细信息
* 新SprintView在创建时需要sprintId。需要从路径捕获此值并将其传递给视图。Backbone允许捕获部分路由。将路由添加到router.js文件中的sprint详细信息页面。