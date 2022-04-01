"""Test unit for the algorithm code"""

from algorithm import train_algo_and_predict
import numpy as np


def test_not_array_train():
    '''Test when train is not an np.ndarray'''

    passed = False

    try:

        algo_result = train_algo_and_predict("train_set","test_set","method_choice")

    except TypeError:

        passed = True

    assert passed


def test_not_in_choices():
    '''Test when method_choice is not the choices'''

    passed = False

    train_set=np.array([[0,0],[1,1]])

    test_set=np.array([[0,0],[1,1]])

    try:

        algo_result = train_algo_and_predict(train_set,test_set,"method_choice")

    except KeyError:

        passed = True

    assert passed


def test_different_shape():
    '''Test when number of column is different'''

    passed = False

    train_set=np.array([[0,0,0],[1,1,1]])

    test_set=np.array([[0,0],[1,1]])

    try:

        algo_result = train_algo_and_predict(train_set,test_set,"LIN_REGRESSION")

    except IndexError:

        passed = True

    assert passed

def test_shape_predict_lin():
    '''Test number of rows of the prediction match number of rows test for linear_regretion'''

    train_set=np.array([[0,0,0],[1,1,1]])

    test_set=np.array([[0,0,0],[1,1,1]])

    algo_result = train_algo_and_predict(train_set,test_set,"LIN_REGRESSION")

    assert algo_result.shape[0]== test_set.shape[0]

def test_shape_predict_dec_tree():
    '''Test number of rows of the prediction match number of rows test for decision_tree'''

    train_set=np.array([[0,0,0],[1,1,1]])

    test_set=np.array([[0,0,0],[1,1,1]])

    algo_result = train_algo_and_predict(train_set,test_set,"DECISION_TREE")

    assert algo_result.shape[0]== test_set.shape[0]

def test_predict_lin():
    '''Test prediction output for linear_regretion example took from sklearn documentation'''

    X=np.array([[1,1],[1,2],[2,2],[2,3]])

    y = np.dot(X, np.array([1, 2])) + 3

    train_set = np.column_stack((X,y))

    test_set=np.array([[3,5,0],[1,2,3]])

    print(test_set.T.shape)

    expected=np.array([16])

    algo_result = train_algo_and_predict(train_set,test_set,"LIN_REGRESSION")

    assert np.isclose(algo_result[0],expected)

def test_predict_dec_tree():
    '''Test prediction output for decision_tree example took from sklearn documentation'''

    train_set=np.array([[0,0,0],[1,1,1]])

    test_set=np.array([[2,2,3],[1,2,3]])

    expected=np.array([1])

    algo_result = train_algo_and_predict(train_set,test_set,"DECISION_TREE")

    assert np.isclose(algo_result[0],expected)
