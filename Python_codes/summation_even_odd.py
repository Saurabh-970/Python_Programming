def main():

    lst = list(map(int,input("Enter the list\n").split()))

    sum_odd = 0
    sum_even = 0

    for num in range(len(lst)):
        if lst[num] % 2 == 0:
            sum_even = sum_even + lst[num]
        else:
            sum_odd = sum_odd + lst[num]
            
    print("Summation of even number is : ",sum_even)
    print("Summartion of odd number is : ",sum_odd)    

main()