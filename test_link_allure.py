import pytest
import  allure


@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
    print ("这是一条链接")
    pass
a = 'http://www.baidu.com'
@allure.testcase(a,'这是一个测试用例')
def test_with_testcase_link():
    print ("这是一个测试用例")
    pass


@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_severity_trivial():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_severity_normal():
    pass
@allure.severity(allure.severity_level.CRITICAL)
def test_with_severity_critical():
    pass
