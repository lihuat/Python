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

xiaotq = Xiaotianquan()
xiaotq.fly()
xiaotq.brak()
xiaotq.eat()

