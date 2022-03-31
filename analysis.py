from sklearn import metrics
import numpy as np


def analyser(predict,real):
    """
    Perform the absolute error between the prediction of the algorithm
    the real data.

    param train_set: numpy array of the train set
    param test_set: numpy array Dataframe of the test set
    
    return: a float (the absolute error)
    """ 
    if(isinstance(predict,np.ndarray)):

        raise TypeError("predict is %s, should be a numpy array"% type(predict))

    if(isinstance(predict,np.ndarray)):

        raise TypeError("real is %s, should be a numpy array"% type(real))


    if(predict.shape==real.shape):

        raise IndexError("predict and real should have the same shape and predict have shape %s and real have shape %s"% (predict.shape,real.shape) )

    error = metrics.mean_absolute_error(real, predict)
    return error