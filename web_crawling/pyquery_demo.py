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
            dicts.append(dict_n)
        print(dicts)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QueryStringSuite))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
