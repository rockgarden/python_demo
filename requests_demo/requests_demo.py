# http://www.python-requests.org/en/master/

import requests

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# r.status_code
# # 200
# type(r)
# r.headers['content-type']
# # 'application/json; charset=utf8'
# r.encoding
# # 'utf-8'
# r.text
# # u'{"type":"User"...'
# r.json()
# # {u'private_gists': 419, u'total_private_repos': 77, ...}

r = requests.get('https://www.baidu.com')
# header 中没有指定 字符集
r.apparent_encoding
r.encoding = r.apparent_encoding
print(r.text)
