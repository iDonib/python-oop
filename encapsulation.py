class Car:
    def __init__(self, name, mileage) -> None:
        self.__name = name
        self.mileage = mileage
    
    def description(self):
        return f"The {self.__name} car gives mileage of {self.mileage}"

c1 = Car("bmw", 55)

print(c1.description())

# print(c1.__name) # cant access

print(c1._Car__name)