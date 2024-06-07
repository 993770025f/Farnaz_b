#super():ازاین تابع برای اشاره به کلاس والد استفاده میشود واین اجازه را میدهد که متدهاوپراپرتی های
#که در کلاس والد تعریف شده اند رادر کلاس فرزند فراخوانی کرده وعملکرد به ارث رسیده از کلاس والدرا شخصی سازی کرده ویا گسترش دهید

class Parent:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Hello my name is{self.name}")
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def introduct(self):
        super().greet()
        print(f"i am {self.age} years old")
child=Child("Ahmad",30)
child.introduct()