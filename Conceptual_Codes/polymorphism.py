class Parent:
    def __init__(self):
        print("Inside parent constructor")


    def fun(self):
        print("Inside fun method of parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
    

    def fun(self):
        super().fun()
        print("inside sun method of child")

cobj = Child()

cobj.fun()

