#وراثت چند گانه زمانیست که یک کلاس از بیش از یک کلاس والد ارث میبرد.زمانی مفیداست که یک کلاس دارای 
#ویژگی ها ومتد هایی از چندین کلاس باشد
class Vehicle():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def  print(self):
        print(f"Brand:{self.brand},Model:{self.model}")
class FourWheeler():
    def fourwheeler(self):
        print('this vehicle has four wheels')

class TowWheeler():
    def towwheeler(self):
        print("this vehicle has tow wheels")
class Car(Vehicle,FourWheeler):
    pass
v1=Vehicle("Toyota","corolla")
v1.print()
car=Car("Honda","CB500")
car.print()

#وراثت چندسطحی زمانیست که یک کلاس از یک کلاس مشتق شده حاصل میشود.زمانی مفید است که یک کلاس دارای ویژگی 
#ها ومتدهایی ازیک کلاس والد و ی کلاس فرزند باشند
class SuperClass:
    def super_method(self):
        print("super class method ")

class DrivedClass2(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method")
class DerivedClass2(DrivedClass2):
    def derived2_method(self):
        print("Derived class 2 method")
d2=DerivedClass2()
d2.super_method()
d2.derived1_method()
d2.derived2_method()


