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
# Function name : CleanTitanicData
# Description   : It preprocessing
#                 It removes unnecessary columns
#                 It handles missing values
#                 It converts test data to numeric format
#                 It does encoding to categorical columns
# Parameters    : df -> Pandas dataframe
# Return        : df -> Clean Pandas dataframe
# Date          : 14/03/2026
# Author        : Saurabh Ravindra Bhonsle
#---------------------------------------------------------------------------------------#

def CleanTitanicData(df): 
    DisplayInfo("Step 2 : Original Data")
    print(df.head())

    # Remove unnecessary data
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existin_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be dropped : ")
    print(existin_columns)

    # DRop the unwanted columns

    df = df.drop(columns = existin_columns)
    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    # Handle age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # coerce mhanje invalid gets converted to Nan mhanje nhiye aplyakde
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()

        #Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\n Age column after preprocessing : ")
        print(df["Age"].head(10))

    # Handle fare column 
    if "Fare" in df.columns:
        print("\n Fare column before preprocessing")
        print(df["Fare"].head(10)) 

        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")   

        fare_median = df["Fare"].median()

        print("\n Median of fare column is",fare_median)

        #Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\n Fare column after preprocssing")
        print(df["Fare"].head(10))

   # handle exmbarked column
    if "Embarked" in df.columns:
        print("\n Embarked column before preprocessing")
        print(df["Embarked"].head(10)) 

        # convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values

        df["Embarked"] = df["Embarked"].replace(('nan','None',''),np.nan)

        # Get most frequent values
        embarked_mode = df["Embarked"].mode()[0]

        print("Mode of embarked column : ",embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\n Embarked column after preprocssing")
        print(df["Embarked"].head(10))

    # Handle Sex column 
    if "Sex" in df.columns:
        print("\n Sex column before preprocessing")
        print(df["Sex"].head(10)) 

        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")
        print("\n Sex column after preprocssing")
        print(df["Sex"].head(10))


    DisplayInfo("Step 3 : Data after preprocessing")
    print(df.head())   

    print("\n Missing values after preprocessing")
    print(df.isnull().sum())   
    return df
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
    df = CleanTitanicData(df)



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