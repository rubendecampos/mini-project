from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn import model_selection


#Dictionnary of the differents proposition of preprocessing and their respective object
#Methods can be added by adding the name of the method as key of the dictionnary and the preprocessing object as value
prepro_methods_choice = {"min_max":preprocessing.MinMaxScaler(),"z_norm":preprocessing.StandardScaler()}


def preprocess(train_set,test_set,method_choice,poly_choice):
    '''preprocess get a splitted (in two part) dataset (train and test)
    and apply a preprocess method on both subsets.

    Parameters:
    ===========

    train_set : pandas Dataframe 
        datafram of the train set

    test_set : pandas Dataframe
        dataframe of the test set
    
    method_choice : str
        the chosen preprocessing method. The available methods are 'min_max' and 'z_norm
                         
    poly_choice : bool
        set at True if a polynomial feature is needed before preprocessing

    Return
    ======
    
    two numpy subsets (train and test) preprocessed'''
    
    prepro_object=prepro_methods_choice[method_choice]

    preproc_train = train_set
    preproc_test = test_set

    if(poly_choice):

        poly_scaler = preprocessing.PolynomialFeatures()
        
        #remove the quality column to generate the polynomial features
        tmp_train = train_set.pop('quality')
        tmp_test = test_set.pop('quality')

        preproc_train = poly_scaler.fit_transform(train_set)
        preproc_test = poly_scaler.transform(test_set)

        #adding the quality column after generation of the polynomial features
        np.append(preproc_train,tmp_train) 
        np.append(preproc_test,tmp_test)

    #apply the chosen preprocessing method on train and test subdataset
    preproc_train = prepro_object.fit_transform(preproc_train)
    preproc_test = prepro_object.transform(preproc_test)

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
