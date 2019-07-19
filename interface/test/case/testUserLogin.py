from interface.test.case.basecase import *
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a')

class TestUserLogin(BaseCase):

    def test_user_login_normal(self):
        case_data= self.get_case_data("test_01")
        self.send_request(case_data)

if __name__ == '__main__':   # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)