from sklearn import metrics

'''analysis module that compare the predicted result with the real result'''

def analyser(predict,real):
    """Perform the absolute error between the prediction of the algorithm
    and the real data.

    Parameter
    =========

    predict : pandas Dataframe
        predicted value, given by our algorithm
    
    real : Pandas Dataframe
        real value (from the test_set)
    
    Return
    ======
    
    error : float
        the absolute error""" 

    error = metrics.mean_absolute_error(real, predict)
    return error