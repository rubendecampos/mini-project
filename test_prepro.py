"""Test unit for the preprocessing code"""

from preprocessing import preprocess
from sklearn import preprocessing
import numpy as np
import pandas as pd


def test_not_dataframe_train():
    '''Test when train is not an dataframe'''

    passed = False

    try:

        process_result = preprocess("train_set","test_set","method_choice",2)

    except TypeError:

        passed = True

    assert passed

def test_not_bool_poly():
    '''Test when poly_feature is not a bool'''

    passed = False

    d = {'col1': [1, 2], 'col2': [3, 4]}

    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d)

    try:

        process_result = preprocess(train,test,"min_max",2)

    except TypeError:

        passed = True

    assert passed


def test_not_in_choices():
    '''Test when method_choice is not the choices'''

    passed = False

    d = {'col1': [1, 2], 'col2': [3, 4]}

    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d)

    try:

        process_result = preprocess(train,test,"method_choice",True)

    except KeyError:

        passed = True

    assert passed


def test_different_shape():
    '''Test when number of column is different'''

    passed = False

    d = {'col1': [1, 2], 'col2': [3, 4]}

    d1 = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}


    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d1)

    try:

        process_result = preprocess(train,test,"min_max",True)

    except IndexError:

        passed = True

    assert passed

def test_min_max_wo_poly():
    '''Test min_max_example took from sklearn documentation'''

    expected = np.array([[0,0],[0.25,0.25],[0.5,0.5],[1,1]])

    d = {'col1': [-1,-0.5,0,1], 'col2': [2,6,10,18]}

    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d)

    train_set, test_set = preprocess(train,test,"min_max",False)

    assert np.allclose(train_set,expected) and np.allclose(test_set,expected)

def test_z_norm_wo_poly():
    '''Test Z_norm example took from sklearn documentation'''

    expected = np.array([[0,-1.22,1.33],[1.22,0,-0.26],[-1.22,1.22,-1.06]])

    d = {'col1': [1, 2,0], 'col2': [-1,0,1],'col3':[2,0,-1]}

    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d)

    train_set, test_set = preprocess(train,test,"z_norm",False)

    assert np.allclose(train_set,expected,atol=1e-02) and np.allclose(test_set,expected,atol=1e-02)


def test_poly_feature_z_norm():
    '''Test polynomial with z_norm preprocessing features example took from sklearn documentation'''

    expected = np.array([[ 1,  0,  1,  0,  0,  1, 1],
       [ 1,  2,  3,  4,  6,  9, 2],
       [ 1,  4,  5, 16, 20, 25, 3]])

    expected2 = np.array([[ 1,  0,  1,  0,  0,  1, 4],
       [ 1,  2,  3,  4,  6,  9, 5],
       [ 1,  4,  5, 16, 20, 25, 6]])

    prepro=preprocessing.StandardScaler()

    expected = prepro.fit_transform(expected)

    expected2 = prepro.transform(expected2)

    d = {'col1': [0, 2,4], 'col2': [1,3,5],'col3':[1,2,3]}

    d2 = {'col1': [0, 2,4], 'col2': [1,3,5],'col3':[4,5,6]}

    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d2)

    train_set, test_set = preprocess(train,test,"z_norm",True)

    assert np.allclose(train_set,expected) and np.allclose(test_set,expected2)

def test_poly_feature_min_max():
    '''Test polynomial features with min_max preprocessing example took from sklearn documentation'''

    expected = np.array([[ 1,  0,  1,  0,  0,  1, 1],
       [ 1,  2,  3,  4,  6,  9, 2],
       [ 1,  4,  5, 16, 20, 25, 3]])

    expected2 = np.array([[ 1,  0,  1,  0,  0,  1, 4],
       [ 1,  2,  3,  4,  6,  9, 5],
       [ 1,  4,  5, 16, 20, 25, 6]])

    prepro=preprocessing.MinMaxScaler()

    expected = prepro.fit_transform(expected)

    expected2 = prepro.transform(expected2)

    d = {'col1': [0, 2,4], 'col2': [1,3,5],'col3':[1,2,3]}

    d2 = {'col1': [0, 2,4], 'col2': [1,3,5],'col3':[4,5,6]}

    train=pd.DataFrame(data=d)

    test=pd.DataFrame(data=d2)

    train_set, test_set = preprocess(train,test,"min_max",True)

    assert np.allclose(train_set,expected) and np.allclose(test_set,expected2)
