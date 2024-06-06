class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
    def moadel(self):
        return (sum(self.scores)/len(self.scores))
    def is_mashroot(self):
        average= self.moadel()
        if average <12:
            return True
        else:
            return False
    def __del__(self):
        print (f"student {self.name} deleted")
student1=Student("reza",[17,15,19,13])
print("Moadel:",student1.moadel())
print("Is-mashroot?",student1.is_mashroot())
del student1