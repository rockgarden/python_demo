# -*- coding:utf-8 -*-
import os
import re
import traceback

import requests
from bs4 import BeautifulSoup


def get_html_text(url, code="utf-8"):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code  # r.apparent_encoding 解析效率低
        return r.text
    except:
        return ''


def get_stock_list(lst, stock_url):  # lst列表保存的列表类型，存储了所有股票的信息；stockURL获得股票列表的url网站
    html = get_html_text(stock_url, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])  # 为何加[0]?
        except:
            continue


def get_stock_info(lst, stock_url, file_path):
    count = 0  # 为了增加进度条
    for stock in lst:
        url = stock_url + stock + '.html'
        html = get_html_text(url)
        try:
            if html == "":  # 判断是否为空页面
                continue
            info_dict = {}  # 存储当前从一个页面中返回的或记录的所有个股信息
            soup = BeautifulSoup(html, 'html.parser')  # 构建解析网页的类型
            stock_info = soup.find('div', attrs={'class': 'stock-bets'})
            # find是找第一个div标签。所有股票信息封装在div标签下，它的属性是class="stock-bets",所以可以搜索这个标签，找到股票所存在的大标签信息，定义为stockInfo

            name = stock_info.find_all(attrs={'class': 'bets-name'})[0]
            # AttributeError: 'NoneType' object has no attribute 'find_all'
            info_dict.update({'股票名称': name.text.split()[0]})
            # 因为某些名称后面还关联了其他标识符，采用空格分开后获得第一部分也就是完整的股票名称，其余部分舍弃。

            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                info_dict[key] = val

            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
                count += 1
                print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end='')  # \r增加不换行的动态显示的进度条
        except:
            count += 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end='')
            traceback.print_exc()
            continue


def make_path(root, path):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
            print(root)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write("")
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print('文件保存失败')


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'  # 获得股票列表的链接
    stock_info_url = 'https://gupiao.baidu.com/stock/'  # 获得股票信息的链接的主体部分
    root = os.getcwd() + "/output"
    output_file = root + "/BaiduStockInfo.txt"
    make_path(root, output_file)
    stock_list = []  # 股票信息变量
    get_stock_list(stock_list, stock_list_url)
    get_stock_info(stock_list, stock_info_url, output_file)


if __name__ == '__main__':
    main()

url = "http://image.ngchina.com.cn/2017/0411/20170411122223468.jpg"
print("当前工作目录为 : %s" % os.getcwd())
root = os.getcwd() + "/output"
path = root + "/" + url.split('/')[-1]
