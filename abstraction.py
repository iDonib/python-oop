from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, name):
        self.name = name

    def description(self):
        print("class car")

    @abstractmethod
    def price(self, x):
            pass

class new(Car):
    def price(self, x):
        print(f"The {self.name} price is {x} lakhs")
        

c1 = new("BMW")

c1.description()
c1.price(25)