
import gc

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print(" Inside destructor")

#allocate
obj = Demo()

#use

#deallocate
del obj

gc.collect()
print("emd of apploication\n")