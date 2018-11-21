class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("----test1-----")

    def __test2(self):
        print ("------test2-----")

    def test3(self):
        print (self.__num2) #可以调用
        self.__test2()

class B(A): #私有方法和私有的数据不会被继承
    def test4(self):
        self.__test2()
        print (self.__num2) #子类中调用父类中的私有方法和属性，不让调用的



b = B()
b.test3()
b.test4()