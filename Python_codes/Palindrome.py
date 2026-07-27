def main():
    StringX = input("Enter the String...")

    reversed_string = ""

    for ch in StringX:
        reversed_string = ch + reversed_string

    if StringX == reversed_string :
        print("Its a palindrom string..")
    else:
        print("Not palindrome")    
        

if __name__ == "__main__":
    main()    