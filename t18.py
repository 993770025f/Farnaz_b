#مثال برای کلاس انتزاعی
#1
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Shape_1(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.height * self.width

shape1=Shape_1(3,4)
print(shape1.area())
#2
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("woof")

    def eat(self):
        print("Eating dog food ...")
class Cat(Animal):
    def sound(self):
        print("meow")
dog=Dog()
dog.sound()
cat=Cat()
cat.sound()
#3
class Pay(ABC):
    @abstractmethod
    def pay(self,amonth):
        pass
class Bank(Pay):
    def pay(self,amounth):
        
        print(f"paymen was made trough the bank:{amounth}")
bank=Bank()
bank.pay(500)