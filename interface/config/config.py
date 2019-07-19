import logging

logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a')# 追加模式


report_file = r"D:\腾讯课堂\interfaceAutomation\interface\data\test_user_data1.xlsx"
if __name__ == '__main__':
    logging.info("hello1") 