import csv
from pyexpat.model import XML_CQUANT_REP
from re import S
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
print("-------------------------------\nDATA SPLITING\n-------------------------------")

# get the data from the file using pandas
data = pd.read_csv('Datasets/winequality-white.csv', sep=';')

# split the data in a training set and a data set (50/50). random_state is the seed (for reproducibility)
train_set, test_set = model_selection.train_test_split(data, train_size=0.5, test_size=0.5, random_state=0)

# they are the same size, GOOD!
print("Training set :")
print(train_set)
print("Test set :")
print(test_set)


#----------------
# PREPROCESSOR
#----------------

print("-------------------------------\nPREPROCESSING\n-------------------------------")

# Preprocessing 1: minmax method
minmax_scaler = preprocessing.MinMaxScaler()

minmax_train = minmax_scaler.fit_transform(train_set)
minmax_test = minmax_scaler.transform(test_set)
minmax_train = pd.DataFrame(minmax_train, columns=train_set.columns)
minmax_test = pd.DataFrame(minmax_test, columns=test_set.columns)


# Preprocessing 2 : z-normalization
std_scaler = preprocessing.StandardScaler()

std_train = std_scaler.fit_transform(train_set)
std_test = std_scaler.transform(test_set)
std_train = pd.DataFrame(train_set, columns=train_set.columns)
std_test = pd.DataFrame(test_set, columns=test_set.columns)


#Preprocessing 3: minmax using Polynomial_Features

poly_scaler = preprocessing.PolynomialFeatures()

poly_train = poly_scaler.fit_transform(train_set)
poly_test = poly_scaler.transform(test_set)
poly_train = pd.DataFrame(train_set, columns=train_set.columns)
poly_test = pd.DataFrame(test_set, columns=test_set.columns)

#Preprocessing 4: z-normalization using Polynomial_Features

# print the output
print("MinMax training :")
print(minmax_train)
print("MinMax test :")
print(minmax_test)

print("z-normalization training :")
print(std_train)
print("z-normalization test :")
print(std_test)


#----------------
# ALGORITHM
#----------------
print("-------------------------------\nALGORITHM COMPUTATION\n-------------------------------")

# pop 'quality' column and put it in the output array
# put the rest in the input array
# do that for each preprocessing technique
y_train = list()    
x_train = list()
y_train.insert(0, minmax_train.pop('quality'))
x_train.insert(0, minmax_train)
y_train.insert(1, std_train.pop('quality'))
x_train.insert(1, std_train)

y_test = list()
x_test = list()
y_test.insert(0, minmax_test.pop('quality'))
x_test.insert(0, minmax_test)
y_test.insert(1, std_test.pop('quality'))
x_test.insert(1, std_test)


# LINEAR REGRESSION
lin_regression = linear_model.LinearRegression()
lin_regression.fit(x_train[0],y_train[0])

# predict the result for the test data
y_predi_lin = list()
y_predi_lin.insert(0, lin_regression.predict(x_test[0]))
lin_regression.fit(x_train[1],y_train[1])
y_predi_lin.insert(1, lin_regression.predict(x_test[1]))


print("LIN REGRESSION - Output Y_Predi :")
print(y_predi_lin[0])
print(y_predi_lin[1])

#############################################

# REGRESSION TREE
DecisionTree = DecisionTreeRegressor(random_state=0)
DecisionTree.fit(x_train[0],y_train[0])

# predict the result for the test data
y_predi_tree = list()
y_predi_tree.insert(0, DecisionTree.predict(x_test[0]))

DecisionTree.fit(x_train[1],y_train[1])
y_predi_tree.insert(1, DecisionTree.predict(x_test[1]))

print("DECISION TREE - Output Y_Predi :")
print(y_predi_tree[0])
print(y_predi_tree[1])


#----------------
# ANALYSIS
#----------------

# display the mean absolute error
error_lin = metrics.mean_absolute_error(y_test[0], y_predi_lin[0])
error_tree = metrics.mean_absolute_error(y_test[0], y_predi_tree[0])

print('minmax preprocessing')
print('MAE linear regression : {:.4}%'.format(error_lin*100,))
print('MAE regression tree : {:.4}%'.format(error_tree*100))


error_lin = metrics.mean_absolute_error(y_test[1], y_predi_lin[1])
error_tree = metrics.mean_absolute_error(y_test[1], y_predi_tree[1])

print('z-normalization')
print('MAE linear regression : {:.4}%'.format(error_lin*100,))
print('MAE regression tree : {:.4}%'.format(error_tree*100))