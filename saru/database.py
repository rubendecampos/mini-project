import pandas as pd
from sklearn import model_selection
import pkg_resources

"""Database module to load and split the housing and wine database into different set : test and training"""

protocols = dict()


def create_protocols(data, n):
    """Create n protocols, each protocol being split in a training set and a test set (50/50)
    !It clears the content of the 'protocols' dictionary!

    Parameters
    ----------
    data : pandas.dataframe
        the dataset to split into 50% of training and 50% and test
    n : int
        number of protocols to create, they are labeled 'proto1', ..., 'proton'

    Returns
    -------
    protocols : dict
        a dictionary containg all the protocols and their subset
    """

    protocols.clear()

    for i in range(n):
        # split the data in a random way. (random_state is used for reproducibility)
        train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=i)
        protocol = f'proto{i}'
        # put train and test set in the protocols dictionary
        protocols[protocol] = {
            'train': train_set,
            'test': test_set
        }

    return protocols


def get(protocol, subset):
    """Get the training or testing set from a protocol
    
    Parameters
    ----------
    protocol : str
        labal of the protocol to get (e.g. 'proto1')
    subset : str
        either 'test' or 'train'

    Returns
    -------
    the test or training set from a protocol : pandas.dataframe
    """
    proto = protocols[protocol]
    return proto[subset]

def set(protocol, train_set, test_set):
    """Set manually a new protocol
    
    Parameters
    ----------
    protocol : str
        the label of the new protocol
    train_set : list
        the training set
    test_set : list
        the test set"""

    protocols[protocol] = {
        'train': train_set,
        'test': test_set
    }

def load_data(user_choice):
    """Load the set of data according to the user choice

    Parameters
    ----------
    user_choice : str
        there are 3 possible choice : 'white-wine', 'red-wine' or 'housing', by default it is 
        set to 'white-wine"""

    if user_choice == 'white-wine':
        DATAFILE = pkg_resources.resource_filename(__name__, "Datasets/winequality-white.csv")
        data = pd.read_csv(DATAFILE, sep=';')
    elif user_choice == 'red-wine':
        DATAFILE = pkg_resources.resource_filename(__name__, "Datasets/winequality-red.csv")
        data = pd.read_csv(DATAFILE, sep=';')
    elif user_choice == 'housing':
        DATAFILE = pkg_resources.resource_filename(__name__, "Datasets/housing.data")
        data = pd.read_fwf(DATAFILE)
        data.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
    # combination of both red and white wine
    elif user_choice == 'wine':
        DATAFILE = pkg_resources.resource_filename(__name__, "Datasets/winequality-white.csv")
        data = pd.read_csv(DATAFILE, sep=';')
        DATAFILE2 = pkg_resources.resource_filename(__name__, "Datasets/winequality-red.csv")
        data = data.append(pd.read_csv(DATAFILE2, sep=';'), ignore_index=True)
    # default choice is set to white wine
    else:
        DATAFILE = pkg_resources.resource_filename(__name__, "Datasets/winequality-white.csv")
        data = pd.read_csv(DATAFILE, sep=';')
    
    return data
