
class Circle():
    
    def __init__(self,r):
        self.r=r
        print("Circle created")
    def prim(self):
        return 2*3.14*self.r
    def area(self):
        return 3.14*self.r*self.r
    def __del__(self):
        print("circle deleted")
c=Circle(10)
print(c.area())
print(c.prim())
del c
     
