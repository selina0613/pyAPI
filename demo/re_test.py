"""
一、re模块
1.作用：根据规则去匹配字符串
2.表达式：匹配字符串的规则
3.常用方法
    findall():匹配所有的字符串。把匹配的结果作为一个列表返回
    match():匹配字符串的开始位置，如果开始位置没有就返回None
    search():在字符串中搜索，返回搜索到的第一个
    finditer():匹配所有的字符串，返回迭代器
二.正则匹配的分类
1.匹配单字符：每次只匹配一个字符

元字符
.   匹配任意字符(除了\n以外)
[]
\d        匹配数字0-9
\D        匹配非数字
\s(小写)   匹配空白（tab 空格）
\S(大写)
\w(小写)   匹配非特殊字符（字符，数字，汉字，_）
\W(大写)   匹配特殊字符

2.多字符匹配
贪婪模式：尽可能多次匹配
非贪婪模式：尽可能少的匹配
元字符
*：匹配前一个字符出现0次，或无限次【贪婪模式】 0-无限次
+：匹配前一个字符出现1次或者无限次，【贪婪模式】 1-无限次
?:匹配前一个字符出现0次或1次【非贪婪模式】 http(s)
{n}:匹配前一个字符连续出现n次
{n,m}:匹配前一个字符连续出现n-m次

3.逻辑运算
或 |
与

4.边界值
^:匹配字符串开始位置
$:匹配字符串结束位置

5.分组匹配
():只匹配括号里的
"""

import re

#自动化使用这个表达式提取替换的参数
res = "#(\w.+?)#"   #正则表达式
s = "{'mobile_phone':'#mobile_phone#','pwd':'Aa123456'}"   #字符串
result = re.findall(res, s)
print(result)

# #()
# res = "#(mobile_phone)#"   #正则表达式
# s = "{'mobile_phone':'#mobile_phone#','pwd':'Aa123456'}"   #字符串
# result = re.findall(res, s)
# print(result)


#$
# res = "nw$"   #正则表达式
# s = "hhelhttpsslo4-45 py@3$4t%nw"   #字符串
# result = re.findall(res, s)
# print(result)

# #^
# res = "^hhe"   #正则表达式
# s = "hhelhttpsslo4-45 py@3$4t%nw_"   #字符串
# result = re.findall(res, s)
# print(result)

#| 或
# res = "ll|th"   #正则表达式
# s = "hhelhttpssllo4-45 pyth@3$4t%nw_"   #字符串
# result = re.findall(res, s)
# print(result)


#{n，m}
# res = "https{1,4}"   #正则表达式
# s = "hhelhttpsslo4-45 py@3$4t%nw_"   #字符串
# result = re.findall(res, s)
# print(result)


#{n}
# res = "https{2}"   #正则表达式
# s = "hhelhttpsslo4-45 py@3$4t%nw_"   #字符串
# result = re.findall(res, s)
# print(result)


#?
# res = "https?"   #正则表达式
# s = "hhelhttplo4-45 py@3$4t%nw_"   #字符串
# result = re.findall(res, s)
# print(result)


#+
# res = "h+"   #正则表达式
# s = "hhello4-45 py@3$4t%honw_"   #字符串
# result = re.findall(res, s)
# print(result)


# *
# res = "h*"   #正则表达式
# s = "hhello4-45 py@3$4t%honw_"   #字符串
# result = re.findall(res, s)
# print(result)


#\W大写 匹配特殊字符
# res = "\W"   #正则表达式
# s = "hello4-45 py@3$4t%honw_"   #字符串
# result = re.findall(res, s)
# print(result)

#\w小写 匹配非特殊字符
# res = "\w"   #正则表达式
# s = "hello445 py34thonw_"   #字符串
# result = re.findall(res, s)
# print(result)

#\S 匹配非空白
# res = "\S"   #正则表达式
# s = "hello445 py34thon"   #字符串
# result = re.findall(res, s)
# print(result)


#\s 匹配空白（tab健，空格）
# res = "\s"   #正则表达式
# s = "hello445 py34thon"   #字符串
# result = re.findall(res, s)
# print(result)


# #\D 匹配字符串中的非数字字符 ，空格也会被打印出来
# res = "\D"   #正则表达式
# s = "hello445 py34thon"   #字符串
# result = re.findall(res, s)
# print(result)



#\d 匹配字符串中的数字
# res = "\d"   #正则表达式
# s = "hello99 py34thon"   #字符串
# result = re.findall(res, s)
# print(result)


# #[]匹配[]中的任意一个字符
# res = "[hn]"   #正则表达式
# s = "hello python"   #字符串
# result = re.findall(res, s)
# print(result)



#.匹配任意字符（\n除外）
# res = "h."   #正则表达式
# s = "hello python"   #字符串
# result = re.findall(res, s)
# print(result)