from faker import Faker
from tools.handle_db import mysql

class HandlePhone:
    def __init__(self):

        self.fk=Faker(locale="zh-CN")

    def __faker_phone(self):
        phone = self.fk.phone_number()
        print(phone)

    def __select_phone(self, phone):
        #查询数据库获取结果
        sql = 'SELECT * mobile_phone FROM member WHERE mobile_phone="{}"'.format(phone)
        result = mysql.get_db_all_value_list(sql=sql)
        return result

    def get_phone(self):
        while True:
            phone = self.__faker_phone()  #生成手机号

            result = self.__select_phone(phone=phone) #查询数据库获取结果

            if len(result) > 0:  #判断是否已注册
                #重新生成
                continue
            else:
                return phone     #返回未注册的手机号


cl = HandlePhone()
result = cl.get_phone()
print(result)