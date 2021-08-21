import pymysql
from conf.setting import mysql_info

class HandleDb:

    def __init__(self):
        self.conn =pymysql.connect(
            host=mysql_info["host"],
            port=mysql_info["port"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            db=mysql_info["db"],
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor)    #如果要返回字典(dict)表示的记录，就要设置cursor参数为pymysql.cursors.DictCursor类
        self.cur = self.conn.cursor()     #获取游标

    #查询并返回数据列表==》list
    def get_db_all_value_list(self, sql):
        """
        :param sql: 查询sql语句
        :return:  value  list
        execute(query,args=None) 函数作用：执行单条的sql语句，执行成功后返回受影响的行数
        """
        result_list = []
        self.cur.execute(sql)
        result = self.cur.fetchall()   #dict [{}]
        for val in result:
            for key, value in val.items():
                print(key, value)
                result_list.append(value)
        return result_list

    #获取查询的全部数据==>dict
    def get_db_all_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()

mysql = HandleDb()


# if __name__ == '__main__':
#     cl = HandleDb()
#     cl.get_db_all_value_list(sql='SELECT * mobile_phone FROM member WHERE mobile_phone=15778179492')
#     cl.close()
