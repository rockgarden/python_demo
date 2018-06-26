# https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# Safari的WebDriver支持默认关闭，所以要配置Safari
# Safari的WebDriver支持默认关闭。要启用WebDriver支持，请执行以下操作：
#
# 确保“开发”菜单可用。可以通过打开Safari首选项（菜单栏中的Safari>偏好设置）打开，然后打开“ 高级”选项卡，并确保选中菜单栏中的“ 显示开发”菜单复选框。
# 在开发菜单中启用远程自动化。这通过菜单栏中的Develop> Allow Remote Automation来切换。
# 授权 safaridriver 启动 webdriverd 托管本地Web服务器的服务。要允许此操作，请/usr/bin/safaridriver手动运行一次并完成身份验证提示。
# 直接前往该目录，双击执行，可重置 safaridriver 如果用命令行之行会报错（报错原因待研究）

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class WebKitFeatureStatusTest(unittest.TestCase):

    def test_setup_module(module):
        WebKitFeatureStatusTest.driver = webdriver.Safari()

    def test_feature_status_page_search(self):

        self.driver.get("https://webkit.org/status/")

        # Enter "CSS" into the search box.
        search_box = self.driver.find_element_by_id("search")
        search_box.send_keys("CSS")
        value = search_box.get_attribute("value")
        self.assertTrue(len(value) > 0)
        search_box.submit()

        # Count the results.
        feature_count = self.shown_feature_count()
        self.assertTrue(len(feature_count) > 0)

    def test_feature_status_page_filters(self):
        self.driver.get("https://webkit.org/status/")

        filters = self.driver.find_element(By.CSS_SELECTOR, "ul#status-filters li input[type=checkbox]")
        self.assertTrue(len(filters) is 7)

        # Make sure every filter is turned off.
        for checked_filter in filter(lambda f: f.is_selected(), filters):
            checked_filter.click()

        # Count up the number of items shown when each filter is checked.
        unfiltered_count = self.shown_feature_count()

        running_count = 0
        for filt in filters:
            filt.click()
        self.assertTrue(filt.is_selected())
        running_count += self.shown_feature_count()
        filt.click()

        self.assertTrue(running_count is unfiltered_count)

    def test_shown_feature_count(self):
        return len(self.driver.execute_script("return document.querySelectorAll('li.feature:not(.is-hidden)')"))

    def test_teardown_module(module):
        WebKitFeatureStatusTest.driver.quit()


if __name__ == '__main__':
    unittest.main()
