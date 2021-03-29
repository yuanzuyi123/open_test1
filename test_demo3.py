import allure

import pytest
from  selenium import  webdriver

import  time


def test_steps_demo(test_data1):

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com/")

    driver.find_element_by_id("kw").send_keys(test_data1)
    time.sleep(2)
    driver.find_element_by_id("su").click()

    time.sleep(2)


    driver.quit()

if __name__ == '__main__':
    test_steps_demo("波多野结衣")