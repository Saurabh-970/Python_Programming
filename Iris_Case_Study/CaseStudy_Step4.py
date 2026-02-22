import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40
############################################################################################################
# Step 1 : Load the dataset
############################################################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)
print("Dataset gets loaded successfully...")
print("Initial entries from dataset :")
print(df.head())

############################################################################################################
# Step 2 : Data Analysis (EDA) Exploratory data analysis
############################################################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column names :",list(df.columns))

print("Missing values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["Species"].value_counts())

print("Statistical report of dataset")

print(df.describe())

############################################################################################################
# Step 3 : Decide Independent and Dependent Variables
############################################################################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X :   Independet variables or features
# Y :   Dependent variables/ lables

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y =df["Species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

############################################################################################################
# Step 4 : Visualisation of dataset
############################################################################################################

print(Border)
print("Step 4 : Visualisation of dataset :")
print(Border)

# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["Species"].unique():
    temp = df[df["Species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)


plt.title("Iris : Petal length vs Petal width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()   