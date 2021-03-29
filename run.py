import unittest
from utill.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':


    # test_dir = './test_case'
    # discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)

    report_title = '用例执行报告 我的标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'

    testsuite = unittest.TestSuite()
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
