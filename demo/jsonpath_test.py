"""
一、jsonpath
1.安装jsonpath
    pip install jsonpath

2.作用
    提取json数据

3.

"""
class_info = {"class_one": {
    "students": [
        {"name": "张一",
         "sex": "男",
         "age": 18,
         "height": 170.5
         },
        {"name": "张二",
         "sex": "女",
         "age": 20,
         "height": 160.5
         },
        {"name": "张三",
         "sex": "男",
         "age": 18,
         "height": 170.5
         },
    ],
    "teacher": {
        "name": "李小二",
        "sex": "男",
        "age": 30,
        "height": 185.5,
        "teacher": "递归搜索测试"
    }
}
}

import jsonpath
"""$:根元素"""
#获取根元素下所有数据，2种写法一样
#.的作用等同于[]表示子元素
result = jsonpath.jsonpath(class_info, '$.*')
result1 = jsonpath.jsonpath(class_info, "$[*]")
print(result)
print(result1)

