from faker import Faker


class Test:
    def __init__(self):
        self.fk = Faker(locale="zh-CN")

    def test01(self):
        Faker.seed(1111)
        print(self.fk.name())

    def test02(self):
        Faker.seed(1111)
        print(self.fk.name())

if __name__ == '__main__':
    c1=Test()
    c1.test01()
    c1.test02()


