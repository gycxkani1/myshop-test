import unittest
import HTMLTestRunnerNew
from calc import Calc
from calc_testcase import TestCalcMethod
import calc_testsuits as suit1

with open('unittest_test/report.html','wb') as fb:
    test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb,verbosity=2,title='测试报告',description='... ',tester='张三')
    test_run.run(suit1.suit)


