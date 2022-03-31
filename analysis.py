from sklearn import metrics
import numpy as np

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

    if(not isinstance(predict,np.ndarray)):

        raise TypeError("predict is %s, should be a numpy array"% type(predict))

    if(not isinstance(real,np.ndarray)):

        raise TypeError("real is %s, should be a numpy array"% type(real))


    if(predict.shape!=real.shape):

        raise IndexError("predict and real should have the same shape and predict have shape %s and real have shape %s"% (predict.shape,real.shape) )

    error = metrics.mean_absolute_error(real, predict)
    return error