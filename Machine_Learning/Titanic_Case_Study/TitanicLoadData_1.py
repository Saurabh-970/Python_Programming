import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#---------------------------------------------------------------------------------------#
# Function name : print("\n" + "-"*70)
# Description   : It displays the formatted title
# Parameters    : title (str)
# Return        : None
# Date          : 14/03/2026
# Author        : Saurabh Ravindra Bhonsle
#---------------------------------------------------------------------------------------#

def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)


#---------------------------------------------------------------------------------------#
# Function name : showData
# Description   : It shows basic information about dataset
# Parameters    : df
#                 df  ->     Pandas dataframe
#                 message
#                 message  -> Heading text to display
# Return        : None
# Date          : 14/03/2026
# Author        : Saurabh Ravindra Bhonsle
#---------------------------------------------------------------------------------------#

def showData(df, message):
    DisplayInfo(message)

    print("First five 5 rows of dataset")
    print(df.head())

    print("Shape of dataset")
    print(df.shape)

    print("\n")

    print("\nColumn names : ")
    print(df.columns.tolist())

    print("\nMissing values each column")
    print(df.isnull().sum())

#---------------------------------------------------------------------------------------#
# Function name : MarvellousTitanicLogistic
# Description   : This main piopeline controller
#                 It loads the dataset, shows raw data
#                 It preprocess the dataset and train the model
# Parameters    : Data path of datset of file
# Return        : None
# Date          : 14/03/2026
# Author        : Saurabh Ravindra Bhonsle
#---------------------------------------------------------------------------------------#

def MarvellousTitanicLogistic(DataPath):

    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    showData(df,"Initial dataset")


#---------------------------------------------------------------------------------------#
# Function name : main
# Description   : Starting point of application
# Parameters    : None
# Return        : None
# Date          : 14/03/2026
# Author        : Saurabh Ravindra Bhonsle
#---------------------------------------------------------------------------------------#

def main():
    
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")


if __name__ == "__main__":
    main()