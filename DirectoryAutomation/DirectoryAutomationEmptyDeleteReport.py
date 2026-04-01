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

    FileCount = 0
    EmptyFileCount = 0

    for FolderName , subFolderName , FileName in os.walk(DirName):
        
            for fName in FileName:
                FileCount = FileCount + 1
                fName = os.path.join(FolderName,fName)
                print("File name : ",fName)
                print("File size : ",os.path.getsize(fName))
                if(os.path.getsize(fName)==0):        #empty file
                    EmptyFileCount = EmptyFileCount + 1
                    os.remove(fName)

    Border = "-"*50
    print(Border)
    print("--------------Automation Report-------------")
    print("Files found : ",FileCount)
    print("Total empty files found : ",EmptyFileCount)
    print(Border)

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

    print(Border)
    print("---------------Marvellous Directory Automation--------------")
    print(Border)

    

if __name__ == "__main__":
    main()