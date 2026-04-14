def CheckEven(No):
    return(No % 2 == 0)

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after fiter is : ",FData)


if __name__ == "__main__":
    main()