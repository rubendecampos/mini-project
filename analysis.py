from sklearn import metrics


def analyser(predict,real):
    """
    Perform the absolute error between the prediction of the algorithm
    the real data.

    param train_set: Pandas Dataframe of the train set
    param test_set: Pandas Dataframe of the test set
    
    return: a float (the absolute error)
    """ 

    error = metrics.mean_absolute_error(real, predict)
    return error