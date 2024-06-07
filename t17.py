class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def A(self,attribute,value):
        if attribute=="age" and value<0:
            print("age cannot be negative")
            setattr(self,attribute,value)
    def get(self,attribute):
        return (getattr(self,attribute,"None"))

    def print(self):
        print(f"hello my name is {self.name} and i am {self.age} years old")

person1=Person("mohammad",20)
setattr(person1,"age",30)
print(person1.age)
person1.print()
person1.A("age",9)
person1.A("age",-20)
print(person1.get("age"))
