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