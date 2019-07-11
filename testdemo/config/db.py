import pymysql
from testdemo.config.config import *

def get_db_conn():
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='test',
                           passwd='123456',
                           db='api_test',
                           charset='utf8')  # 如果查询有中文，需要指定测试集编码

    return conn

# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)    # 输出执行的sql
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    logging.debug(result)  # 输出查询结果
    cur.close()
    conn.close()
    return result

# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)  # 输出执行的sql
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))  # 输出错误信息
    finally:
        cur.close()
        conn.close()