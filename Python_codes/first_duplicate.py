def main():
    
    lst = list(map(int,input("Enter the list\n").split()))

    for i in range(len(lst)):
        for j in range(i + 1,len(lst)):
            if lst[i] == lst[j]:
                print("first duplicate element is ",lst[i])
                return
    print("No duplicate element found\n")        
main()            