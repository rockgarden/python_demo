# python_demo

- **python version 3.6.5**

- **重要：在一个项目下 所有的 modules 是一起编译的，也就是说不同的 modules 文件夹类名等不能重复！**

## 使用
首先运行 librarys_batch_installer.py，安装三方库。

## 介绍

  1. code: python 语言入门
  2. game: python 项目练习
  3. matplotlib: python 统计分析库入门
  4. requests_demo: requests 网络请求库入门
  5. beautiful_soup_demo: bs4 网页解析库入门
  6. socket_demo: socket 库开发
  7. elasticsearch: 文本搜索
  
## 相关库

- [rsa](https://pypi.org/project/rsa/):RSA实现, 它支持加密和解密, 签名和验证签名, 以及根据PKCS＃1版本1.5生成密钥.
- [PIL-pillow](https://pypi.org/project/Pillow/):图像处理(安装命令 pip install pillow)。

- [PyInstaller-pyintaller](http://www.pyinstaller.org):打包Python源文件为可执行文件(安装命令 pip install pyintaller).
- [Wheels](https://pythonwheels.com):第三方打包工具(安装命令 pip install wheel), [github_wheel](https://github.com/pypa/wheel).

- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/):GUI库, QT5应用的框架, 跨平台的工具包.

- [PyMySQL](https://pypi.org/project/PyMySQL/):可代替MySQLdb-python.

- [GitPython](https://pypi.org/project/GitPython/):git的开发库.


    # 应用主文件 __init.py__/app.py
    # 手动指定将MySQLdb转给pymysql处理
    import pymysql
    pymysql.install_as_MySQLdb() 


- [jieba](https://pypi.org/project/jieba/):中文分词组件
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy):字符串模糊匹配

- [wordcloud](https://github.com/amueller/word_cloud):词云组件

- [chardet](https://github.com/chardet/chardet):通用字符编码检测器

### 数据分析
- [NumPy-numpy](http://www.numpy.org):N维数据表示和运算
- [pandas](http://pandas.pydata.org):数据分析高层次应用库
- [SciPy-scipy](https://www.scipy.org):数学、科学和工程计算功能库
- [Matplotlib-matplotlib](https://matplotlib.org)二维数据可视化功能库
- [Seaborn](http://seaborn.pydata.org/):统计类数据可视化功能库
- [mayavi](http://docs.enthought.com/mayavi/mayavi/):三维科学数据可视化功能库

### 文本处理
- [pypdf2](https://pythonhosted.org/PyPDF2/):用来处理pdf文件的工具集, [github](https://github.com/mstamy2/PyPDF2)
- [nltk](http://nltk.org/):自然语言文本处理第三方库
- [python-docx](https://github.com/python-openxml/python-docx):创建或更新Microsoft Word文件的第三方库

### 机器学习
- [scikit-learn](http://scikit-learn.org/):机器学习和数据挖掘组件库
- [tensorflow](https://www.tensorflow.org/):机器学习计算框架
- [mxnet](https://mxnet.apache.org):基于神经网络的深度学习计算框架[github](https://github.com/apache/incubator-mxnet)

### 网络爬虫
- [requests](http://www.python-requests.org/):HTTP协议访问及页面级网络爬虫功能库
- [scrapy](https://scrapy.org):专业的网络爬虫框架
- [pyspider](http://docs.pyspider.org):强大的Web页面爬取系统(面向一般用户)

### Web信息提取
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4):HTML和XML解析器 
- [re](https://docs.python.org/3.6/library/re.html):(自带)正则表达式解析和处理功能库
- [goose3](http://goose3.readthedocs.io/en/latest/index.html):提取文章类型Web页面的功能库, [github_python-goose](https://github.com/goose3/goose3),另有JAVA版支持python2 [goose-extractor](https://github.com/grangier/python-goose)

### Web网站开发
- [django](https://www.djangoproject.com/)最流行的Web开发框架, [github](https://github.com/django/django)
- [pyramid](https://trypyramid.com/):规模适中的Web应用框架
- [Flask](https://www.palletsprojects.com/p/flask/):轻量级Web开发框架.

### 文本搜索
- [elasticsearch](https://github.com/elastic/elasticsearch-py):文本搜索库.

### 网络应用开发
- [werobot](https://github.com/offu/WeRoBot):微信公众号开发框架.
- [aip](http://ai.baidu.com/docs#/Begin/top):百度AI开放平台接口
<pre>
    pip3 install git+https://github.com/Baidu-AIP/python-sdk.git@master
</pre>
- [MyQR](https://github.com/sylnsfar/qrcode):二维码生成第三方库

### 图形用户界面
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/):基于Qt的专业级GUI开发框架 
- [wxPython](https://wxpython.org):跨平台GUI开发框架
- [PyGObject](https://pygobject.readthedocs.io/en/latest/):使用GTK+开发GUI的功能库

### 游戏开发
- [Pygame](http://www.pygame.org/):简单小游戏开发框架
- [Panda3D](https://www.panda3d.org/):开源、跨平台的3D渲染和游戏开发库
- [cocos2d](http://python.cocos2d.org/):构建2D游戏和图形界面交互式应用的框架

### 虚拟现实
- [python-vrzero](https://github.com/WayneKeenan/python-vrzero):在树莓派上开发VR应用的Python库
- [pyovr](https://github.com/cmbruns/pyovr):开发Oculus Rift的Python库
- [Vizard](http://www.worldviz.com/vizard-virtual-reality-software):基于Python的通用VR开发引擎

### 图形艺术
- [quade](http://www.michaelfogleman.com/static/quads/):迭代的艺术, [github](https://github.com/fogleman/Quads)
- [ascii_art](https://github.com/lord63/ascii_art):ASCII艺术库-普通图片转为ASCII艺术风格
- [turtle](https://docs.python.org/3/library/turtle.html):(自带)海龟绘图库

### 其它
- [pyquery](https://github.com/gawel/pyquery):类似于jquery的python库

- SymPy 数学符号计算工具pip install sympy
- Networkx 复杂网络和图结构的建模和分析pip install networkx
- PyOpenGL 多平台OpenGL开发接口 pip installpyopengl
- docopt Python命令行解析 pip install docopt

## 附录
[lib2to3](https://docs.python.org/3.5/library/2to3.html?highlight=unicode#module-lib2to3):将可运行的python2转换成python3
运行在command line: 2to3 xx.py