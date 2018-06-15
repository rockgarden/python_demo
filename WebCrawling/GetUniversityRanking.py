# -*- coding: utf-8 -*-
import bs4
import requests


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)  # 注意是timeout，而不是time
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"


def fill_university_list(ulist, html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    th = soup.thead
    if isinstance(th, bs4.element.Tag):  # 检查是否是 Tag
        ths = th('th')  # 相当于tds = tr.find_all('td')
        # print(ths)
        ulist.append([ths[0].string, ths[1].string, ths[2].string, ths[3].string])
    for tr in soup.find('tbody').children:  # find()直接返回第一个结果元素（不是列表）。注意表示方法，find()不能省略，跟find_all()不一样，children是迭代类型
        # for tr in soup.find_all('tbody', limit = 1).children:
        '''
        # find_all()返回列表。这种写法运行会出错（因为.children的是具体元素而不是列表，如soup.head.contents）：
        # AttributeError: ResultSet object has no attribute 'children'.
        # You're probably treating a list of items like a single item.
        # Did you call find_all() when you meant to call find()?
        '''
        if isinstance(tr, bs4.element.Tag):  # 检查是否是 Tag
            tds = tr('td')  # 相当于tds = tr.find_all('td')
            # print(tds)
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


# def print_university_list(ulist, num):
#     print("{:^10}\t{:^10}\t{:^10}".format("排名", "学校名称", "省份"))
#     for i in range(num):
#         u = ulist[i]
#         print("{:^10}\t{:^10}\t{:^10}".format(u[0], u[1], u[2]))

# 优化输出格式后的printUnivList
def print_university_list(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:{3}^10}\t{4:^10}"  # {3}指打印时需要填充时使用format函数的第三个变量，即中文空格
    # print(tplt.format("排名", "学校名称", "省份", chr(12288)))  # chr(12288)表示中文空格
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288), u[3]))


def main():
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    university_info = []
    html = get_html_text(url)
    fill_university_list(university_info, html)
    print_university_list(university_info, 20)


if __name__ == '__main__':
    main()
