import requests
from bs4 import BeautifulSoup  # 从bs4库里导入BeautifulSoup类 #import bs4

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
Soup = BeautifulSoup(demo, "html.parser")  # bs4的HTML解析器
print(Soup.prettify())  # prettify()函数，使代码格式显示得标准一些，最后加一个换行符
