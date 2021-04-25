from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from keras.models import Sequential
from keras.layers import Dense, LSTM
from joblib import dump
import pickle
from constants import *


# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

dataset = read_csv(DESTINATION_FOLDER + FILENAME, header=0, index_col=0)
values = dataset.values
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
dump(scaler, 'scaler.joblib')
dump(scaler, 'scaler.bin', compress=True)
pickle.dump(scaler, open('scaler.pkl', 'wb'))
# frame as supervised learning
reframed = series_to_supervised(scaled, N_DAYS, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[[25, 26, 28, 29]], axis=1, inplace=True)
# reframed.drop(reframed.columns[[27, 28, 30, 31, 32, 33, 34, 35]], axis=1, inplace=True)
# reframed.drop(reframed.columns[[3]], axis=1, inplace=True)
# split into train and test sets
values = reframed.values
X = values[:, :N_OBS]
y = values[:, -N_FEATURES]
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.15, random_state=42)
# train = values[:TRAIN_SIZE, :]
# test = values[TRAIN_SIZE:, :]
# # split into input and outputs
# train_X, train_y = train[:, :N_OBS], train[:, -N_FEATURES]
# test_X, test_y = test[:, :N_OBS], test[:, -N_FEATURES]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], N_DAYS, N_FEATURES))
test_X = test_X.reshape((test_X.shape[0], N_DAYS, N_FEATURES))
# design network
model = Sequential()
model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
# fit network
history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
# save model to single file
model.save('lstm_model.h5')
# make a prediction
yhat = model.predict(test_X)
test_X = test_X.reshape((test_X.shape[0], N_DAYS*N_FEATURES))
# invert scaling for forecast
inv_yhat = concatenate((yhat, test_X[:, -4:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
# # invert scaling for actual
test_y = test_y.reshape((len(test_y), 1))
inv_y = concatenate((test_y, test_X[:, -4:]), axis=1)
inv_y = scaler.inverse_transform(inv_y)
inv_y = inv_y[:, 0]
# plot forecasts against actual outcomes
pyplot.plot(inv_y, label='wartość oczekiwana')
pyplot.plot(inv_yhat, color='red', label='wartość prognozowana')
pyplot.legend()
pyplot.xlabel('Numer próbki')
pyplot.ylabel('Średnia temperatura dobowa °C')
pyplot.title('Wykres wartości prognozowanej średniej temperatury dobowej')
pyplot.show()

# inv_y_cut = inv_y[440:]
# inv_yhat_cut = inv_yhat[440:]
inv_y_cut = inv_y[350:]
inv_yhat_cut = inv_yhat[350:]
pyplot.plot(inv_y_cut, label='wartość oczekiwana')
pyplot.plot(inv_yhat_cut, color='red', label='wartość prognozowana')
pyplot.legend()
pyplot.xlabel('Numer próbki')
pyplot.ylabel('Średnia temperatura dobowa °C')
pyplot.title('Wykres wartości prognozowanej średniej temperatury dobowej')
pyplot.show()
for t in range(400):
    print('predicted=%f, expected=%f' % (inv_yhat[t], inv_y[t]))
# calculate RMSE
rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
print('Test RMSE: %.3f' % rmse)
# print()
