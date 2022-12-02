import os
import time
import unittest
from HtmlTestRunner_PY.HtmlTestRunner import HTMLTestRunner
from HtmlTestRunner_PY import HTMLTestRunner_PY2
from HtmlTestRunner_PY import HTMLTestRunner_PY3


dir_path = os.getcwd()
case_path = os.path.abspath('testcase')
report_path = os.path.abspath('report')
one_test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
two_test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
three_test_case = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
now_time = time.strftime('%Y-%m-%d_%H.%M.%S')
file_name = now_time + '_result.html'


if __name__ == '__main__':
    """生成三种类型的测试报告"""

    """第一种测试报告"""
    one_file_path = report_path + '\\' + file_name
    fp = open(one_file_path, 'a', encoding='utf-8')
    one_run = HTMLTestRunner(output=report_path, stream=fp, report_title='测试报告', descriptions='用例执行情况')
    one_run.run(one_test_case)
    fp.close()

    """第二种测试报告"""
    two_file_path = report_path + '\\' + file_name
    with open(two_file_path, 'wb') as report:
        two_runner = HTMLTestRunner_PY2.HTMLTestRunner(stream=report, title='测试报告', description='用例执行情况')
        two_runner.run(two_test_case)

    """第三种测试报告"""
    three_file_path = report_path + '\\' + now_time + '_all_result.html'
    with open(three_file_path, 'wb') as pyreport:
        three_runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=pyreport, title='测试报告', description='用例执行情况')
        three_runner.run(three_test_case)



