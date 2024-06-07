class Vehicle:
    def __init__(self,fare):
        self.fare=fare

    def __add__(self,other):
        return self.fare + other.fare
bus=Vehicle(100)
car=Vehicle(200)
print(bus+car)
