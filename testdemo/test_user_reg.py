import unittest
import requests
# from db import *
from testdemo.read_excel import *
import json

class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserReg")  # 读取TestUserReg工作簿的所有数据

    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))  # 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等
        name = data.get("name")  # 范冰冰
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