from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study.")


    DataSet = load_iris()

    # Metadata of dataset..............
    print("Independent variables are : ")
    print(DataSet.feature_names)
    print("Lenght of independent variable is",len(DataSet.feature_names))

    print("Dependent variables are :")
    print(DataSet.target_names)
    print("Lenght of dependent variable is",len(DataSet.target_names))

    

if __name__ == "__main__":    
    main()
