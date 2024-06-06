class Triangle():
    def __init__(self,a,b,c):
        self.z1=a
        self.z2=b
        self.z3=c
        if (a+b)>c and (a+c)>b and (b+c)>a:
            print ("triangle is true")
        else:
            print("triangle is false")
    def perim(self):
        return self.z1+self.z2+self.z3
    def area(self):
        s=(self.z1+self.z2+self.z3)/2
        return (s*(s-self.z1)*(s-self.z2)*(s-self.z3)**(0/5))
    def __del__(self):
        print("triangle deleted")
t=Triangle(5,7,6)
print(t.perim())
print(t.area())
del t
