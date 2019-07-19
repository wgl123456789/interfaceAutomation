import sys
#sys.path.append(r"D:\腾讯课堂\interfaceAutomation\interface")
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
from interface.lib.HTMLTestReportCN import HTMLTestRunner
import logging

from interface.test.case.testUserLogin import TestUserLogin
from testdemo.test_user_reg import TestUserReg
from interface.lib.smtplibTest import *
logging.info("================================== 测试开始 ==================================")
#suite = unittest.defaultTestLoader.discover("./")
suite = unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal'))
#suite.addTest(TestUserReg('test_user_reg_normal'))

with open(r"D:\腾讯课堂\interfaceAutomation\interface\report\report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="汪队").run(suite)
send_email(r'D:\腾讯课堂\interfaceAutomation\interface\report\report.html')  # 发送邮件
logging.info("================================== 测试结束 ==================================")