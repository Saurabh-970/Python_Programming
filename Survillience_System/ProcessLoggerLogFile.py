#Command  line input

import psutil
import sys
import os

######################### PROCESS AUTOMATION ##########################
def CreateLog(FolderName):
    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")


def main():
    Border = "-"*50
    print(Border)
    print("---------- Platform Surveillance System---------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes Periodically")
            print("3 : Sends mail with the log")
            print("4 : Store infirmation about processes")
            print("5 : Store the information about the CPU")
            print("6 : Store the information about the RAM usage")
            print("7 : Store the information about the secondary storage")


        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print("Scriptname.py TimeInterval Directoryname")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    #python Demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("TimeInterval : ",sys.argv[1])
        print("DirectoryName : ",sys.argv[2])

        CreateLog(sys.argv[2])

    else:
        print("Invalid no of COMMAND LINE ARGUMENTS")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")






    print(Border)
    print("----------Thankyou for using our script----------")
    print(Border)
    

if __name__ == "__main__":
    main()