import os
import re
import sys
import unittest

from pyquery import PyQuery as pq

sys.path.insert(0, os.path.abspath('..'))


class QueryStringSuite(unittest.TestCase):
    htmlFile = 'assets/test.html'

    def test_simple(self):
        result = pq(filename=self.htmlFile)

        dicts = []

        for tr in result("tr")[2:]:
            tr_doc = pq(tr)
            dict_n = {}
            notice_id = tr_doc.attr("onclick").split("'")[1]
            dict_n["id"] = notice_id
            dict_n["company"] = pq(tr_doc("td")[0]).text()
            dict_n["type"] = pq(tr_doc("td")[1]).text()
            dict_n["title"] = pq(tr_doc("td")[2]).text()
            dict_n["date"] = pq(tr_doc("td")[3]).text()
            dict_n["url"] = "https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=" + notice_id

        for tr in result("tr").items():
            # 过滤 None
            if tr.attr("onclick"):
                dict_n = {}
                notice_id = tr.attr("onclick").split("'")[1]
                dict_n["id"] = notice_id
                # TODO: 强转为list，解决'generator' object is not subscriptable
                tds = list((tr('td').items()))
                dict_n["company"] = tds[0].text()
                dict_n["type"] = tds[1].text()
                dict_n["title"] = tds[2].text()
                dict_n["date"] = tds[3].text()
                dict_n["url"] = "https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=" + notice_id
                print(dict_n)
                dicts.append(dict_n)

    def test_url_openself(self):
        url = 'https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=479700'
        # 478023 477256 478772 478825 479328 479412 479700

        # 去除无效元素 script
        result = pq(url, encoding="utf-8").remove('script')

        topics = {}

        # 无用内容列表
        useless_topics = ['免责声明', '发布公告的媒介', '电子采购应答规则']
        # 项目概况相关主题列表
        project_overview_topics = ['项目概况与招标范围', '项目概况', '招标范围', '项目概况与招标内容',
                                   '采购说明', '采购内容', '采购内容及相关内容', '采购项目概况', '采购货物的名称', '采购项目的名称',
                                   '工程概况与比选内容', '比选项目的名称', ]
        # 截止日期正则表达式
        deadline_pattern = re.compile('截止时间(.*)(\d+)年(\d{1,2})月(\d{1,2})日')
        # 日期正则表达式 年月日上午时
        date_pattern = re.compile('(\d+)年(\d{1,2})月(\d{1,2})日(.*)(\d{1,2})时')
        # 无效字符字典
        useless_char = dict.fromkeys(ord(c) for c in u"\xa0\n\t_ ")

        # 去除空元素
        tr_items = result('#mobanDiv > table tr').items()
        tr_items_nonzero = []
        for item in tr_items:
            # print(item('span').length)
            if item('span').length > 0:
                tr_items_nonzero.append(item)

        # !提取--项目名称
        topics['项目名称'] = result('h1').text()

        # !提取--招标人
        last_tr = tr_items_nonzero[-1]
        last_tr_span_text = pq(pq(last_tr)('span')[0]).text()
        print('\n', last_tr_span_text)
        if last_tr_span_text.count("："):
            text = last_tr_span_text.split("：")[1]
            if text.count('/'):
                topics['招标人'] = text.split("/")[0]
                topics['招标代理机构'] = text.split("/")[1]
            else:
                topics['招标人'] = text
                topics['招标代理机构'] = '无'

        # !提取--采购内容概况
        for each in tr_items_nonzero:
            span_list = list(each('tr > td > span').items())
            if len(span_list) > 0:
                topic = span_list[0].text().split('、')[1]
                while topic in project_overview_topics:
                    print("\n 采购内容概况: ", topic)
                    topics['采购内容概况'] = pq(each).clone().remove('table')('div').text().translate(useless_char)
                else:
                    print("\n 采购内容概况: ", topic)
                    topics['采购内容概况'] = '解析失败'

        # !提取--其它主题
        for each in result('#mobanDiv > table tr').items():
            span = each('tr > td > span')
            # 过滤无主题内容
            if span.length > 0:
                topic = pq(span[0]).text().split('、')[1]
                if topic not in (useless_topics + project_overview_topics):
                    print(topic)
                    len_p = each('p').length
                    len_div = each('div').length
                    # print("\n p 元素: ", len_p, "\n div 元素: ", len_div)
                    infos = []
                    items = []
                    if len_p > 0:
                        items = each('p').items()
                    else:
                        if len_div > 0:
                            items = each('div').items()

                    for item in items:
                        text = item.clone().text().translate(useless_char)
                        # !提取--投标截止时间
                        deadline = deadline_pattern.findall(text)
                        if len(deadline) > 0:
                            print('投标截止时间', deadline)
                            for m in date_pattern.finditer(text):
                                topics['投标截止时间'] = m.group()
                        else:
                            infos.append(text)
                    topics[topic] = infos
                    print(infos)

        print("\n noticeBean: ", topics)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QueryStringSuite))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())

# if topic == "联系方式":
#     # contact_info = each('#ggdiv3').text().splitlines()
#     # print("MsoNormal: ", each('#ggdiv3 .MsoNormal > span').text())
#     # dict_c = {}
#     # for info in contact_info:
#     #     print("\n", "".join(info.split()))
#     #     # Del Non - breaking space
#     #     # dict_c["".join(info.split("：")[0].split())] = info.split("：")[1]
#     # dict_n.update(dict_c)
#     # print(dict_c)
#     infos = []
#     for item in each('p').items():
#         infos.append("".join(item.text().split()))
#     topics['联系方式'] = infos
#     print(infos)
# elif topic == "资格要求":
#     infos = []
#     for item in each('p').items():
#         infos.append("".join(item.text().split()))
#     topics['资格要求"'] = infos
#     print(infos)
# elif topic == "获取采购文件及应答文件的递交":
#     infos = []
#     for item in each('p').items():
#         infos.append("".join(item.text().split()))
#     topics['应答说明'] = infos
#     print(infos)
# elif topic == "获取比选文件":
#     infos = []
#     for item in each('div').items():
#         infos.append("".join(item.text().split()))
#     topics['获取比选文件'] = infos
#     print(infos)
# elif topic == "应答文件的递交":
#     infos = []
#     for item in each('div').items():
#         infos.append("".join(item.text().split()))
#     topics['应答文件的递交'] = infos
#     print(infos)
# elif topic == "采购货物的名称":
#     infos = []
#     for item in each('div').items():
#         infos.append("".join(item.text().split()))
#     topics['应答文件的递交'] = infos
#     print(infos)
