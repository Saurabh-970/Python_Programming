def main():
    pass

    lst = list(map(int,input("Enter the number").split()))

    Add = 0
    for i in lst:
        Add = Add + i

    Avg = Add / len(lst)
    print(Avg)    


if __name__ == "__main__":
    main()    