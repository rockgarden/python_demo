import unittest

from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# https://blog.csdn.net/sunyao_123/article/details/76942809
class FuzzywuzzySuite(unittest.TestCase):

    def test_simple(self):
        print(fuzz.ratio("项目说明", "采购内容及相关内容"))
        print(fuzz.partial_ratio("采购说明", "采购内容及相关内容"))
        choices = ['项目概况与招标范围', '采购说明', '采购内容及相关内容', '采购项目概况']
        print(process.extract("采购说明", choices, limit=2))
        print(process.extract("项目概况", choices, limit=3))
        print(process.extractOne("项目说明", choices))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FuzzywuzzySuite))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
