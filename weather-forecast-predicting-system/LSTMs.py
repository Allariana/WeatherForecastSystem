from math import sqrt

from keras.optimizer_v1 import SGD
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.model_selection import train_test_split
from constants import *

# define contrived series
data = read_csv(DESTINATION_FOLDER + "\warsaw.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
series = Series(data)
# prepare data for normalization
values = series.values
values = values.reshape((len(values), 1))
# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
# normalize the dataset
normalized = scaler.transform(values)
# inverse transform
# inversed = scaler.inverse_transform(normalized)
# Preparing Data
values = DataFrame(DataFrame(normalized).values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t-1', 't']
X = dataframe['t-1']
y = dataframe['t']
# split data for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
X_train = X_train.to_numpy()
X_train = X_train.reshape(1, X_train.size, 1)
X_test = X_test.to_numpy()
X_test = X_test.reshape(1, X_test.size, 1)
y_train = y_train.to_numpy()
y_train = y_train.reshape(1, y_train.size, 1)
y_test = y_test.to_numpy()
y_test = y_test.reshape(1, y_test.size, 1)
#
# define the model
model = Sequential()
model.add(LSTM(5, input_shape=(X_train.size, 1)))
model.add(Dense(1))
algorithm = SGD(lr=0.1, momentum=0.3)
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])
#
#
# # model.fit(X, y, batch_size=3500, epochs=100)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, predictions))
# # Evaluate the Model
# loss, accuracy = model.evaluate(X, y)  # accuracy 0.0002
print()
