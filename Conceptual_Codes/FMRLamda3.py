from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is : ",Data)

    FData = list(filter((lambda No : (No % 2 == 0)),Data))     #accepts bool
    print("Data after fiter is : ",FData)

    MData = list(map((lambda No : No + 1),FData)) 
    print("Data after mapping  is : ",MData)

    RData = reduce((lambda A,B : A+B),MData)
    print("Data after reduce is : ",RData)
    


if __name__ == "__main__":
    main()