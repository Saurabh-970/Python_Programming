def EmployeeInfo(Name,Age,Salary,City):
    print("Name : ",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)

def main():
    #positional
    #EmployeeInfo("Neha", 21 , 2000.678 ,"Pune")  # correct
    #EmployeeInfo(21 ,"NEHA" ,"Pune", 2000.678 )  # wrong

    #Keyword arguments
    EmployeeInfo(Age = 26, Name= "Rahul" , City= "Pune",Salary= 2000.50)  #correct

if __name__ == "__main__":
    main()