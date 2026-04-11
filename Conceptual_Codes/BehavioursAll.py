class Demo:
    #class variable
    No = 10

    def __init__(self,A,B):
        #instance variable
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside instance method fun",self.Value1 , self.Value2)

    @classmethod                                     #decorator
    def sun(cls):
        print("Inside class method sun : ",cls.No)

    @staticmethod
    def gun():
        print("Inside static method gun",Demo.No)

Demo.sun()
print("Class variable No : ",Demo.No)

obj = Demo(11,21)

obj.fun()

print("Instance variable : ",obj.Value1,obj.Value2)

Demo.gun()


#decorators in python: giving special meaning to something
#if it is an instance method then no need of decorator 
# @ symbol is used as a decorator and for class methid its compulsory
# static python recommends to write a decorator its readable and understandable
#static methid can access class variabke but we need to use class name to access it