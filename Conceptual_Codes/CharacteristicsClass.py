import gc

class Demo:
    # Class Variable
    No1 = 10
    No2 = 20

    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")

print(Demo.No1)
print(Demo.No2)
