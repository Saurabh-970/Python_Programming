def main():
    lst = list(map(int,input("Enter the number").split()))

    Smallet = lst[0]
    for i in lst:
        if i < Smallet:
            Smallet =  i
    print(Smallet)        

if __name__ == "__main__":
    main()