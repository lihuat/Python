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



class Cat(Animal):
    def catch(self):
        print('---捉老鼠----')





a = Animal()
a.eat()


wangcai = Dog()
wangcai.brak()
wangcai.sleep()

tom = Cat()
tom.catch()
tom.eat()