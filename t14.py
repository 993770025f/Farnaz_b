class Car:
    def __init__(self,name,w):
        self.name=name
        self.w=w
    def __lt__(self,other):
        return self.w < other.w
car1=Car("k",100)
car2=Car("p",200)
print(car1<car2)


