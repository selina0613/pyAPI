"""


"""
import re
import ast
from conf.setting import replace_data
from tools.handle_phone import HandlePhone
from tools.handle_attribute import HandleAttribute
from tools.handle_db import mysql

class HandleReplace:

    def __init__(self):
        self.handle_phone = HandlePhone() #初始化手机号处理

    #设置类属性
    def __set__attribute(self, key, val):
        setattr(HandleAttribute, key, val)  #动态设置属性

    #执行aql语句，并将aql获取到的数据设置为类属性
    def __execute_sql_and_setattr(self, sql):
        #[{},{},{}]
        result = mysql.get_db_all_data(sql=sql)
        for dict_data in result:
            for key, val in dict_data.items():
                self.__set__attribute(key=key, val=val)


    #将需要替换的参数，从对应的渠道获取到对应的结果，设置为类属性
    def __set_attribute_data(self, key_list, replace_data, sql=None):
        """
        :param key_list: 拿到需要替换数据的名称，list
        :param replace_data:
        :param sql:
        :return:
        """
        #设置类属性
        #1.从脚本获取手机号，设置为类属性
        #2.从配置文件获取数据，设置为类属性
        #3.从数据库获取数据，设置为类属性
        #["SELECT monile_phone FROM member ORDER BY id DESC LIMIT 1"]
        if sql:    #True
            for i in ast.literal_eval(sql):
                #1.执行sql语句，获取执行结果
                #2.将拿到的结果设置为类属性
                self.__execute_sql_and_setattr(sql=i)


        #遍历key_list
        for key in key_list:
            # 如果key==phone 表示需要生成一个未注册过的手机号
            if key == "phone":
                phone = self.handle_phone.get_phone()  #获取到未注册的手机号
                #把未注册的手机号注册为类属性
                self.__set__attribute(key=key, val=phone)
            #如果key=mobile_phone,表示需要去setting.py文件去读取参数
            elif key in replace_data and key not in str(sql):
                #将配置文件读取的参数，设置为类属性
                self.__set__attribute(key=key, val=replace_data['mobile_phone'])
            else:
                print("该替换方式暂不支持")

    def __get_replace_keys(self, data):
        #拿到需要替换数据的名称
        re_str = r"#(\w.+?)#"
        key_list = re.findall(re_str, str(data))
        return key_list

    #参数替换
    def replace_data(self, data, sql=None):
        #
        if data:   #参数不为空时做参数替换，为空时不用替换
            #拿到需要替换数据的名称
            key_list = self.__get_replace_keys(data=data)
            if len(key_list) > 0:
                print("需要做数据替换")
                #1、根据数据的来源去获取数据 2、然后设置为类属性
                self.__set_attribute_data(key_list=key_list, replace_data=replace_data, sql=sql)
                #3、进行参数替换
                for key in key_list:
                    data.replace(f"#key#", str(getattr(HandleAttribute, key)))
                return ast.literal_eval(data)  #转为字典
            else:
                print("不需要做数据替换")
                return ast.literal_eval(data)
        else:
            print("data参数为空，不需要做参数替换")

