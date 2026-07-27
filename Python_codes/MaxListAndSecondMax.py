def main():
    
    lst = list(map(int,input("Enter the number").split()))

    Max = lst[0]
    Second = float('-inf')
    
    if len(lst) < 2 :
        print("Maximum number is ",lst[0])
        print("Second number doest exist")
        return 
    for i in lst:

        if i > Max :
            Second = Max
            Max = i
        elif i > Second and i != Max :
            Second = i


    print("Max number is ",Max)
    print("Second largest is : ",Second)

if __name__ == "__main__":
    main()    