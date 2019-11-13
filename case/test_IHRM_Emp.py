"""
测试员工模块的增删改查实现
"""
# 1.导包
import logging
import unittest
import requests

# 2.创建测试类
import app
from api.EmpAPI import EmpCRUD


class Test_Emp(unittest.TestCase):
    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 4.资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5.测试函数1：增
    # 直接执行失败的原因：
    # 原因1：先执行登录操作  2.还需要提交银行卡（token）
    def test_add(self):
        logging.info("增加员工信息")
        # 1.请求业务
        response = self.emp_obj.add(self.session, username="molly116", mobile="15711261116")

        # 2.断言业务
        print("员工新增响应结果：", response.json())
        # 员工新增响应结果： {'success': True, 'code': 10000, 'message': '操作成功！', 'data': {'id': '1193819090510499840'}}
        # 提取ID
        id = response.json().get("data").get("id")
        app.USER_ID = id
        # print("新增员工的ID：",id)
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))

    # 6.测试函数2：改
    def test_update(self):
        logging.warning("修改员工信息")
        # 1.请求业务
        response = self.emp_obj.update(self.session, app.USER_ID, "molly114")
        # 2.断言业务
        print("修改后的员工信息：", response.json())
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))

    # 7.测试函数3：查
    def test_get(self):
        logging.warning("查询员工信息")
        # 1.请求业务
        response = self.emp_obj.get(self.session, app.USER_ID)
        # 2.断言业务
        print("-" * 100)
        print("查询到的员工信息：", response.json())
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))

    # 8.测试函数4：删
    def test_delete(self):
        logging.warning("删除员工信息")
        # 1.请求业务
        response = self.emp_obj.delete(self.session, app.USER_ID)
        # 2.断言业务
        print("-" * 100)
        print("删除的员工信息：", response.json())
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))