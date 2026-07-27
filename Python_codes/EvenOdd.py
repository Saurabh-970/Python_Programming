
def EvenOdd(iNo):

    if iNo % 2 == 0:
        print("Even number")
    elif iNo % 3 == 0:
        print("Number is divisibile by 3")
    else :
        print("Number is odd")    

def main():
    

    print("Enter the number.")
    number = int(input())

    EvenOdd(number)


if __name__ == "__main__":
    main()