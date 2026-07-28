def main():

    lst = list(map(int,input("Enter the list :\n").split()))

    temp = []

    for i in lst:
        temp = [i] + temp
    print(temp)
main()        