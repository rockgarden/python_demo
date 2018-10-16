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
        
    /// 通过 app.js 应用中统一解析 config
    
    /// 在 templates/app/index.html 增加 模型、视图、路由的描述文件
        <script src="{% static 'board/js/app.js' %}"></script>
        <script src="{% static 'board/js/models.js' %}"></script>
        <script src="{% static 'board/js/views.js' %}"></script>
        <script src="{% static 'board/js/router.js' %}"></script>
        
