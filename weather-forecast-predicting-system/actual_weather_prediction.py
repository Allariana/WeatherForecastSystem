import OWMApi
import pickle
from keras.models import load_model
from joblib import load
from pandas import DataFrame

actual_data = []
actual_data = OWMApi.get_actual_weather_data()
df = DataFrame(actual_data).transpose()
values = df.values
values = values.astype('float32')
# scaler = load('scaler.bin')
# scaler = pickle.load(open('scaler.pkl', 'rb'))
scaler = load('scaler.joblib')
# scaled = scaler.fit_transform(values)
scaled = scaler.transform(values)

# load model from single file
model = load_model('lstm_model.h5')
# make predictions
# yhat = model.predict(X, verbose=0)
# print(yhat)