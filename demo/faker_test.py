"""
一、四要素
1.姓名
2.身份证信息
3.手机号
4.银行卡

二、个人信息
1.

三、文本类
1.字符串
2.词语
3.文章
4.随机数

四、时间类
1.当前时间
2.未来时间

五、高级用法
数据共享，通过seed保持数据一致
"""

from faker import Faker
fk=Faker(locale="zh-CN")
#根据百家姓随机拼接中文进行生成
name = fk.name()
print(name)

#生成身份证
card = fk.ssn()
print(card)

#生成手机号  #注意生成手机号时注意是否有生成短信验证码，有则需停掉
phone = fk.phone_number()
print(phone)

#生成银行卡
card_number = fk.credit_card_number()
print(card_number)

#生成地址   （带邮编）
addr = fk.address()
print(addr)

#生成公司名称
company = fk.company()
print(company)

#生成邮箱
email = fk.email()
print(email)

#生成岗位
job = fk.job()
print(job)

#国家  （跨境时用）
country = fk.country()
print(country)

#生成省份
province = fk.province()
print(province)

#生成城市
city = fk.city()
print(city)

#生成简单的个人信息
simple_profile = fk.simple_profile()
print(simple_profile)

#生成完整的个人信息
profile = fk.profile()
print(profile)


#生成英文字符串
pystring = fk.pystr()
print(pystring)

#生成词语
word = fk.word()
print(word)

#生成文章
text = fk.text()
print(text)


#生成随机数
random_num = fk.random_int(min=100,max=999)
print(random_num)

#年份 1970年-现在
year = fk.year()
print(year)

#月份
month = fk.month()
print(month)


#格式：年-月-日
date = fk.date()
print(date)

#格式：年-月-日
now = fk.date_this_year()
print(now)

#格式：年-月-日 时分秒
now_time = fk.date_time()
print(now_time)

#指定时间范围 "-1y"代表一年前，
now = fk.date_between(start_date="-1y", end_date="today")
print(now)


#未来时间
future1 = fk.future_date()
print(future1)
future2 = fk.future_datetime()
print(future2)

#批量生成不重复的数据
name_list=[fk.unique.name() for i in range(10)]
print(name_list)

numlist =[i for i in range(10)]
print(numlist)

#数据共享
