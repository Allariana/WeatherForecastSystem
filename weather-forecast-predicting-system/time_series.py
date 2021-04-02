# create a lag feature
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

from constants import *

series = read_csv(DESTINATION_FOLDER + "\warsaw.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
temps = DataFrame(series.values)
dataframe = concat([temps.shift(3), temps.shift(2), temps.shift(1), temps], axis=1)
dataframe.columns = ['t-2', 't-1', 't', 't+1']
print(dataframe.head(5))