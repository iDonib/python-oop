class VSCode:

    def execute(self):
        print("Compiling...")
        print("Running...")


class Laptop:

    def code(self, ide):
        ide.execute()
    
class PyCharm:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling...")
        print("Running...")


ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)