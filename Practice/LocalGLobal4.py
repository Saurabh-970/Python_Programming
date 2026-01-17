No =  11      #Global

def Fun():
    global No 
    print("Value of No from fun is :", No)      #11
    No = No + 1         #12
    print("Value of No from fun is :", No)      #22

print("Value of No is :",No)    #11
Fun()
print("Value of No is :",No)    #12