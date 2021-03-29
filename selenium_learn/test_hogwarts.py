

from selenium import webdriver
from time import sleep

class TestHogwards():
    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_hogwords(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("君海游戏QA").click()
        self.driver.find_element_by_css_selector(".topic-22758 .title > a").click()



