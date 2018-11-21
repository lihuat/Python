class Animal:
    def eat(self):
        print('eat')
    def drink(self):
        print('drink')
    def sleep(self):
        print('sleep')
    def run(self):
        print('run')



class Dog(Animal):
    def brak(self):
        print("旺旺叫")



class Xiaotianquan(Dog):
    def fly(self):
        print("--飞---")

    def brak(self):
        print('----狂叫!-----')
        # 第一种方法 调用被重写的父类的方法
        #Dog.brak(self) #調用的是父的
        #第二种  
        super().brak()



xiaotq = Xiaotianquan()
#xiaotq.fly()
xiaotq.brak()
#xiaotq.eat()

