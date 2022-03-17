from re import sub
import numpy as np
import pandas as pd
from sklearn import model_selection

protocols = dict()

# generate n protocols, each protocol being split in a train set and a test set (50/50)
def create_protocols(data, n):

    for i in range(n):
        # split the data in a random way. (random_state is used for reproducibility)
        train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=0)
        protocol = f'proto{i}'
        # put train and test set in the protocols dictionary
        protocols[protocol] = {
            'train': train_set,
            'test': test_set
        }

    return protocols


# get the training or testing set from a protocol
def get(protocol, subset):
    proto = protocols[protocol]
    return proto[subset]

# set manually a new protocol
def set(protocol, train_set, test_set):
    protocols[protocol] = {
        'train': train_set,
        'test': test_set
    }

# load the data from the database chose by the user
def load_data(user_choice):
    data = pd.read_csv('Datasets/winequality-white.csv', sep=';')
    return data

if __name__ == '__main__':
    data = load_data(1)
    protocols = create_protocols(data,3)

    train_set = get('proto2','train')
    print(train_set)