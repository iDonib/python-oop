
class Student:

    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def showInfo(self):
        print(self.name, self.rollno)
        self.lap.showInfo()


    class Laptop:

        def __init__(self) -> None:
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 8

        def showInfo(self):
            print(self.brand, self.cpu, self.ram)
        
s1 = Student("Binod", 1)
s2 = Student("Arnav", 25)

s1.showInfo()
print(s1.lap.brand)

lap1 = Student.Laptop()
# lap1.showInfo()