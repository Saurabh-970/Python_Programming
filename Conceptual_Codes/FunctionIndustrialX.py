
def CheckEven(No):
    if((No % 2) == 0):
        return True
    else:
        return False

def main():
    value = 0
    Ret = False
    print("enter the no : ")
    value = int(input())

    Ret = CheckEven(value)
    
    if(Ret == True):
        print("It is even")
    else:
        print("It is odd")
 
if __name__ == "__main__":
        main()
