from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study.")


    DataSet = load_iris()

    print(DataSet.data[0])
    print(DataSet.data[1])
    print(DataSet.data[2])
    print(DataSet.data[3])

    print(DataSet.target[0])
    print(DataSet.target[1])
    print(DataSet.target[2])
    print(DataSet.target[3])

    print(DataSet.target[50])
    print(DataSet.target[51])
    print(DataSet.target[52])
    print(DataSet.target[53])

    print(DataSet.target[100])
    print(DataSet.target[101])
    print(DataSet.target[102])
    print(DataSet.target[103])
    
if __name__ == "__main__":    
    main()
