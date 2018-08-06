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
        url = 'https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=478825'
        # 478023 477256 478772 478825
        response = pq(url, encoding="utf-8")
        topics = {}
        # 无用内容
        useless_topics = ['免责声明', '发布公告的媒介', '电子采购应答规则']
        topics['项目名称'] = response('h1').text()
        # 建立日期的正则表达式
        deadline_pattern = re.compile('投标截止时间(.*)(\d+)年(\d{1,2})月(\d{1,2})日')
        date_pattern = re.compile('(\d+)年(\d{1,2})月(\d{1,2})日')
        # 无效字符
        useless_char = dict.fromkeys(ord(c) for c in u"\xa0\n\t_ ")
        print(useless_char)

        for each in response('#mobanDiv > table tr').items():
            # 过滤无用内容
            span_list = list(each('tr > td > span').items())
            # print(len(span_list))
            if len(span_list) > 0:
                topic = span_list[0].text().split('、')[1]
                if topic not in useless_topics:
                    if topic in ['项目概况与招标范围', '采购说明', '采购内容及相关内容', '采购项目概况', '采购货物的名称']:
                        print(each.text())
                        # topics[topic] = each.html()
                    # elif topic == "联系方式":

                    else:
                        print("\n", topic)
                        len_p = each('p').length
                        len_div = each('div').length
                        print("\n p 元素: ", len_p)
                        print("\n div 元素: ", len_div)
                        infos = []
                        if len_p > 0:
                            for item in each('p').items():
                                text = item.text().translate(useless_char)
                                deadline = deadline_pattern.findall(text)
                                print(deadline)
                                if len(deadline) > 0:
                                    topics['投标截止时间'] = date_pattern.findall(text)[0]
                                else:
                                    infos.append(text)
                        else:
                            if len_div > 0:
                                for item in each('div').items():
                                    text = "".join(item.text().split()).replace("_", "")
                                    deadline = deadline_pattern.findall(text)
                                    print(deadline)
                                    if len(deadline) > 0:
                                        topics['投标截止时间'] = date_pattern.findall(text)[0]
                                    else:
                                        infos.append(text)

                        topics[topic] = infos
                        print(infos)

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
        print("\n noticeBean: ", topics)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QueryStringSuite))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
