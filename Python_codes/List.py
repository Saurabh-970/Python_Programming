# This code performs summation of all the elements in the list.

def main():
    pass

    print("Enter the list")
    lst = list(map(int,input().split()))

    sum = 0
    for i in lst:
        sum = sum + i
    print(sum)    

if __name__ == "__main__":
    main()    