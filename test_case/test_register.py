"""注册接口"""
import unittest
import requests

from tools.handle_excel import HangleExcel
from tools.handle_path import case_data_dir
from conf.setting import register_case_data
from ddt import ddt, data
from tools.handle_db import mysql
import ast
from tools.handle_replace import HandleReplace

case_list = HangleExcel(file_name=case_data_dir, sheet_name=register_case_data["sheet_name"]).get_test_case()

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.headers = {"X-Lemonban-Media-Type": "lemonban.v2","Content-Type":"application/json"}
        cls.replace = HandleReplace()

    @classmethod
    def tearDownClass(cls) -> None:
        mysql.close()

    @data(*case_list)
    def test_register(self, case):
        try:
            #1.请求头
            headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}

            #2.参数替换 造数据faker 正则re，jsonpath
            new_data = self.replace.replace_data(data=case["data"], sql=case["replace_sql"])

            #3发送requests请求
            res = requests.post(url=case['url'], headers=headers, json=ast.literal_eval(case['data']))
            print(res.json())

            #4.接口断言   (返回值断言)
            #{"code":0, "msg": "OK"}
            actual_data = {"code": res.json()["code"], "msg": res.json()["msg"]}
            expect_data = case["expected_data"]
            self.assertEqual(expect_data, actual_data)

            #5.数据库断言


        except:
            print("执行报错了")




# if __name__ == '__main__':
