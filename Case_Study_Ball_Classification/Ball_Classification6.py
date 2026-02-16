from sklearn import tree
# Rough 1
# Smooth 0

#Tennis = 1
#Cricket = 2

import sklearn

def main():
    print("Ball Classification Case Study.")

    # Independent Variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    # Dependent Variables
    Y =   [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independent variables for traning
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]

    # Independent variables for traning
    Xtest = [[35,1],[95,0]]

    # Dependent variables for training
    Ytrain =  [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Dependent variables for Testing
    Ytest =  [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain,Ytrain)

    Result = trainedmodel.predict([[35,1]]) 

    print("Model predicts the object as :",Result)

    if Result == 1:
        print("Object looks like tennis ball")
    elif Result == 2:
        print("Object looks like cricket ball")    

if __name__ == "__main__":    
    main()

# Data Set Size