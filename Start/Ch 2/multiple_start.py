# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "B"


class C(A, B):
    def __init__(self):
        super().__init__()
    def showProps(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)    # This will print A because of the order of inheritance in the class definition

c = C()
c.showProps()
print(C.__mro__)  # This will show the method resolution order for class C
