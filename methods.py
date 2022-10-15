class Student:
    school = "NCIT"

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school
        
    @staticmethod
    def getInfo():
        print ("This is student class ...")

s1 = Student(99, 56, 85)
s2 = Student(87, 88, 85)

print(Student.getSchool())

print(s2.average())

Student.getInfo()