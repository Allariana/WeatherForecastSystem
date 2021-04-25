import OWMApi
from keras.models import load_model

actual_data = []
actual_data = OWMApi.get_actual_weather_data()

# load model from single file
model = load_model('lstm_model.h5')
# make predictions
# yhat = model.predict(X, verbose=0)
# print(yhat)