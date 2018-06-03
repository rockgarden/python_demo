# CGI脚本输出CGI的环境变量

# hello_get.py文件的代码

# CGI处理模块
import cgi

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")
# 文件保存后修改 hello_get.py，修改文件权限为 755：
# chmod 755 hello_get.py


# 简单的表单实例：GET方法
# 以下是一个通过HTML的表单使用GET方法向服务器发送两个数据，提交的服务器脚本同样是hello_get.py文件.
'''
hello_get.html 代码如下：
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/hello_get.py" method="get">
站点名称: <input type="text" name="name">  <br />

站点 URL: <input type="text" name="url" />
<input type="submit" value="提交" />
</form>
</body>
</html>
'''
# 默认情况下 cgi-bin 目录只能存放脚本文件，我们将 hello_get.html 存储在 test 目录下，修改文件权限为 755：
# chmod 755 hello_get.html


# 使用POST方法传递数据
# 使用POST方法向服务器传递数据是更安全可靠的，像一些敏感信息如用户密码等需要使用POST传输数据。
# 以下同样是hello_get.py ，它也可以处理浏览器提交的POST表单数据:

# CGI处理模块
import cgi

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")
# 以下为表单通过POST方法（method="post"）向服务器脚本 hello_get.py 提交数据:
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/hello_get.py" method="post">
站点名称: <input type="text" name="name">  <br />
站点 URL: <input type="text" name="url" />
<input type="submit" value="提交" />
</form>
</body>
</html>
</form>
'''

# 通过CGI程序传递checkbox数据
# checkbox用于提交一个或者多个选项数据，HTML代码如下：
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/checkbox.py" method="POST" target="_blank">
<input type="checkbox" name="runoob" value="on" /> 菜鸟教程
<input type="checkbox" name="google" value="on" /> Google
<input type="submit" value="选择站点" />
</form>
</body>
</html>
'''
# checkbox.py 文件的代码
import cgi

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
    google_flag = "是"
else:
    google_flag = "否"

if form.getvalue('runoob'):
    runoob_flag = "是"
else:
    runoob_flag = "否"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 菜鸟教程是否选择了 : %s</h2>" % runoob_flag)
print("<h2> Google 是否选择了 : %s</h2>" % google_flag)
print("</body>")
print("</html>")
# 修改 checkbox.py 权限：chmod 755 checkbox.py


# 通过CGI程序传递Radio数据
# Radio 只向服务器传递一个数据，HTML代码如下：
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/radiobutton.py" method="post" target="_blank">
<input type="radio" name="site" value="runoob" /> 菜鸟教程
<input type="radio" name="site" value="google" /> Google
<input type="submit" value="提交" />
</form>
</body>
</html>
'''
# radiobutton.py 脚本代码
import cgi

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = "提交数据为空"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 选中的网站是 %s</h2>" % site)
print("</body>")
print("</html>")
# radiobutton.py 权限：chmod 755 radiobutton.py


# 通过CGI程序传递 Textarea 数据
# Textarea 向服务器传递多行数据，HTML代码如下：
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/textarea.py" method="post" target="_blank">
<textarea name="textcontent" cols="40" rows="4">
在这里输入内容...
</textarea>
<input type="submit" value="提交" />
</form>
</body>
</html>
'''
# textarea.py 脚本代码
import cgi

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "没有内容"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 输入的内容是：%s</h2>" % text_content)
print("</body>")
print("</html>")
# 修改 textarea.py 权限：chmod 755 textarea.py


