from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn import model_selection
import pandas as pd

'''algorithm module that use the previously preprocessed data and predict their output'''

#Dictionnary of the differents proposition of algorithms and their respective object
#Algorithms can be added by adding the name of the method as key of the dictionnary and the algorithm object as value
algo_choice = {"LIN_REGRESSION":linear_model.LinearRegression(),"DECISION_TREE":DecisionTreeRegressor(random_state=0)}


def train_algo_and_predict(train_set,test_set,method_choice):
    """Train a machine learning algorithm using the train set and
    perform a prediction

    Parameters
    ----------
    train_set : numpy.array
        use to train the model
    test_set : numpy.array
        set that will be use to test our algorithm
    method_choice : str
        the chosen algo method. The available method are : Linear Regression and Regression Tree.

    Returns
    -------
    prediction : array
        the predicted output""" 

    if(not isinstance(train_set,np.ndarray)):

        raise TypeError("train_set is %s, should be a np.ndarray"% type(train_set))

    if(not isinstance(test_set,np.ndarray)):

        raise TypeError("test_set is %s, should be a np.ndarray"% type(test_set))

    if(not isinstance(method_choice,str)):

        raise TypeError("method_choice is %s, should be a string"% type(method_choice))

    if(method_choice not in algo_choice):

        raise KeyError("method_choice %s, does not exists in algo choices "% str(method_choice))


    if(train_set.shape[1]!=test_set.shape[1]):

        raise IndexError("train and test sets should have the same number of columns, train has %s and test has shape %s"% (train_set.shape[1],test_set.shape[1]))


    algo_object=algo_choice[method_choice]

    y_train = train_set[:,-1]
    x_train = train_set[:,:-1]

    x_test = test_set[:,:-1]

    algo_object.fit(x_train,y_train)

    prediction = algo_object.predict(x_test)

    return prediction

