def EmployeeInfo(Name  ,Age,Salary,City= "Mumbai"):
    print("Name : ",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)

def main():
   # EmployeeInfo(Age = 26, Name= "Rahul" , City= "Pune",Salary= 2000.50)  #correct
   EmployeeInfo("Rahul",26,24566,"Pune")
   EmployeeInfo("Rahul",26,24566)

if __name__ == "__main__":
    main()