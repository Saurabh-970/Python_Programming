def main():

    StringX = input("Enter the string\n")

    start = 0
    end = len(StringX) - 1

    while(start < end):

        if(StringX[start] != StringX[end]):
            print("Not Palindrome")
            return
        
        start = start + 1
        end = end - 1

    print("It is palindrome")    

if __name__ == "__main__":
    main()    