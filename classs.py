from distutils import dep_util


class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept

        # private variable
        self.__salary = salary

    def show_details(self):
        print("name: ", self.name)
        print("role: ", self.role)
        print("dept: ", self.dept)
        print("salary: ", self.__salary)

class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Teacher", "science", 250000)

    def show_details(self):
        print("name: ",self.name)
        print("salary: ", self.__salary)

t1 = Teacher("Binod", 25)
t1.show_details()
# print(t1.__salary)


