class Base(object):
    def test(self):
        print ('---Baes-----')




class A(Base):
    def test1(self):
        print ('---test1----')


class B(Base):
    def test2(self):
        print ('-----test2-----')




class C(A,B): #多继承
    pass



c = C()
c.test1()
c.test()