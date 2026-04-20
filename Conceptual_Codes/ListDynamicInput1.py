def main():
    print("Emter the s of elements : ")
    Size = int(input())

    Data = list()
    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)
    

if __name__== "__main__":
   main()