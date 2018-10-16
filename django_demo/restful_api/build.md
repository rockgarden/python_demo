## bulid Commands 

    $ pip3 install djangorestframework Markdown django-filter
    
    $ django-admin.py startproject restful_api
    $ cd restful_api
    $ python3 manage.py startapp api
    
    /// 修改 restful_api/settings.py
    
    $ pip3 install psycopy2
    $ pip3 install psycopg2-binary
           
    $ pg_ctl -D /usr/local/var/postgres start
    $ createdb -E UTF-8 api
    
    /// 修改 restful_api/urls.py
    $ python3 manage.py runserver
    /// test http://127.0.0.1:8000/api/token/
    /// get 405
    /// test http://127.0.0.1:8000 
    /// get 404 
    /// path error: The empty path didn't match any of these.
  
    /// 第一步 - 创建model层
    /// 创建 api/models.py 
    $ python3 manage.py makemigrations api
    $ python3 manage.py migrate
    $ python3 manage.py createsuperuser
    /// wangkan freestar
    $ python3 manage.py runserver
    
    /// 创建 序列化器 serializers.py 实现API
    /// 修改 api/views.py 创建 ViewSet
    /// Serializer 与 ViewSet 一一对应
    
    /// 创建 api/urls.py 实现连接路由
    /// 修改 restful_api/urls.py 将连接路由加入根节点URL
    
    /// edit api/serializers.py 链接资源文件
    $ python3 manage.py runserver
    /// test http://127.0.0.1:8000/api
    /// eg: 
    /// test http://127.0.0.1:8000/api/sprints/
    /// 需要鉴权 wangkan/freestar
    
    /// 第二步 - 创建filter和view层的层次结构
    /// edit api/views.py 添加过滤器
    /// new api/my_filters.py 实现自定义过滤器
    /// edit api/views.py 引入自定义过滤器
    http://127.0.0.1:8000/api/tasks/?search=foor
    http://127.0.0.1:8000/api/tasks/?search=first
    
    /// edit api/serializers.py 添加链接将 sprint user task 关联起来

## Error
    /// django.db.utils.OperationalError: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
        当报此错误时表示 PostgreSQL 没有启动, 需要重新 运行 postgres start
    $ pg_ctl -D /usr/local/var/postgres start