# 通过CGI程序传递下拉数据。
# HTML 下拉框代码如下：
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<form action="/cgi-bin/dropdown.py" method="post" target="_blank">
<select name="dropdown">
<option value="runoob" selected>菜鸟教程</option>
<option value="google">Google</option>
</select>
<input type="submit" value="提交"/>
</form>
</body>
</html>
'''
# dropdown.py 脚本代码
import cgi

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('dropdown'):
    dropdown_value = form.getvalue('dropdown')
else:
    dropdown_value = "没有内容"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 选中的选项是：%s</h2>" % dropdown_value)
print("</body>")
print("</html>")
# 修改 dropdown.py 权限：chmod 755 dropdown.py


# CGI中使用Cookie
# 在 http 协议一个很大的缺点就是不对用户身份的进行判断，这样给编程人员带来很大的不便， 而 cookie 功能的出现弥补了这个不足。
# cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据 ，当下次客户访问脚本时取回数据信息，从而达到身份判别的功能，cookie 常用在身份校验中。
# 　
# cookie的语法
# http cookie的发送是通过http头部来实现的，他早于文件的传递，头部set-cookie的语法如下：
# Set-cookie:name=name;expires=date;path=path;domain=domain;secure
# name=name: 需要设置cookie的值(name不能使用";"和","号),有多个name值时用 ";" 分隔，例如：name1=name1;name2=name2;name3=name3。
# expires=date: cookie的有效期限,格式： expires="Wdy,DD-Mon-YYYY HH:MM:SS"
# path=path: 设置cookie支持的路径,如果path是一个路径，则cookie对这个目录下的所有文件及子目录生效，例如： path="/cgi-bin/"，如果path是一个文件，则cookie指对这个文件生效，例如：path="/cgi-bin/cookie.cgi"。
# domain=domain: 对cookie生效的域名，例如：domain="www.runoob.com"
# secure: 如果给出此标志，表示cookie只能通过SSL协议的https服务器来传递。
# cookie的接收是通过设置环境变量HTTP_COOKIE来实现的，CGI程序可以通过检索该变量获取cookie信息。


# Cookie设置
# Cookie的设置非常简单，cookie会在http头部单独发送。以下实例在cookie中设置了name 和 expires：
print('Content-Type: text/html')
print('Set-Cookie: name="菜鸟教程";expires=Wed, 28 Aug 2016 18:30:00 GMT')
print()
print("""
        <html>
          <head>
            <meta charset="utf-8">
            <title>菜鸟教程(runoob.com)</title>
          </head>
            <body>
                <h1>Cookie set OK!</h1>
            </body>
        </html>
        """)
# 将以上代码保存到 cookie_set.py，并修改 cookie_set.py 权限：chmod 755 cookie_set.py
# 以上实例使用了 Set-Cookie 头信息来设置Cookie信息，可选项中设置了Cookie的其他属性，如过期时间Expires，域名Domain，路径Path。
# 这些信息设置在 "Content-type:text/html"之前。


# 检索Cookie信息
# Cookie信息检索页非常简单，Cookie信息存储在CGI的环境变量HTTP_COOKIE中，存储格式如下：
# key1=value1;key2=value2;key3=value3....
# 以下是一个简单的CGI检索cookie信息的程序：
# CGI检索cookie信息的程序
# cookie_get.py
import os

# import Cookie

print("Content-type: text/html")
print()

print("""
        <html>
        <head>
        <meta charset="utf-8">
        <title>菜鸟教程(runoob.com)</title>
        </head>
        <body>
        <h1>读取cookie信息</h1>
        """)

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print("cookie data: " + data + "<br>")
    except KeyError:
        print("cookie 没有设置或者已过去<br>")
print("""
</body>
</html>
""")
# 将以上代码保存到 cookie_get.py，并修改 cookie_get.py 权限：chmod 755 cookie_get.py


# 文件上传实例
# HTML设置上传文件的表单需要设置 enctype 属性为 multipart/form-data，代码如下所示：
'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
 <form enctype="multipart/form-data" 
                     action="/cgi-bin/save_file.py" method="post">
   <p>选中文件: <input type="file" name="filename" /></p>
   <p><input type="submit" value="上传" /></p>
   </form>
</body>
</html>
'''
# save_file.py脚本文件代码
import cgi, os
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())

    message = '文件 "' + fn + '" 上传成功'

else:
    message = '文件没有上传'

print("""\
        Content-Type: text/html\n
        <html>
        <head>
        <meta charset="utf-8">
        <title>菜鸟教程(runoob.com)</title>
        </head>
        <body>
           <p>%s</p>
        </body>
        </html>
        """ % (message,))
# 将以上代码保存到save_file.py，并修改save_file.py权限：chmod 755 save_file.py
# 如果你使用的系统是Unix/Linux，你必须替换文件分隔符，在window下只需要使用open()语句即可：
fn = os.path.basename(fileitem.filename.replace("\\", "/"))

# 文件下载对话框
# 我们先在当前目录下创建 foo.txt 文件，用于程序的下载。
# 文件下载通过设置HTTP头信息来实现，功能代码如下：
# HTTP 头部
print("Content-Disposition: attachment; filename=\"foo.txt\"")
print()
# 打开文件
fo = open("foo.txt", "rb")

str = fo.read();
print(str)

# 关闭文件
fo.close()
