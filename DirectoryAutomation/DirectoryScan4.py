#############################  FILE input output in python ######################################

import os

##############################################################################
# Description   : working on directory
# Function name : DirectoryScanner
# Author        : Neha Navin Desai
# Date          : 31/01/2025
# Input         : create folders subfolders
# Output        : display folders subfolders
###############################################################################

# os.walk :  returns 3 lists folders subfolders filename

def DirectoryScanner(DirectoryName = "Marvellous"):
    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("Unable to scan as its not a directory")  
        return
          
    print("Contents of the directory are : ")

    for FolderName, subFolderName , FileName in os.walk(DirectoryName):
        print("folder name : ",FolderName)

        for subf in subFolderName:
            print("SubFolder name : ",subf)

        for fName in FileName:
            print("File Name : ",fName)

def main():
    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)

    

if __name__ == "__main__":
    main()