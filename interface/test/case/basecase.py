import unittest
import requests
import json
import sys
sys.path.append("../..")   # 统一将包的搜索路径提升到项目根目录下

from interface.lib.read_excel import *
from interface.lib.case_log import *
from interface.config import config

class BaseCase(unittest.TestCase):   # 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        data_file =config.report_file
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        print(case_data,url,args,expect_res,method,data_type)

        if method.upper() == 'GET':   # GET类型请求
            res = requests.get(url=url, params=json.loads(args))

        elif data_type.upper() == 'FORM':   # 表单格式请求
            res = requests.post(url=url, data=json.loads(args), headers=None)
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.text, expect_res)
        else:
            res = requests.post(url=url, data=json.loads(args), headers=None)   # JSON格式请求
#            log_case_info(case_name, url, args, expect_res,res.json())
            self.assertEqual(res.text,expect_res)



