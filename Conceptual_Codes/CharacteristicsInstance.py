import gc

class Demo:
    # Class Variable
    No1 = 10
    No2 = 20

    def __init__(self):
        #Instance variable
        self.A = 101
        self.B = 201
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")

print(Demo.No1)
print(Demo.No2)

obj = Demo()

print(obj.A)
print(obj.B)