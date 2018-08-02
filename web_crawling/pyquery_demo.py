import os
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
        url = 'https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=478023'
        # 478023
        response = pq(url, encoding="utf-8")
        # print("\n", response('#mobanDiv tr').text())
        # 无用内容 #mobanDiv > .tab2 tr > td > span, #mobanDiv > .tab2 #titDiv
        useless_topics = ['免责声明', '发布公告的媒介', '电子采购应答规则']
        for each in response('#mobanDiv tr').items():
            # 过滤无用内容
            span = each('td > span').text()
            if span:
                topic = span.split('、')[1]
                if topic not in useless_topics:
                    print("\n\n", topic)
                    dict_n = {}
                    # dict_n["采购人"] = tds[0].text()
                    # dict_n["type"] = tds[1].text()
                    # dict_n["title"] = tds[2].text()
                    # dict_n["date"] = tds[3].text()
                    # dict_n["url"] = "https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=" + notice_id
                    if topic == "联系方式":
                        contact_info = each('#ggdiv3')
                        print("span: ", each('#ggdiv3 span').text())
                        print("MsoNormal: ", each('#ggdiv3 .MsoNormal').text())


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QueryStringSuite))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())