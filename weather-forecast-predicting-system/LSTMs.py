from keras.optimizer_v1 import SGD
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
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
X = X.to_numpy()
X = X.reshape(1, 4022, 1)
y = y.to_numpy()
y = y.reshape(1, 4022, 1)
# define the model
model = Sequential()
model.add(LSTM(5, input_shape=(4022, 1)))
model.add(Dense(1))
algorithm = SGD(lr=0.1, momentum=0.3)
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])
# split data for train and test
# training_dataset_length = math.ceil(len(data) * .75)
# train_data = data[0:training_dataset_length, :]
# x_train = []
# y_train = []

# for i in range(10, len(train_data)):
#     x_train.append(train_data[i-10:i, 0])
#     y_train.append(train_data[i, 0])

model.fit(X, y, batch_size=3500, epochs=100)
# Evaluate the Model
loss, accuracy = model.evaluate(X, y)  # accuracy 0.0002
print()
