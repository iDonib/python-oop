import math
class Cone:
    def __init__(self, base, axis):
        self.base = base
        self.axis = axis
        
    def getVolume(self):
        vol = math.pi * (self.base**2) * self.axis / 3
        return vol
    
    def getTSA(self):
        tsa = math.pi * base * (base  + math.sqrt(base**2 + axis**2))
        return tsa

base = float(input("Enter radius of base: "))
axis = float(input("Enter axis: "))

con = Cone(base, axis)

print("volume= ", con.getVolume())
print("TSA= ", con.getTSA())

