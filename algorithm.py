from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn import model_selection
import pandas as pd

#Dictionnary of the differents proposition of algorithms and their respective object
#Algorithms can be added by adding the name of the method as key of the dictionnary and the algorithm object as value
algo_choice = {"LIN_REGRESSION":linear_model.LinearRegression(),"DECISION_TREE":DecisionTreeRegressor(random_state=0)}



def train_algo(train_set,test_set,method_choice):
    """
    Train a machine learning algorithm using the train set and
    perform a prediction

    param train_set: numpy array of the train set
    param test_set: numpy array of the test set
    param method_choice: The chosen algo method.
                         All available methods are referenced in the dictionnary
                         "algo_choice" above
    return: An array of the prediction of the algoritm
    """ 

    algo_object=algo_choice[method_choice]

    y_train = train_set[:,-1]
    x_train = train_set[:,:-1]

    print(y_train.shape)
    print(x_train.shape)

    x_test = test_set[:,:-1]

    print(x_test.shape)

    algo_object.fit(x_train,y_train)

    prediction = algo_object.predict(x_test)

    return prediction


if __name__ == '__main__':

    data = pd.read_csv('Datasets/winequality-white.csv', sep=';')   
    train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=0)

    train_set = np.array(train_set)

    test_set = np.array(test_set)

    print(train_set.shape)

    predi = train_algo(train_set,test_set,"LIN_REGRESSION")


    print(predi)
