from sklearn import metrics

'''analysis module that compare the predicted result with the real result'''

def analyser(predict,real):
    """Perform the absolute error between the prediction of the algorithm
    and the real data.

    Parameters
    ----------
    predict : pandas.dataframe
        predicted value, given by our algorithm
    real : Pandas.dataframe
        real value (from the test_set)
    
    Returns
    -------
    error : float
        the absolute error""" 

    error = metrics.mean_absolute_error(real, predict)
    return error