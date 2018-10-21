Backbone路由是一种通过History API为我们的应用程序创建URL的方法。 除了API根目录和登录之外，API还需要某种身份验证，以便用户与我们的应用程序进行交互。 没有身份验证令牌，客户端将无法执行任何操作。 如果令牌不可用，我们需要创建一种显示登录表单的方法，并且能够获取它。 在服务器上，我们将通过将用户重定向到登录URL并在登录建立后重定向回来处理此问题。

## bulid Commands 
    
    /// 在 templates/app/index.html 布置模板代码依赖, 按顺序增加
        <script src="{% static 'board/vendor/jquery.js' %}"></script>
        <script src="{% static 'board/vendor/underscore.js' %}"></script>
        <script src="{% static 'board/vendor/backbone.js' %}"></script>

    /// 在 backbone.js 依赖后 增加 模型、视图、路由添加JSON对象空值，用于Django模板的上下文对象
        <script id="config" type="text/json">
            {
                "models": {},
                "collections": {},
                "views": {},
                "router": null,
                "apiRoot": "{% url 'api-root' %}",
                "apiLogin": "{% url 'api-token' %}"
            }
        </script>
        
    /// 通过 app.js 应用中统一解析JSON生成全局变量config
    
    /// 在 templates/app/index.html 增加 模型、视图、路由的描述文件
        <script src="{% static 'board/js/app.js' %}"></script>
        <script src="{% static 'board/js/models.js' %}"></script>
        <script src="{% static 'board/js/views.js' %}"></script>
        <script src="{% static 'board/js/router.js' %}"></script>
    
    /// 在 views.js 创建视图来渲染主页模板
    /// 在 router.js 设置路由
    /// 在 index.html 中创建 ID 如 home-template 作为主页模板代码（Underscore.js中的__.template）的引用.
    /// 在 app.js 中生成全局变量router.
    /// 在 项目配置的 urls.py文件中创建 视图url 来渲染 index.html
    
    /// 应用内用户验证 在models.js 创建基本模型
    /// 在models.js添加方法为XMLHttpRequest(xhr)设置请求头信息
    /// 在models.js添加CSRF(Cross-site request forgery)跨站点请求伪造
    /// 在xx/static/xx/js/views.js中创建登录视图
    /// 由于使用相同的模式创建更多视图来完成我们的应用程序，所以可利用Backbone的可扩展性在iews.js中创建一个通用的视图模板，并在模型上建模所有的views。
    
    /// 将login-template添加到index.html文件
    
    /// 创建通用表单视图:在js/views.js中增加FormView
    
    /// 验证路由:通过我们的router.js文件劫持应用程序路由来处理token无效问题。
    
**标题视图**

LoginView一样，HeaderView与特定路由无关。它始终存在。只有在登录状态发生变化时才需要更改。
这都可以在路由（static/xx/js/router.js）中处理。
分离所有路由的劫持并从主要内容强制执行逻辑和标头有助于确保每个路由都不必单独处理视图及其模板中的登录状态。
1.  HeaderView将用于呈现显示在所有视图顶部的标题。将此模板添加到index.html文件中添加到`<head>`元素中。
2.  js/views.js中创建一个与该模板相关联的视图HeaderView，并包含用于添加我们的注销交互的认证要求。

**创建站点CSS**

在继续与API进行更多交互之前，让我们在网站标题和登录表单中添加一些基本样式。要有一个干净的起点来添加样式，我们首先要包含一个重置样式表。
这可以从http://necolas.github.io/ normalize.css / latest / normalize.css下载，并应保存到供应商静态目录中。
我们还将在css目录中创建我们的站点CSS。
1.  New .css
2.  引入index.html.