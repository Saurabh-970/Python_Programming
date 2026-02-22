from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study.")


    DataSet = load_iris()

    Border = "-"*50
    print(Border)

    for i in range(len(DataSet.target)):
        print("ID %d, Features %s, Label %s"%(i,DataSet.data[i],DataSet.target[i]))

    print(Border)
if __name__ == "__main__":    
    main()
