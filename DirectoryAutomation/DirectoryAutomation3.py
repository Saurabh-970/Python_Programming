############################# Automation in python ######################################

import sys
import os

##############################################################################
# Description   : working on directory automation
# Function name : DirectoryScanner 
# Author        : Neha Navin Desai
# Date          : 01/02/2026
# Input         : 
# Output        : 
###############################################################################
def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("Its not a directory")
        return


    for FolderName , subFolderName , FileName in os.walk(DirName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName)
            print("File name : ",fName)
            print("File size : ",os.path.getsize(fName))



def main():
    Border = "-"*60
    print(Border)

    print("---------------Marvellous Directory Automation--------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1])

    

if __name__ == "__main__":
    main()