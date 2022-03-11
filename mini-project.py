import csv
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import numpy as np
import pandas as pd

#-------------------------------------------------------------
# mini-project workflow
#-------------------------------------------------------------
# Goal : try to make the code work and understand
# how everything work.
# Try to implement the workflow given in activity 3 in
# an easier way.
# For this little program we use only the white wine quality
# database and only one pair of train/test sets


#----------------
# DATABASE
#----------------
print("DATA SPLITING\n-------------------------------")

# get the data from the file using pandas
data = pd.read_csv('Datasets/winequality-white.csv', sep=';')

# split the data in a training set and a data set (50/50). random_state is the seed (for reproducibility)
train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=0)

# they are the same size, GOOD!
print("Training set :")
display(train_set)
print("Test set :")
display(test_set)


#----------------
# PREPROCESSOR
#----------------

print("PREPROCESSING\n-------------------------------")

# Preprocessing 1: minmax method
minmax_scaler = preprocessing.MinMaxScaler()

minmax_train = pd.DataFrame(train_set)
minmax_test = pd.DataFrame(test_set)
minmax_train[:] = minmax_scaler.fit_transform(train_set[:])
minmax_test[:] = minmax_scaler.transform(test_set[:])

##############################################

# Preprocessing 2 : z-normalization
"""
std_scaler = preprocessing.StandardScaler()

std_train = pd.DataFrame(train_set)
std_test = pd.DataFrame(test_set)
std_train[:] = std_scaler.fit_transform(train_set[:])
std_test[:] = std_scaler.transform(test_set[:])

"""

#Preprocessing 3: minmax using Polynomial_Features
"""
poly_scaler = preprocessing.PolynomialFeatures()

poly_train = pd.DataFrame(train_set)
poly_test = pd.DataFrame(test_set)
poly_train[:] = poly_scaler.fit_transform(train_set[:])
poly_test[:] = poly_scaler.transform(test_set[:])

"""

#Preprocessing 4: z-normalization using Polynomial_Features

# print the output
print("MinMax training :")
display(minmax_train)
print("MinMax test :")
display(minmax_test)


#----------------
# ALGORITHM
#----------------
print("ALGORITHM COMPUTATION\n-------------------------------")

# pop 'quality' column and put it in the output array
# put the rest in the input array
y_train = minmax_train.pop('quality')
x_train = minmax_train

print("Output Y_train :")
display(y_train)
print("Input X_train :")
display(x_train)

# fit the x and y in the linear regression model
lin_regression = linear_model.LinearRegression()
lin_regression.fit(x_train,y_train)

# TODO : CONTINUE THE ALGO PART, BUILD THE MODEL ETC...

y_test = minmax_test.pop('quality')
x_test = minmax_test

print("Output Y_test :")
display(y_test)
print("Input X_test :")
display(x_test)

y_predi_lin = lin_regression.predict(x_test)

print("Output Y_Predi :")
display(y_predi_lin)

#############################################

#regretion tree

DecisionTree = DecisionTreeRegressor(random_state=0)
DecisionTree.fit(x_train,y_train)


y_predi_tree = DecisionTree.predict(x_test)

print("Output Y_Predi :")
display(y_predi_tree)


#----------------
# ANALYSIS
#----------------

error_lin = metrics.mean_absolute_error(y_test, y_predi_lin)

error_tree = metrics.mean_absolute_error(y_test, y_predi_tree)


print('MAE linear regretion:', error_lin)

print('MAE regression tree:', error_tree)
