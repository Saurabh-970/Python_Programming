def main():
    Ans = 0

    try:
        print("Inside try")

        print("Enter 1 no : ")
        No1 = int(input())

        print("Enter 2 no : ")
        No2 = int(input())
        
        Ans = No1/No2
        
    except:
        print("Inside except")
    finally:
        print("Inside finally")

        
    print("Division is : ",Ans)

if __name__ == "__main__":
    main()