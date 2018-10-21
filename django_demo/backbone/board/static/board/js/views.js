//立即调用函数(immediately invoked function expression)
//使用 jQuery, Backbone, Underscore.js来保持代码整洁，并可通过app.js访问全局变量global variables。
//This function expression is based on the JavaScript closure,  没有返回值，用来把对象隔离在全局范围之外。
//helps keep our objects out of the global scope.
(function ($, Backbone, _, app) {

    //模板视图
    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function () {
            this.template = _.template($(this.templateName).html());
            //用Underscore.js的_.template工具将主页模板渲染到HTML
        },
        render: function () {
            var context = this.getContext(),
            html = this.template(context);
            this.$el.html(html);
        },
        getContext: function () {
            return {};
        }
    });

    var FormView = TemplateView.extend({
        events: {
            'submit form': 'submit'
        },
        //每个错误消息都是从新的错误模板创建的，该模板使用我们在脚本顶部创建的新内联Underscore.js模板。
        errorTemplate: _.template('<span class="error"><%- msg %></span>'),
        //此方法从每个提交的表单中删除任何现有错误。
        clearErrors: function () {
            $('.error', this.form).remove();
        },
        showErrors: function (errors) {
            //遍历响应中的所有字段和错误，并在字段标签之前将每个错误添加到DOM。
            _.map(errors, function (fieldErrors, name) {
                var field = $(':input[name=' + name + ']', this.form),
                    label = $('label[for=' + field.attr('id') + ']', this.form);
                if (label.length === 0) {
                    //如果未找到匹配的字段，则会在第一个标签之前添加错误。
                    label = $('label', this.form).first();
                }
                function appendError(msg) {
                    //每个错误消息都是从新的错误模板创建
                    label.before(this.errorTemplate({msg: msg}));
                }
                _.map(fieldErrors, appendError, this);
            }, this);
        },

        //serializeForm是表单字段值的更通用的序列化，而不是LoginView中存在的显式版本。
        serializeForm: function (form) {
            return _.object(_.map(form.serializeArray(), function (item) {
                // Convert object to tuple of (name, value)
                return [item.name, item.value];
            }));
        },

        //通过阻止默认提交和清除错误来设置表单提交的开始。 扩展此视图的每个视图都需要进一步定义此回调。
        submit: function (event) {
            event.preventDefault();
            this.form = $(event.currentTarget);
            //从每个提交的表单中删除任何现有错误。
            this.clearErrors();
        },

        //失败时，需要向用户显示错误。
        failure: function (xhr, status, error) {
            var errors = xhr.responseJSON;
            this.showErrors(errors);
        },
        //错误将作为JSON返回，并具有与字段名称匹配的键
        //{"username": ["This field is required."], "password": ["This field is required."]}
        //{"non_field_errors": ["Unable to login with provided credentials."]}

        //done是触发登录事件的通用版本。它还处理从DOM中删除表单。
        done: function (event) {
            if (event) {
                event.preventDefault();
            }
            this.trigger('done');
            this.remove();
        }
    });

    //HomepageView和LoginView都从TemplateView扩展，可清理重复代码。
    var HomepageView = TemplateView.extend({
        templateName: '#home-template'
        // 用ID选择器来指派用什么underscore.js模板来渲染主页。
    });

    //LoginView从FormView而不是TemplateView扩展。
    var LoginView = FormView.extend({
        id: 'login',
        templateName: '#login-template',

        //此事件属性侦听LoginView元素内任何表单元素上的所有提交事件。触发事件时，它将执行提交回调。
        //提交回调会阻止提交表单，以便视图可以提交并处理结果。
        submit: function (event) {
            var data = {};
            //提交回调-调用原始的FormView提交，以防止提交并清除任何错误。
            //调用父类方法(JavaScript无super)
            FormView.prototype.submit.apply(this, arguments);
            //表单使用serializeForm帮助程序序列化数据，而不是手动检索用户名和密码字段。
            data = this.serializeForm(this.form);
            //通过使用新的app.apiLogin配置，将用户名和密码信息提交给后端。
            $.post(app.apiLogin, data)
                .done($.proxy(this.loginSuccess, this))
                //使用默认的failure回调，不必在此重新定义。
                .fail($.proxy(this.failure, this));
        },
        //登录成功后,将使用先前定义的令牌保存令牌,app.session和登录事件被触发。
        //loginSuccess回调现在在保存令牌后使用done帮助程序。
        loginSuccess: function (data) {
            app.session.save(data.token);
            this.done();
        }
    });

    //HeaderView从TemplateView扩展，以使逻辑与其他视图保持类似。
    var HeaderView = TemplateView.extend({
        //与以前的视图不同，tagName已定义。这意味着模板呈现为<header>元素。
        tagName: 'header',
        templateName: '#header-template',
        //当用户通过身份验证时，标头中的导航将具有两个链接。一个将返回主页，另一个将退出。
        events: {
            'click a.logout': 'logout'
        },
        //经过身份验证的值将根据当前会话状态传递给模板上下文。如果此状态发生更改，则不会自动更新。必须再次渲染视图。
        getContext: function () {
            return {authenticated: app.session.authenticated()};
        },
        //注销逻辑-视图中的注销回调中处理。
        logout: function (event) {
            event.preventDefault();
            app.session.delete();
            window.location = '/';
        }
    });

    //加入HomepageView加入app.views字典供应用的其它模块使用（如路由）
    //HomepageView和LoginView被添加到app.views字典中。
    //TemplateView是views.js之外不需要的实现细节，因此它仍然是隐藏的。
    app.views.HomepageView = HomepageView;
    app.views.LoginView = LoginView;
    //视图被添加到app.views映射中，以便路由器可以使用它。
    app.views.HeaderView = HeaderView;

})(jQuery, Backbone, _, app);
