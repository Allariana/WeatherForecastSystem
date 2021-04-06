import math

from keras.activations import sigmoid
from keras.optimizer_v1 import SGD
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation
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
# normalize the dataset and print
normalized = scaler.transform(values)
values = DataFrame(DataFrame(normalized).values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t-1', 't']
data = dataframe.to_numpy()
data = data.reshape((data.shape[0], data.shape[1], 1))
# inverse transform and print
inversed = scaler.inverse_transform(normalized)
# print(inversed)
# define the model
model = Sequential()
model.add(LSTM(5, input_shape=(2, 1)))
model.add(Dense(1))
algorithm = SGD(lr=0.1, momentum=0.3)
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])
# split data for train and test
training_dataset_length = math.ceil(len(data) * .75)
train_data = data[0:training_dataset_length, :]
x_train = []
y_train = []


for i in range(10, len(train_data)):
    x_train.append(train_data[i-10:i, 0])
    y_train.append(train_data[i, 0])

model.fit(x_train, y_train, batch_size=32, epochs=100)
print()
