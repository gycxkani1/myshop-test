import unittest
from calc import Calc
class TestCalcMethod(unittest.TestCase):
    def setUp(self):
        self.filename="unittest_test/TestCase.log"
        self.file=open(self.filename,mode='a',encoding='utf-8')
        self.file.write("在每个测试用例执行之前都会调用"+"\n")
    def test_add(self):
        result = Calc(2, 3).add()
        try:
            self.assertEqual(result,4)
        except AssertionError as e:
            self.file.writelines(f"测试异常为{e}"+"\n")
            raise e
        else:
            self.file.writelines(f"测试通过" + "\n")

    def test_sub(self):
        result = Calc(2, 3).sub()
        try:
            self.assertEqual(result,-1)
        except AssertionError as e:
            self.file.writelines(f"测试异常为{e}"+"\n")
            raise e
        else:
            self.file.writelines(f"测试通过" + "\n")

    def tearDown(self):
        self.file.writelines("测试用例执行结束"+"\n")
        self.file.close()

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestCalcMethod('test_add'))
    # suite.addTest(TestCalcMethod('test_sub'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
