#overloading
class X:
    def test(self,k=10,p=10):
        if k!=10 and p!=10:
            return k*p
        elif k!=10 and p==10:
            return 3.14*k*k
        else:
            return 100
x=X()
print(x.test(5,10))
print(x.test(7,8))
print(x.test(10,9))
