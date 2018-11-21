class Base(object):
    def test(self):
        print ('---Baes-----')




class A(Base):
    def test(self):
        print ('---test1----')


class B(Base):
    def test(self):
        print ('-----test2-----')


class C(A,B): #多继承
    #def test(self):
    #   print ('-----test3------')
    pass

c = C()
c.test()


print (C.__mro__)# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
# 决定调用一个方法的时候搜索的顺序，如果在某个类中找到方法就停止搜索 ， C3算法决定的


