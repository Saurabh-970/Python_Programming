def main():

    lst = list(map(int,input("Enter the list\n").split()))
    find = int(input("Enter the number to search\n"))

    for i in range(len(lst)):
        if lst[i] == find:
            print("Element found at index .",i)
            return    
    print("Not found..")        

main()