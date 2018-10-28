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
            defaults: {
            token: null
        },
        initialize: function (options) {
            this.options = options;
            $.ajaxPrefilter($.proxy(this._setupAuth, this));
            this.load();
        },
        load: function () {
            var token = localStorage.apiToken;
            if (token) {
                this.set('token', token);
            }
        },
        save: function (token) {
            this.set('token', token);
            if (token === null) {
                localStorage.removeItem('apiToken');
            } else {
                localStorage.apiToken = token;
            }
        },
        delete: function () {
            this.save(null);
        },
        authenticated: function () {
            return this.get('token') !== null;
        },
        _setupAuth: function (settings, originalOptions, xhr) {
            if (this.authenticated()) {
                xhr.setRequestHeader(
                    'Authorization',
                    'Token ' + this.get('token')
                );
            }
        }
    });
    
    app.session = new Session();

    var BaseModel = Backbone.Model.extend({
        // 覆盖默认的URL构造，并首先从links属性中查找self值。
        url: function () {
            var links = this.get('links'),
                url = links && links.self;
            if (!url) {
                //如果API未提供URL，则使用原始Backbone方法构造它。
                url = Backbone.Model.prototype.url.call(this);
            }
            return url;
        }
    });

    // 为每个模型创建存根：Sprint，Tasks和User。
    // 每个都添加到app.models映射中以在整个应用程序中使用。
    app.models.Sprint = BaseModel.extend({  //模型已更改为从BaseModel而不是Backbone.Model扩展
        //使用API提供的任务链接。此提取完成后，任务将添加到全局app.tasks集合中。
        fetchTasks: function () {
            var links = this.get('links');
            if (links && links.tasks) {
                app.tasks.fetch({url: links.tasks, remove: false});
            }
        }
    });
    app.models.Task = BaseModel.extend({    //模型已更改为从BaseModel而不是Backbone.Model扩展
        //statusClass有助于将任务映射到应与之关联的StatusView。
        statusClass: function () {
            var sprint = this.get('sprint'),
                status;
            if (!sprint) {
                status =  'unassigned';
            } else {
                status = ['todo', 'active', 'testing', 'done'][this.get('status') - 1];
            }
            return status;
        },
        //inBacklog确定了任务对待积压的意义。
        inBacklog: function () {
            return !this.get('sprint');
        },
        //inSprint确定任务是否在给定的sprint中。
        inSprint: function (sprint) {
            return sprint.get('id') == this.get('sprint');
        }
    });

    // 用username来引用用户
    app.models.User = BaseModel.extend({
        idAttributemodel: 'username'
    });

    var BaseCollection = Backbone.Collection.extend({
        // 解析parse覆盖在集合上存储next，previous和count元数据，然后返回来自API结果键results的对象列表。
        parse: function (response) {
            this._next = response.next;
            this._previous = response.previous;
            this._count = response.count;
            return response.results || [];
        },
        // getOrFetch方法返回一个延迟对象，该对象将解析为模型实例。
        getOrFetch: function (id) {
            var result = new $.Deferred(),
                // 使用this.get在ID中查找当前集合中的模型。
                // 调用this.get不会向API服务器发出请求; 它只查找与集合中当前内存中模型列表中的给定ID匹配的模型。
                // 如果在集合中找到模型，则会立即使用结果解析延迟对象。
                model = this.get(id);
            if (!model) {
                //如果模型不在集合中，则从API获取。此步骤使用原始视图实现中的相同逻辑，该逻辑首先将空模型放入集合中并从API中检索它。
                model = this.push({id: id});
                model.fetch({
                    success: function (model, response, options) {
                        result.resolve(model);
                    },
                    error: function (model, response, options) {
                        result.reject(model, response);
                    }
                });
            } else {
                result.resolve(model);
            }
            return result;
        }
    });

    // 获取API根目录，并将AJAX延迟对象存储为app.collections.ready。这将允许应用程序的其他部分等待集合准备就绪。
    app.collections.ready = $.getJSON(app.apiRoot);

    //当响应返回时，生成的URL用于构建每个集合。
    //集合定义将添加到app.collections映射中，并创建app.sprints，app.tasks和app.users的集合共享实例。
    app.collections.ready.done(function (data) {
        app.collections.Sprints = BaseCollection.extend({ //所有集合都已配置为从BaseCollection扩展。
            model: app.models.Sprint,
            url: data.sprints
        });
        app.sprints = new app.collections.Sprints();
        app.collections.Tasks = BaseCollection.extend({ //所有集合都已配置为从BaseCollection扩展。
            model: app.models.Task,
            url: data.tasks,
            //使用backlog = True过滤器来获取未分配给sprint的任务。与获取任务一样，生成的任务将添加到全局app.tasks集合中。
            getBacklog: function () {
                this.fetch({remove: false, data: {backlog: 'True'}});
            }
        });
        app.tasks = new app.collections.Tasks();
        app.collections.Users = BaseCollection.extend({ //所有集合都已配置为从BaseCollection扩展。
            model: app.models.User,
            url: data.users
        });
        app.users = new app.collections.Users();
    });
    
})(jQuery, Backbone, _, app);