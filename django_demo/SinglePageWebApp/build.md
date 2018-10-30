

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


### Sprint详细信息页面
**渲染Sprint**
* 从API获取sprint数据并将其传递到模板以呈现细节。让我们在/js/views.js中构建我们的视图，指向这个新视图模板并传入该数据。
* 将视图添加到路由器之前，需要将sprint-template添加到我们的index.html文件中（/templates）

**路由Sprint详细信息**
* 新SprintView在创建时需要sprintId。需要从路径捕获此值并将其传递给视图。Backbone允许捕获部分路由。将路由添加到router.js文件中的sprint详细信息页面。

**使用客户端状态**
* 在客户端上，我们不需要在每次需要模型对象时都使用API，sprint可能已经在app.sprints集合中。
* 可以在models.js中使用一个简单的集合助手 collection helper 来解决这个问题。
* views.js中更新SprintView以使用这种集合助手。当发现sprint时，无论是本地还是来自API，都需要处理成功的情况，以及当给定sprintId不存在sprint时的失败情况。
* 更新模板（xx/templates/xx/index.html）以处理无效的sprint案例。

**渲染任务**
* 从任务状态视图开始，在js/views.js中增加statusView.
* 定义三个选项：sprint，status和title。需要将基本模板添加到 templates/index.html。
* StatusView共有五个实例，由SprintView管理，一旦视图初始化，应该js / views.js中实现。
* 在 static/js/models.js中添加两个辅助方法，为每个sprint提取任务。
* 两个辅助方法都没有返回任何东西。相反，应用程序将在添加这些项目时使用app.tasks集合触发的事件。 这也将由js/views.js中的SprintView处理。
* addTask回调将处理从API接收的任务以及客户端上已有的任务。仅当任务与sprint或backlog任务相关时，才应呈现该任务。让我们在 js / models.js中为Task模型添加一些新方法来帮助理清这个逻辑。
* 返回到static/js/views.js中的SprintView来处理添加任务。

**AddTaskView**
* AddTaskView build in board/static/board/js/views.js
* 添加了一个新的事件处理程序来处理取消按钮。并将它作为FormView中的默认值（/js/views.js）
* 在/js/views.js中更新状态视图以呈现这个新表单。
* 新任务模板添加到index.html文件以完成任务创建工作流程。
* 提供一个更具可读性和可用性的结构，我们将在/css/board.css中添加一些CSS。

### CRUD任务

**在Sprint中渲染任务**
* 在/js/views.js中创建TaskItemView，以使用此模板呈现每个任务。TaskItemView初始化时，它会将自身绑定到模型的更改与删除事件。
如果在客户端上更新了模型实例，则视图将再次呈现自身以反映这些更新。 如果删除模型，视图将从DOM中删除自身。
渲染还在元素上设置CSS顺序，灵活盒布局使用它来正确呈现顺序，而不管DOM中的位置如何。
* 在js/views.js中的SprintView.renderTask方法中使用TaskItemView。
* 在css/board.css添加一些小的样式来分隔任务。

**更新任务**
* 首先在/js/views.js中创建模板添任务详细视图。
* 模板添任务详细信息加到index.html，并包含用于在sprint中创建新任务的相应表单。
* 保存按钮默认隐藏，仅在保存更改时显示。当用户单击列表中的任务时，需要创建TaskDetailView实例。
TaskItemView需要侦听此事件。在/js/views.js中实现这些要求。

**内联编辑功能**
* 通过在可信的HTML5元素上使用自定义方法来添加创建内联可编辑内容的功能JS/views.js。
* 将新方法添加我们的模板index.html，并为我们想要内联编辑的每个部分分配contenteditable。DOM的特定区域通过data-field属性与模型字段相关联。
* 默认的FormView.showErrors无法显示API中的错误。FormView.showErrors依赖于<input>和<label>标记，使名称与模型名称匹配。
* 在js/views.js中TaskDetailView定义自己的showErrors，它将错误与基于data-field属性的正确区域相关联。
* css/board.css中添加detail/edit状态样式。