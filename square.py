class Square:
    def __init__(self, length) -> None:
        self.length = length

    def getArea(self):
        print("Area: ", self.length**2)
    
    def getPerimeter(self):
        return 4*self.length
    
s1 = Square(5)
s1.getArea()
print("peri: ",s1.getPerimeter())