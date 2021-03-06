(function ($, Backbone, _, app) {

    var AppRouter = Backbone.Router.extend({
        ///定义路由
        routes: {
            '': 'home'
        },
        initialize: function (options) {
            this.contentElement = '#content'; //引用ID选择器，指定Underscore模板加载的位置.
            this.current = null;
            //创建路由时会初始化标题视图，并将其元素添加到<body>的开头。
            this.header = new app.views.HeaderView();
            $('body').prepend(this.header.el);
            this.header.render();
            Backbone.history.start(); //触发路由
        },
        home: function () {
            var view = new app.views.HomepageView({el: this.contentElement});
            this.render(view);
        },

        //覆盖路由器的默认路由方法。它作为哈希路由传递，并且是回调方法的名称或显式回调函数。
        route: function (route, name, callback) {
            // Override default route to enforce login on every page
            var login;
            callback = callback || this[name];
            //原始回调函数将被包装，以便在调用之前首先检查身份验证状态。
            callback = _.wrap(callback, function (original) {
                var args = _.without(arguments, original);
                if (app.session.authenticated()) {
                    //如果用户已通过身份验证，则只需调用原始回调。
                    original.apply(this, args);
                } else {
                //如果用户未经过身份验证，则隐藏当前页面内容并改为呈现登录视图。当登录视图触发完成事件时，允许继续原始回调。
                    // Show the login screen before calling the view
                    $(this.contentElement).hide();
                    // Bind original callback once the login is successful
                    login = new app.views.LoginView();
                    $(this.contentElement).after(login.el);
                    login.on('done', function () {
                        this.header.render(); //登录完成后，将再次呈现标题以反映新状态。
                        $(this.contentElement).show();
                        original.apply(this, args);
                    }, this);
                    // Render the login form
                    login.render();
                }
            });
            //使用新的包装回调调用原始路由。
            return Backbone.Router.prototype.route.apply(this, [route, name, callback]);
        },
        render: function (view) { //render function 在视图切换时帮助路由追踪
            if (this.current) {
                this.current.undelegateEvents();
                this.current.$el = $();
                this.current.remove();
            }
            this.current = view;
            this.current.render();
        }
    });
    
    app.router = AppRouter; //路由附加到app配置中让它在整个项目范围内可用.

})(jQuery, Backbone, _, app);