import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import 
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#---------------------------------------------------------------------------------#
# Step 1 : Load the dataset
#---------------------------------------------------------------------------------#

df = pd.read_csv("breast_cancer.csv")
print("Shape of dataset is ",df.shape )
print("First 5 records : ",df.head())

#---------------------------------------------------------------------------------#
# Step 2 : Seperate features and lables
#---------------------------------------------------------------------------------#

X = df.drop("target",axis=1)
Y = df["target"]

#---------------------------------------------------------------------------------#
# Step 3 : Split dataset for training and testing
#---------------------------------------------------------------------------------#

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------------------------------------------------------#
# Step 4 : Create boosting model (Adaboost)
#---------------------------------------------------------------------------------#

boost_model = Ada(random_state=42)

#---------------------------------------------------------------------------------#
# Step 5 : Create Bagging model
#---------------------------------------------------------------------------------#

boost_model = AdaBoostClassifier(
    estimator=boost_model,
    n_estimators=10,
    random_state=42
)

#---------------------------------------------------------------------------------#
# Step 5 : Train Bagging model
#---------------------------------------------------------------------------------#

boost_model.fit(X_train,Y_train)

#---------------------------------------------------------------------------------#
# Step 7 : Test Bagging Model
#---------------------------------------------------------------------------------#

Y_pred = boost_model.predict(X_test)

#---------------------------------------------------------------------------------#
# Step 7 : Evaluate Baggging Model
#---------------------------------------------------------------------------------#

print("Boosting accuracy : ",accuracy_score(Y_test,Y_pred))

print("Confusion matrix : ")
print(confusion_matrix(Y_test,Y_pred))