from pandas import read_csv
from numpy import split
from numpy import array
from sklearn.preprocessing import MinMaxScaler

from constants import *


# split a univariate dataset into train/test sets
def split_dataset(data):
    train = values[:TRAIN_SIZE, :]
    test = values[TRAIN_SIZE:, :]
    train = array(split(train, len(train)/3))
    test = array(split(test, len(test)/3))
    return train, test

dataset = read_csv(DESTINATION_FOLDER + FILENAME, header=0, index_col=0)
values = dataset.values
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# split into train and test
train, test = split_dataset(scaled)
