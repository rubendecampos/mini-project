import database
import pandas as pd
import numpy as np
from sklearn import model_selection

def test_database_get_1():
    data = database.load_data(1)
    protocols = database.create_protocols(data, 3)
    
    train_set_expected = database.get('proto2','train')
    test_set_expected = database.get('proto2','test')

    data = pd.read_csv('Datasets/winequality-white.csv', sep=';')
    train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=2)

    assert (np.isclose(train_set_expected, train_set), f'Expected {train_set_expected}, but got {train_set}')
    assert (np.isclose(test_set_expected, test_set), f'Expected {test_set_expected}, but got {test_set}')
