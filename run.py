import unittest
from BSTestRunner import BSTestRunner
import time

test_dir = './test_case'
report_dir = './reports'


def all_case():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    return discover


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + '.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='接口自动化测试报告', description='社交圈接口报告')
    runner.run(all_case())
