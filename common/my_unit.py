import unittest

class My_Unit(unittest.TestCase):

    def setUp(self) -> None:
        print("进行登录操作需要")

    def tearDown(self) -> None:
        print("退出登录操作")

    @classmethod
    def setUpClass(cls) -> None:
        print("数据库链接之类的操作")

    @classmethod
    def tearDownClass(cls) -> None:
        print("断开数据库链接")
