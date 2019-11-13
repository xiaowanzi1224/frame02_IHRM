"""
测试套件:
    按照需要组合被执行的测试函数

    补充说明：
    关于测试套件的组织，接口业务测试中，需要保证测试套件中的执行顺序：
    合法实现：suite.addTest(类名（"函数名")，逐一实现
    非法实现：suite.addTest(unittest.makeSuite(类名))
"""

# 1.导包
import unittest

import app
from case.test_IHRM_Emp import Test_Emp
from case.test_IHRM_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

# 2.实例化套件对象，组织被执行的测试函数

suite = unittest.TestSuite()
suite.addTest(TestLogin("test_login_success"))  # 组织登录成功的测试函数
suite.addTest(Test_Emp("test_add"))  # 组织员工新增的测试函数
suite.addTest(Test_Emp("test_update"))  # 组织员工修改的测试函数
suite.addTest(Test_Emp("test_get"))  # 组织员工查询的测试函数
suite.addTest(Test_Emp("test_delete")) # 组织员工删除的测试函数
# 3.执行套件，生成测试报告
# runner = unittest.TextTestRunner()
# runner.run(suite)

with open(app.PRO_PATH + "/report/report.html","wb") as f:
    # 创建 HTMLTestRunner 对象
    runner = HTMLTestRunner(f, title="人力资源管理系统测试报告", description="测试员工模块的增删改查相关接口")
    # 执行
    runner.run(suite)