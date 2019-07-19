import unittest
from testdemo.HTMLTestReportCN import HTMLTestRunner
from testdemo.config.smtplibTest import *
import logging

from testdemo.testUserLogin import TestUserLogin

logging.info("================================== 测试开始 ==================================")
#suite = unittest.defaultTestLoader.discover("./")
suite = unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal'))

with open("./report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

#send_email('report.html')  # 发送邮件
logging.info("================================== 测试结束 ==================================")