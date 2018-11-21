class Dog(object):
    def print_self(self):
        print ('大家好，我是xx，希望以后大家多多关照')

class Xiaotq(Dog):
    def print_self(self):
        print ('hello everybody,我是你们的老大')


def introduce(temp): #都是引用
    temp.print_self()


dog1 = Dog()
introduce(dog1)

dog2 = Xiaotq()
introduce(dog2)