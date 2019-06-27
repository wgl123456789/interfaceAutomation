import unittest
import requests
# from db import *
from testdemo.read_excel import *
import json
from interface.test.case.basecase import *

class TestUserReg(BaseCase):

    def test_user_reg_normal(self):
        case_data = self.get_case_data("test_user_reg_normal")
        if not case_data:
            print("用例数据不存在")
        else:
            self.send_request(case_data)
        #
        # # 环境检查
        # if check_user(name):
        #     del_user(name)
        # # 发送请求
        # res = requests.post(url=url, json=data)  # 用data=data 传字符串也可以
        # # 响应断言（整体断言）
        # self.assertDictEqual(res.json(), expect_res)
        # # 数据库断言
        # self.assertTrue(check_user(name))
        # # 环境清理（由于注册接口向数据库写入了用户信息）
        # del_user(name)

if __name__ == '__main__':    # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)