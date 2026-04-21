No = 11   #global

def Fun():
    global No 
    print("Value of n o from fun is : ",No) #11 
    No = No + 1   #12
    print("Value of no from fun is : ",No) #12

print("Value of No is : ",No) #11
Fun()
print("Value of No is : ",No) 