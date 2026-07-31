def main():

    lst = list(map(int,input("Enter the list\n").split()))
    find = int(input("Enter the number to check the frequency\n"))
    count = 0

    for i in lst:
        if i == find:
            count += 1
    print("Frequency of the number is ",count)
main()        