"""
封装unittest峰装实现
"""
# 1.导包
import json
import unittest
import requests

import app
from api.login_api import Login
# 参数化步骤1：导包----------------------
from parameterized import parameterized


# 参数化步骤2：解析----------------------
def read_json_file():
    # 1.创建空列表接受数据
    data = []
    # 2.解析文件流，将数据追加进列表
    with open(app.PRO_PATH + "/data/log_data.json", "r", encoding="utf-8") as f:
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            # 组织成元组
            ele = (mobile, password, success, code, message)
            # 追加进列表
            data.append(ele)
    # 3.返回列表
    return data


# 2.创建测试类（继承unittest.TestCase）：


class TestLogin(unittest.TestCase):
    # 初始化函数
    def setUp(self) -> None:
        # 初始化session对象
        self.session = requests.Session()
        # 初始化api对象
        self.login_obj = Login()

    # 资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 核心：测试函数 - 登录
    # 参数化
    # 参数化步骤3：调用----------------------
    @parameterized.expand(read_json_file())
    def test_login(self, mobile, password, success, code, message):
        print("-" * 100)
        print("测试的数据：", mobile, password, success, code, message)

        # 调用请求业务
        response = self.login_obj.login(self.session, mobile, password)
        # 实现断言
        print(response.json())
        result = response.json()
        self.assertEqual(success,result.get("success"))
        self.assertEqual(code,result.get("code"))
        self.assertIn(message,result.get("message"))

    #编写登录成功的测试函数
    def test_login_success(self):
        # 1.直接通过提交正向数据发送请求业务
        reponse = self.login_obj.login(self.session,"13800000002","123456")
        # 2.断言业务
        print("登录成功的结果：",reponse.json())
        self.assertEqual(True,reponse.json().get("success"))
        self.assertEqual(10000,reponse.json().get("code"))
        self.assertIn("操作成功",reponse.json().get("message"))
        # 提取token
        token = reponse.json().get("data")
        print("登录后响应的token:", token)
        # 预期允许其他文件调用token，可以扩大token
        app.TOKEN = token