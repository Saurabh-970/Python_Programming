def main():

    lst = list(map(int,input("Enter the list\n").split()))

    even_max = float('-inf')

    for num in lst:
        if num % 2 == 0:
            if num > even_max:
                even_max = num
    if even_max == float('-inf'):
        print("there is no even number")
    else:
        print("Largest even number is ",even_max)

main()        
