from sklearn import preprocessing
import numpy as np
import pandas as pd
from sklearn import model_selection

'''preprocessing module : to ensure that our algorithm works correctly, we preprocess the
the data using 4 preprocessing techniques'''

#Dictionnary of the differents proposition of preprocessing and their respective object
#Methods can be added by adding the name of the method as key of the dictionnary and the preprocessing object as value
prepro_methods_choice = {"min_max":preprocessing.MinMaxScaler(),"z_norm":preprocessing.StandardScaler()}


def preprocess(train_set,test_set,method_choice,poly_choice):
    '''preprocess get a splitted (in two part) dataset (train and test)
    and apply a preprocess method on both subsets.

    Parameters
    ----------
    train_set : pandas.DataFrame 
        datafram of the train set
    test_set : pandas.DataFrame
        dataframe of the test set
    method_choice : str
        the chosen preprocessing method. The available methods are 'min_max' and 'z_norm          
    poly_choice : bool
        set at True if a polynomial feature is needed before preprocessing, Warning using polynomial
        feature, the ouput column has to be the last column of the sets

    Returns
    -------
    preproc_train, preproc_test : numpy.array
        two numpy subsets (train and test) preprocessed'''

    if(not isinstance(train_set,pd.DataFrame)):

        raise TypeError("train_set is %s, should be a pandas.DataFrame"% type(train_set))

    if(not isinstance(test_set,pd.DataFrame)):

        raise TypeError("test_set is %s, should be a pandas.DataFrame"% type(test_set))

    if(not isinstance(method_choice,str)):

        raise TypeError("method_choice is %s, should be a string"% type(method_choice))

    if(not isinstance(poly_choice,bool)):

        raise TypeError("poly_choice is %s, should be a bool"% type(poly_choice))
   
    if(method_choice not in prepro_methods_choice):

        raise KeyError("method_choice %s, does not exists in methods choices "% str(method_choice))

    if(len(train_set.columns)!=len(test_set.columns)):

        raise IndexError("train and test sets should have the same number of columns, train has %s and test has shape %s"% (len(train_set.columns),len(test_set.columns)))

    prepro_object=prepro_methods_choice[method_choice]
    
    preproc_train = np.array(train_set)
    preproc_test = np.array(test_set)

    if(poly_choice):

        poly_scaler = preprocessing.PolynomialFeatures()
        

        #Generate the polynomial features without the output column
        tmp_train = poly_scaler.fit_transform(preproc_train[:,:-1])
        tmp_test = poly_scaler.transform(preproc_test[:,:-1])
        #adding the output column after generation of the polynomial features
        preproc_train = np.column_stack((tmp_train,preproc_train[:,-1])) 
        preproc_test = np.column_stack((tmp_test,preproc_test[:,-1]))


    #apply the chosen preprocessing method on train and test subdataset
    preproc_train = prepro_object.fit_transform(preproc_train)
    preproc_test = prepro_object.transform(preproc_test)

    return preproc_train,preproc_test


if __name__ == '__main__':

    data = pd.read_csv('Datasets/winequality-white.csv', sep=';')   
    train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=0)




    for n, p in enumerate(prepro_methods_choice):

        print("choice n°"+str(n)+" "+p)

    method_choice = list(prepro_methods_choice)[int(input())]

    print("use polynomial_feature ? ")

    poly_choice = bool(input())

    preproc_train,preproc_test= preprocess(train_set, test_set,method_choice,poly_choice)


