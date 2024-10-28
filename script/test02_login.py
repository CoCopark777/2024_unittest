# 登录成功
import unittest

# 导包
import requests

class TestImage(unittest.TestCase):

    # 前置处理
    def setUp(self):
        # 实例化接口对象
        pass

    # 后置处理
    def tearDown(self):
        pass

    def test01_login_success(self):
        # 发送请求
        url = "http://kdtx-test.itheima.net/api/login"
        header_data = {
            "Content-Type": "application/json"
        }
        login_data = {
            "username":"admin",
            "password":"HM_2023_test",
            "code":2,
            "uuid":"9d4408f3f9c04f0986de8a0e8d1ed1ef"
        }
        response = requests.post(url=url, headers=header_data, json=login_data)
        # 查看响应
        print(response.status_code)
        print(response.text)

