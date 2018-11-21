class Dog:
    def __del__(self):
        print("英雄over！")#当对象最后执行


dog1 = Dog()
dog2 = dog1

del dog1#硬链接 一个类有两个对象
#del dog2
print("==============================")


#查看几个对象: import sys , sys.getrefcount()