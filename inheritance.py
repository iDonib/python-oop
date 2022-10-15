class A:
    def __init__(self):
        print("In A init")
    
    def feature1(self):
        print("feature 1 A working")
    
    def feature2(self):
        print("feature 2 is working")
    

class B:

    def __init__(self):
        print("In B init")
        # super().__init__()

    def feature1(self):
        print("feature 1 B is working")
    
    def feature4(self):
        print("feature 4 is working")


class C(A,B):
    def __init__(self):
        print("In C init")
        super().__init__()

    def feature5(self):
        print("feature 5 is working")

    def feat(self):
        super().feature2()


# a1 = A()
b1 = C()
b1.feature1()
b1.feat()
# c1 = C()

# a1.feature1()
# a1.feature2()

# b1.__init__()

# c1.feature1()