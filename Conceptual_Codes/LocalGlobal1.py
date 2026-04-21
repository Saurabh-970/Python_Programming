No = 11   #global

def Fun():
    No = 21   # local
    print("Value of no from fun is : ",No)  #21

print("Value of No is : ",No) #11
Fun()