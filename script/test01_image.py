import unittest
# 获取图片验证码

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

    def test01_get_image(self):
        # 发送请求
        response = requests.get(url="http://kdtx-test.itheima.net/api/captchaImage")
        # 查看响应
        print(response.status_code)
        print(response.text)