import unittest
from common.requests_api import auto_request
from common.base_api import SQL
sql = SQL().select_all(table_name='testcase_ndxs')

"""可以尝试在此文件编写测试用例，对应的数据在数据库testcase_ndxs表内"""


class TestNDXS(unittest.TestCase):

    def setUp(self):
        self.a = 1
        self.b = 2
        self.c = [1, 2, 3]

    def tearDown(self):
        pass

    def test_ZCJK(self):
        '''a * b = 2 这个用例应该成功'''
        print('a * b = 2')
        self.assertEqual(self.a * self.b, 2)

    def test_DL(self):
        """ a + b = 3 这个用例应该通过"""
        self.assertEqual(self.a + self.b, 3, msg="我是测试断言成功的")

    def test_TJJP(self):
        """ a / c = 1 这是个有subTest的用例"""
        for i in self.c:
            with self.subTest(i=i):
                print('a / c = 1')
                self.assertEqual(self.a / i, 1)

    def test_CJJK(self):
        """ 除零异常 """
        print('1/0')
        self.assertEqual(self.a / 0, 1)

    def test_CKZJJL(self):
        """用例3，plus，此用例执行出错，因为c未定义"""
        self.assertEqual(self.a * self.b, c)

    def test_HQSYJPXX(self):
        """这是条失败的用例"""
        unittest.TestCase().fail()


if __name__ == '__main__':
    unittest.main()
