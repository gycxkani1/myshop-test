import unittest
from calc import Calc
from calc_testcase import TestCalcMethod
# 创建测试套件
suit=unittest.TestSuite()
# 添加测试用例到测试套件
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCalcMethod))



