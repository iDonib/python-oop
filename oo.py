class Orders:
    def __init__(self, items) -> None:
        self.items = items
    
    def __add__(self, other):
        return self.items + other.items
    
    def __gt__(self,other):
        return len(self.items) > len(other.items)
    
o1 = Orders([1,2,3,4])
o2 = Orders([10,20,30])

print(o1+o2)
print(o1>o1)
print(dir(o1))

print(o1.__class__.__name__)