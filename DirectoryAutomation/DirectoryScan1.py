#############################  FILE input output in python ######################################

import os

##############################################################################
# Description   : 
# Function name : main
# Author        : Neha Navin Desai
# Date          : 31/01/2025
# Input         : create folders subfolders
# Output        : display folders subfolders
###############################################################################

# os.walk :  returns 3 lists folders subfolders filename
def main():
    DirectoryName = input("Enter the name of directory : ")

    print("Contents of the directory are : ")

    for FolderName, subFolderName , FileName in os.walk(DirectoryName):
        print("folder name : ",FolderName)

        for subf in subFolderName:
            print("SubFolder name : ",subf)

        for fName in FileName:
            print("File Name : ",fName)



if __name__ == "__main__":
    main()