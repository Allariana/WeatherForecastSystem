from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AR

from constants import *

series = read_csv(DESTINATION_FOLDER + "\warsaw.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
# create a lag feature
temps = DataFrame(series.values)
# dataframe = concat([temps.shift(3), temps.shift(2), temps.shift(1), temps], axis=1)
# dataframe.columns = ['t-2', 't-1', 't', 't+1']
# print(dataframe.head(5))

# lag plot of time series
# lag_plot(series)
# pyplot.show()

# correlation of lag=1
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t', 't+1']
result = dataframe.corr()
print(result)

# autocorrelation plot of time series
# autocorrelation_plot(series)
# pyplot.show()
# plot_acf(series, lags=31)
# pyplot.show()

# evaluate a persistence model
# create lagged dataset
# dataframe = concat([temps.shift(1), temps], axis=1)
# dataframe.columns = ['t', 't+1']
# # split into train and test sets
# X = dataframe.values
# train, test = X[1:len(X) - 7], X[len(X) - 7:]
# train_X, train_y = train[:, 0], train[:, 1]
# test_X, test_y = test[:, 0], test[:, 1]


# persistence model
# def model_persistence(x):
#     return x
#
# # walk-forward validation
# predictions = list()
# for x in test_X:
#     yhat = model_persistence(x)
#     predictions.append(yhat)
# rmse = sqrt(mean_squared_error(test_y, predictions))
# print('Test RMSE: %.3f' % rmse)
#
# # plot predictions vs expected
# pyplot.plot(test_y)
# pyplot.plot(predictions, color='red')
# pyplot.show()

# create and evaluate a static autoregressive model - fatalne wyniki
# split dataset
X = series.values
train, test = X[1:len(X)-100], X[len(X)-100:]

# train autoregression
# model = AR(train)
# model_fit = model.fit()
# print('Lag: %s' % model_fit.k_ar)
# print('Coefficients: %s' % model_fit.params)
#
# # make predictions
# predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
# for i in range(len(predictions)):
#     print('predicted=%f, expected=%f' % (predictions[i], test[i]))
# rmse = sqrt(mean_squared_error(test, predictions))
# print('Test RMSE: %.3f' % rmse)
#
# # plot results
# pyplot.plot(test)
# pyplot.plot(predictions, color='red')
# pyplot.show()

# calculate residual errors for a persistence forecast model Test RMSE: 2.346
# load data
# create lagged dataset
# values = DataFrame(series.values)
# dataframe = concat([values.shift(1), values], axis=1)
# dataframe.columns = ['t', 't+1']
# split into train and test sets
X = dataframe.values
train_size = int(len(X) * 0.66)
train, test = X[1:train_size], X[train_size:]
train_X, train_y = train[:, 0], train[:, 1]
test_X, test_y = test[:, 0], test[:, 1]
# persistence model
predictions = [x for x in test_X]
# skill of persistence model
rmse = sqrt(mean_squared_error(test_y, predictions))
print('Test RMSE: %.3f' % rmse)
# calculate residuals
residuals = [test_y[i]-predictions[i] for i in range(len(predictions))]
residuals = DataFrame(residuals)
print(residuals.head())

print("Koniec")
