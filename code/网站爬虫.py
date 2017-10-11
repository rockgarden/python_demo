# python文件写入也可以进行网站爬虫，以下代码是打开project.txt文件，并向里面写入http://www.baidu.com网站代码。
from urllib import request

response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
# TypeError: 'list' object is not callable
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()