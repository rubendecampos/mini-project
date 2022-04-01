
"""Test unit for the database code"""

import sys
sys.path.append('saru/')

import database
import pandas as pd
import numpy as np
from sklearn import model_selection

def doit(label, nb_proto, train_set_expected, test_set_expected):
    """Runs a test

    Parameters
    ==========

    label : string
        the name of the dataset to load

    nb_proto: int
        the nb of protocols to create

    train_set_expected, test_set_expected: pandas.dataframe
        two pandas dataframes containing the expected result of the test

    """

    data = database.load_data(label)
    protocols = database.create_protocols(data, nb_proto)
    
    train_set = database.get('proto{}'.format(nb_proto-1),'train')
    test_set = database.get('proto{}'.format(nb_proto-1),'test')
    
    assert (np.isclose(train_set_expected, train_set), f'Expected {train_set_expected}, but got {train_set}')
    assert (np.isclose(test_set_expected, test_set), f'Expected {test_set_expected}, but got {test_set}')


def test_create_protocol_red():
    '''Test the creation of 3 red wine protocols'''

    data = pd.read_csv('saru/Datasets/winequality-red.csv', sep=';')
    train_set_expected, test_set_expected = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=2)

    doit('red-wine', 3, train_set_expected, test_set_expected)

def test_create_protocol_white():
    '''Test the creation of 3 white wine protocols'''

    data = pd.read_csv('saru/Datasets/winequality-white.csv', sep=';')
    train_set_expected, test_set_expected = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=2)
    doit('white-wine', 3, train_set_expected, test_set_expected)
    
def test_create_protocol_housing():
    '''Test the creation of 3 housing protocols'''

    data = pd.read_fwf('saru/Datasets/housing.data')
    train_set_expected, test_set_expected = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=2)
    doit('housing', 3, train_set_expected, test_set_expected)
