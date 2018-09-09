# django 2.1

## Command 

1. 用模板创建项目


    $ django-admin.py startproject foo --template=project_name


## Tips
Django被称为模型 - 模板 - 视图（MTV）框架。 视图部分通常检查传入的HTTP请求，并查询或构造发送到表示层的必要数据。

Web服务器网关接口（WSGI）是Web服务器如何与Django等应用程序框架进行通信的规范，由PEP 333定义并在PEP 3333中进行了改进。
对于使用WSGI的Web服务器有很多选择，包括Apache通过mod_wsgi ，Gunicorn，uWSGI，CherryPy，Tornado和Chaussette。
这些服务器中的每一个都需要使用正确定义的WSGI应用程序。 Django有一个简单的界面，可以通过get_wsgi_application创建这个应用程序。
    
    $ gunicorn xxx --log-file=-

HTTP本身是无状态协议，这意味着每个到服务器的请求都独立于先前的请求。 如果需要特定状态，则必须在应用程序层添加。 
像Django这样的框架使用cookie和其他机制将同一客户端发出的请求联系在一起。

