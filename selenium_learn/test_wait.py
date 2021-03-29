
from selenium import  webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://home.testing-studio.com/")
        self.driver.implicitly_wait(3)

    def  test_wait(self):

        self.driver.find_element(By.XPATH,'//title')
        sleep(3)