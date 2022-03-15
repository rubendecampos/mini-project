from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn import model_selection


#Dictionnary of the differents proposition of preprocessing and their respective object
prepro_methods_choice = {"min_max":preprocessing.MinMaxScaler(),"z_norm":preprocessing.StandardScaler()}



def preprocess(train_set,test_set,method_choice,poly_choice):

    prepro_object=prepro_methods_choice[method_choice]

    preproc_train = train_set
    preproc_test = test_set

    if(poly_choice):

        poly_scaler = preprocessing.PolynomialFeatures()

        preproc_train = poly_scaler.fit_transform(train_set)
        preproc_test = poly_scaler.transform(test_set)


    
    preproc_train = prepro_object.fit_transform(preproc_train)
    preproc_test = prepro_object.transform(preproc_test)


    preproc_train = pd.DataFrame(preproc_train)
    preproc_test = pd.DataFrame(preproc_test)


    return preproc_train,preproc_test


if __name__ == '__main__':

    data = pd.read_csv('Datasets/winequality-white.csv', sep=';')   
    train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=0)


    print(train_set)

    print(test_set)

    for n, p in enumerate(prepro_methods_choice):

        print("choice n°"+str(n)+" "+p)

    method_choice = list(prepro_methods_choice)[int(input())]

    print("use polynomial_feature ? ")

    poly_choice = int(input())

    preproc_train,preproc_test= preprocess(train_set, test_set,method_choice,poly_choice)


    print(preproc_train)

    print(preproc_test)
