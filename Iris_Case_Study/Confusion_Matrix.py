from sklearn.metrics import confusion_matrix

def main():

    # 1 : Positive
    # 2 : Negative

    Actual = [1,0,1,1,1,0,1,0,0,1]
    Predcited = [1,0,0,1,1,1,1,1,0,1]

    print("Actual data :",Actual)
    print("Predicted data :",Predcited)

    con_mat = confusion_matrix(Actual,Predcited)

    print(con_mat)

    
if __name__ == "__main__":    
    main()
