from functools import reduce

def CheckEven(No):
    return(No % 2 == 0)

def Increment(No):
    return No + 1

def Add(A,B):
    return A+B


def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is : ",Data)

    FData = list(filter(CheckEven,Data))     #accepts bool
    print("Data after fiter is : ",FData)

    MData = list(map(Increment,FData)) 
    print("Data after mapping  is : ",MData)

    RData = reduce(Add,MData)
    print("Data after reduce is : ",RData)
    


if __name__ == "__main__":
    main()