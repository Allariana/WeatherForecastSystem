import OWMApi
from keras.models import load_model
from joblib import load
from pandas import DataFrame
import numpy as np
from numpy import concatenate
from constants import *

actual_data = []
actual_data = OWMApi.get_actual_weather_data()
df = DataFrame(actual_data).transpose()
values = df.values
values = values.astype('float32')
scaler = load('scaler.joblib')
values_all = values[:, 0:5]
values_all = scaler.transform(values_all)
for i in range(5, 21, 5):
    values_cut = values[:, i:(i+5)]
    values_cut = scaler.transform(values_cut)
    values_all = np.concatenate([values_all, values_cut], axis=1)

values_all = values_all.reshape((values_all.shape[0], N_DAYS, N_FEATURES))
# load model from single file
model = load_model('lstm_model.h5')
# make predictions
yhat = model.predict(values_all)
values_all = values_all.reshape((values_all.shape[0], N_DAYS*N_FEATURES))
# invert scaling for forecast
inv_yhat = concatenate((yhat, values_all[:, -4:]), axis=1)
inv_yhat = scaler.inverse_transform(inv_yhat)
inv_yhat = inv_yhat[:, 0]
result = int(round(inv_yhat[0]))

f = open("result.txt", "w+")
f.write("%d" % result)
f.close()
print(result)
