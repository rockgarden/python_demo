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
        serializeForm: function (form) {
            return _.object(_.map(form.serializeArray(), function (item) {
                // Convert object to tuple of (name, value)
                return [item.name, item.value];
            }));
        },
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

    var LoginView = FormView.extend({
        id: 'login',
        templateName: '#login-template',
        //此事件属性侦听LoginView元素内任何表单元素上的所有提交事件。触发事件时，它将执行提交回调。
        //提交回调会阻止提交表单，以便视图可以提交并处理结果。
        submit: function (event) {
            var data = {};
            FormView.prototype.submit.apply(this, arguments);
            data = this.serializeForm(this.form);
            //通过使用新的app.apiLogin配置，将用户名和密码信息提交给后端。
            $.post(app.apiLogin, data)
                .done($.proxy(this.loginSuccess, this))
                .fail($.proxy(this.failure, this));
        },
        //登录成功后,将使用先前定义的令牌保存令牌,app.session和登录事件被触发。
        loginSuccess: function (data) {
            app.session.save(data.token);
            this.done();
        }
    });

    var HeaderView = TemplateView.extend({
        tagName: 'header',
        templateName: '#header-template',
        events: {
            'click a.logout': 'logout'
        },
        getContext: function () {
            return {authenticated: app.session.authenticated()};
        },
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
    app.views.HeaderView = HeaderView;

})(jQuery, Backbone, _, app);
