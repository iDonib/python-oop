class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        print("In show B")
    




a1 = B()
a1.show()

