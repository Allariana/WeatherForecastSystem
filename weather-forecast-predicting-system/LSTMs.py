from pandas import read_csv
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
from constants import *
# define contrived series
data = read_csv(DESTINATION_FOLDER + "\warsaw.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
series = Series(data)
print(series)
# prepare data for normalization
values = series.values
values = values.reshape((len(values), 1))
# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print
normalized = scaler.transform(values)
print(normalized)
# inverse transform and print
inversed = scaler.inverse_transform(normalized)
print(inversed)