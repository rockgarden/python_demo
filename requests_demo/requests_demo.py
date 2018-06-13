# https://github.com/HaifengHong/WebCrawling

import requests

r = requests.get('https://www.baidu.com')
# header 中没有指定 字符集
print(r.encoding)  # charset未指定时默认ISO-8859-1
print(r.apparent_encoding)
r.encoding = r.apparent_encoding
print(r.text)
r.json()  # TODO: json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
