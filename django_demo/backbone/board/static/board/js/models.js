(function ($, Backbone, _, app) {
	
    // CSRF helper functions taken directly from Django docs
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/i.test(method));
    }
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Setup jQuery ajax calls to handle CSRF
    //由于此函数是自调用的，因此在加载models.js时将进行这些$.ajaxPrefilter调用。
    $.ajaxPrefilter(function (settings, originalOptions, xhr) {
        var csrftoken;
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    });

    var Session = Backbone.Model.extend({
            //token变量默认为空
            defaults: {
            token: null
        },
        initialize: function (options) {
            this.options = options;
            //在初始化Session模型之前，我们希望实际检查用户是否经过身份验证。
            //使用$.ajaxPrefilter根据_setupAuth方法的结果代理令牌。
            $.ajaxPrefilter($.proxy(this._setupAuth, this));
            this.load();
        },
        load: function () {
            //基于localStorage获取token初始值
            var token = localStorage.apiToken;
            if (token) {
                this.set('token', token);
            }
        },
        save: function (token) {
            this.set('token', token);
            //检查token是否为有真实值,若无赋值,则移除apiToken,取消授权.
            if (token === null) {
                localStorage.removeItem('apiToken');
            } else {
                localStorage.apiToken = token;
            }
        },
        delete: function () {
            this.save(null);
        },
        //检查当前实例下token是否存在
        authenticated: function () {
            return this.get('token') !== null;
        },
        //XMLHttpRequest作为JavaScript对象返回，该对象使用回调方法进行状态更改。
        //它使我们能够向Web服务器发送HTTP请求，包括标头和参数。
        //在我们的Session模型中，定义了一个名为_setupAuth的方法。
        //这将检查身份验证，如果为true，则将令牌传递到XMLHttpRequest中请求的头参数。
        _setupAuth: function (settings, originalOptions, xhr) {
            if (this.authenticated()) {
                xhr.setRequestHeader(
                    'Authorization',
                    'Token ' + this.get('token')
                );
            }
        }
    });
    //创建会话模型
    app.session = new Session();
    
})(jQuery, Backbone, _, app);
//这是处理身份验证的地方。
//如果当前会话模型正在存储API令牌，则此令牌将按照django-rest-framework的预期添加到Authorization请求头中。