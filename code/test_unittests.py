import unittest

from name_function import get_formatted_name


# test_ 开头的方法都将自动运行
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# 在 Unittests 框架下执行 main
# 启动测试集合, 运行集合方法
if __name__ == '__main__':
    unittest.main()
