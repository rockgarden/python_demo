(function ($, Backbone, _, app) {

    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function () {
            this.template = _.template($(this.templateName).html());
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
            'submit form': 'submit',
            'click button.cancel': 'done'  //FormView现在默认将任何button.cancel点击绑定到done方法。
        },
        errorTemplate: _.template('<span class="error"><%- msg %></span>'),
        clearErrors: function () {
            $('.error', this.form).remove();
        },
        showErrors: function (errors) {
            _.map(errors, function (fieldErrors, name) {
                var field = $(':input[name=' + name + ']', this.form),
                    label = $('label[for=' + field.attr('id') + ']', this.form);
                if (label.length === 0) {
                    label = $('label', this.form).first();
                }
                function appendError(msg) {
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
            this.clearErrors();
        },
        failure: function (xhr, status, error) {
            var errors = xhr.responseJSON;
            this.showErrors(errors);
        },
        done: function (event) {
            if (event) {
                event.preventDefault();
            }
            this.trigger('done');
            this.remove();
        },
        //$.ajax故障回调将响应对象作为第一个参数，但Model.save将模型实例作为第一个参数，响应作为第二个参数。
        modelFailure: function (model, xhr, options) {
            var errors = xhr.responseJSON;
            this.showErrors(errors);
        }
    });

    var NewSprintView = FormView.extend({ //此视图扩展了FormView帮助类，应该在HomepageView之前定义。
        templateName: '#new-sprint-template',
        className: 'new-sprint',  //NewSprintView不再需要扩展事件，并且可以从每个视图中删除此声明。
        //单击“添加”按钮将触发表单提交，该表单由FormView基础处理。除了默认的提交事件处理程序之外，视图还将处理取消按钮以调用FormView定义的done方法。
        submit: function (event) {
            var self = this,
                attributes = {};
            FormView.prototype.submit.apply(this, arguments);
            attributes = this.serializeForm(this.form);
            app.collections.ready.done(function () {
                //表单值是序列化的。视图使用app.sprints.create，而不是手动调用$.post。成功和失败处理程序将重新绑定到视图中。
                app.sprints.create(attributes, {
                    wait: true,
                    success: $.proxy(self.success, self),
                    //失败回调转到添加到FormView的新modelFailure。
                    error: $.proxy(self.modelFailure, self)
                });
            });
        },
        //创建sprint后，视图调用done并重定向到sprint的详情路由
        success: function (model) {
            this.done();
            window.location.hash = '#sprint/' + model.get('id');
        }
    });

    var HomepageView = TemplateView.extend({ //此视图扩展了FormView帮助类，应该在HomepageView之前定义。
        templateName: '#home-template',
        //添加按钮的单击事件现在由renderAddForm处理。
        events: {
            'click button.add': 'renderAddForm'
        },
        //创建视图时，将获取结束日期大于七天的Sprint。当sprint可用时，将再次呈现视图以显示它们。
        initialize: function (options) {
            //在initialize函数中保存对this的当前值的引用，该引用将是视图的实例，以便稍后可以在完成的回调函数中使用它。
            //它的值取决于函数/方法的调用方式，并确保它是正确的可能是棘手的 - 特别是对于嵌套的回调函数。
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments);
            app.collections.ready.done(function () {
                var end = new Date();
                end.setDate(end.getDate() - 7);
                end = end.toISOString().replace(/T.*/g, '');
                app.sprints.fetch({
                    data: {end_min: end},
                    //$ .proxy，可用于为函数调用显式设置此上下文。Underscore有一个名为_.bind的等效助手。
                    //这两个模拟ECMAScript 5中引入的Function.prototype.bind并确保跨浏览器兼容性。
                    success: $.proxy(self.render, self)
                });
            });
        },
        getContext: function () {
            //模板上下文现在包含来自app.sprints的当前sprint。如果app.collections未准备好，则可能未定义。在这种情况下，模板将获得空值。
            return {sprints: app.sprints || null};
        },
        //renderAddForm将创建一个NewSprintView实例，该实例在按钮上方呈现。视图完成后，无论是添加还是取消按钮，都会再次显示该链接。
        renderAddForm: function (event) {
            var view = new NewSprintView(),
                link = $(event.currentTarget);
            event.preventDefault();
            link.before(view.el);
            link.hide();
            view.render();
            view.on('done', function () {
                link.show();
            });
        }
    });

    var LoginView = FormView.extend({
        id: 'login',
        templateName: '#login-template',
        submit: function (event) {
            var data = {};
            FormView.prototype.submit.apply(this, arguments);
            data = this.serializeForm(this.form);
            $.post(app.apiLogin, data)
                .done($.proxy(this.loginSuccess, this))
                .fail($.proxy(this.failure, this));
        },
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

    var AddTaskView = FormView.extend({  //扩展FormView以实现基本模板呈现和表单提交以及错误处理。
        templateName: '#new-task-template',  //NewSprintView不再需要扩展事件，并且可以从每个视图中删除此声明。
        submit: function (event) {
            var self = this,
                attributes = {};
            FormView.prototype.submit.apply(this, arguments);
            //代码将表单序列化为API可以使用的可使用的JSON数据。
            attributes = this.serializeForm(this.form);
            //在集合中创建新任务，并为与API的交互分配各种属性。因为我们正在使用模型保存方法，所以失败被绑定到FormView的modelFailure回调。
            app.collections.ready.done(function () {
                app.tasks.create(attributes, {
                    wait: true,
                    success: $.proxy(self.success, self),
                    error: $.proxy(self.modelFailure, self)
                });
            });
        },
        success: function (model, resp, options) {
            this.done();
        }
    });

    var StatusView = TemplateView.extend({
        tagName: 'section',
        className: 'status',
        templateName: '#status-template',
        events: {
            //视图现在绑定一个事件处理程序，用于单击带有add类的按钮。虽然此视图的所有实例都具有此处理程序，但呈现按钮的唯一模板是待处理任务的StatusView实例。
            'click button.add': 'renderAddForm'
        },
        //StatusView定义三个选项sprint，status和title
        initialize: function (options) {
            TemplateView.prototype.initialize.apply(this, arguments);
            this.sprint = options.sprint;
            this.status = options.status;
            this.title = options.title;
        },
        getContext: function () {
            return {sprint: this.sprint, title: this.title};
        },
        //单击按钮时会创建一个新的AddTaskView实例，并在完成后自动删除，无论是创建新任务还是用户单击取消。
        renderAddForm: function (event) {
            var view = new AddTaskView(),
                link = $(event.currentTarget);
            event.preventDefault();
            link.before(view.el);
            link.hide();
            view.render();
            view.on('done', function () {
                link.show();
            });
        },
        //addTask方法来添加任务视图，它可以插入到DOM中。
        addTask: function (view) {
            $('.list', this.$el).append(view.el);
        }
    });

    var TaskDetailView = FormView.extend({
        tagName: 'div',
        className: 'task-detail',
        templateName: '#task-detail-template',
        events: _.extend({
            'blur [data-field][contenteditable=true]': 'editField'
        }, FormView.prototype.events),
        initialize: function (options) {
            FormView.prototype.initialize.apply(this, arguments);
            this.task = options.task;
            this.changes = {};
            $('button.save', this.$el).hide();
            this.task.on('change', this.render, this);
            this.task.on('remove', this.remove, this);
        },
        getContext: function () {
            return {task: this.task, empty: '-----'};
        },
        submit: function (event) {
            FormView.prototype.submit.apply(this, arguments);
            this.task.save(this.changes, {
                wait: true,
                success: $.proxy(this.success, this),
                error: $.proxy(this.modelFailure, this)
            });
        },
        success: function (model) {
            this.changes = {};
            $('button.save', this.$el).hide();
        },
        editField: function (event) {
            var $this = $(event.currentTarget),
                value = $this.text().replace(/^\s+|\s+$/g,''),
                field = $this.data('field');
            this.changes[field] = value;
            $('button.save', this.$el).show();
        },
        showErrors: function (errors) {
            _.map(errors, function (fieldErrors, name) {
                var field = $('[data-field=' + name + ']', this.$el);
                if (field.length === 0) {
                    field = $('[data-field]', this.$el).first();
                }
                function appendError(msg) {
                    var parent = field.parent('.with-label'),
                        error = this.errorTemplate({msg: msg});
                    if (parent.length  === 0) {
                        field.before(error);
                    } else {
                        parent.before(error);
                    }
                }
                _.map(fieldErrors, appendError, this);
            }, this);
        }
    });

    var TaskItemView = TemplateView.extend({
        tagName: 'div',
        className: 'task-item',
        templateName: '#task-item-template',
        events: {
            'click': 'details'
        },
        initialize: function (options) {
            TemplateView.prototype.initialize.apply(this, arguments);
            this.task = options.task;
            this.task.on('change', this.render, this);
            this.task.on('remove', this.remove, this);
        },
        getContext: function () {
            return {task: this.task};
        },
        render: function () {
            TemplateView.prototype.render.apply(this, arguments);
            this.$el.css('order', this.task.get('order'));
        },
        details: function () {
            var view = new TaskDetailView({task: this.task});
            this.$el.before(view.el);
            this.$el.hide();
            view.render();
            view.on('done', function () {
                this.$el.show();
            }, this);
        }
    });

    //基于TemplateView扩展，并使用现有的钩子(回调)。
    var SprintView = TemplateView.extend({
        templateName: '#sprint-template',
        initialize: function (options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments);
            //该模型仅知道模型的id。随后的fetch方法将从API检索剩余的详细信息。
            this.sprintId = options.sprintId;
            this.sprint = null;
            //tasks属性为关联数组
            this.tasks = {};
            //创建SprintView时，会为每种可能的状态案例创建StatusView。
            this.statuses = {
                unassigned: new StatusView({
                    sprint: null, status: 1, title: 'Backlog'}),
                todo: new StatusView({
                    sprint: this.sprintId, status: 1, title: 'Not Started'}),
                active: new StatusView({
                    sprint: this.sprintId, status: 2, title: 'In Development'}),
                testing: new StatusView({
                    sprint: this.sprintId, status: 3, title: 'In Testing'}),
                done: new StatusView({
                    sprint: this.sprintId, status: 4, title: 'Completed'})
            };
            app.collections.ready.done(function () {
                //返回结果时，app.tasks将触发add事件，该事件将绑定到视图上的addTask。
                app.tasks.on('add', self.addTask, self);
                //原始模型fetch已被getOrFetch取代。由于它返回一个延迟对象，因此必须在sprint可用时将其与一个完成回调链接。
                app.sprints.getOrFetch(self.sprintId).done(function (sprint) {
                    self.sprint = sprint;
                    self.render();
                    // Add any current tasks
                    //如果我们在sprint页面之间导航，则可能已经存储在客户端上的任务。那些也需要添加。请记住，并非所有任务都与此sprint相关，并且还需要在addTask回调中过滤掉它们。
                    app.tasks.each(self.addTask, self);
                    // Fetch tasks for the current sprint
                    sprint.fetchTasks();
                }).fail(function (sprint) {  //如果从API获取模型会引发错误，则会触发失败回调。在这种情况下，我们在渲染模板之前将sprint表示为无效。
                    self.sprint = sprint;
                    self.sprint.invalid = true;
                    self.render();
                });
                // Fetch unassigned tasks
                app.tasks.getBacklog();
            });
        },
        getContext: function () {
            return {sprint: this.sprint};
        },
        //渲染SprintView将删除子视图的现有元素。需要将子视图重新插入DOM中，并且需要再次绑定事件。
        render: function () {
            TemplateView.prototype.render.apply(this, arguments);
            _.each(this.statuses, function (view, name) {
                $('.tasks', this.$el).append(view.el);
                view.delegateEvents();
                view.render();
            }, this);
            _.each(this.tasks, function (view, taskId) {
                //tasks数组将task.id映射到任务的子视图实例。addTask已更新为分配。以迭代映射更新渲染。
                var task = app.tasks.get(taskId);
                view.remove();
                this.tasks[taskId] = this.renderTask(task);
            }, this);
        },
        //过滤到与此视图相关的任务。它还包含所有添加的任务的列表，以防视图需要再次呈现。
        addTask: function (task) {
            if (task.inBacklog() || task.inSprint(this.sprint)) {
                this.tasks[task.get('id')] = this.renderTask(task);
            }
        },
        //渲染任务当前由内联的Underscore模板处理。
        renderTask: function (task) {
            //创建新TaskItemView的实例并循环遍历状态子视图。renderTask现在返回子视图，addTask用于跟踪查看映射的任务。
            var view = new TaskItemView({task: task});
            _.each(this.statuses, function (container, name) {
                if (container.sprint == task.get('sprint') &&
                    container.status == task.get('status')) {
                    container.addTask(view);
                }
            });
            view.render();
            return view;
        }
    });

    app.views.HomepageView = HomepageView;
    app.views.LoginView = LoginView;
    app.views.HeaderView = HeaderView;
    //将SprintView添加到app.views中，以便路由器可以使用它。
    app.views.SprintView = SprintView;

})(jQuery, Backbone, _, app);
