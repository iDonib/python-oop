class Stack:
    def __init__(self):
        # private member
        self.__stack = []
    

    def push(self, item):
        self.__stack.append(item)
    
    def pop(self):
        self.__stack.pop()

    def traverse(self):
        for item in self.__stack[::-1]:
            print("|",item,"|")
    
s1 = Stack()

s1.push(1)
s1.push(2)
s1.push(4)
s1.push(1)
s1.push(2)
s1.push(4)

s1.pop()
s1.pop()

s1.push(55)

s1.traverse()
