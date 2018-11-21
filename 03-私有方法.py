class Dog:
    def __test1(self):#私有方法
        print('-------1----------')
    #共有方法
    def test2(self):
        print('-------2----------')


    def __send_msg(self):
        print('------正在发送短信--------')
    def send_msg(self,new_money):
        if new_money >=0.01:
            self.__send_msg()
        else:
            print('余额不足，清充值')


dog = Dog()
#dog.__test1()
dog.test2()
dog.send_msg(0)





