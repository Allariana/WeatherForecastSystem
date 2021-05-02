import OWMApi
from keras.models import load_model
from joblib import load
from pandas import DataFrame
import numpy as np
from numpy import concatenate
from PIL import Image, ImageFont, ImageDraw
from constants import *
city = ['warsaw', 'KRAKÓW-OBSERWATORIUM']
d = {'lat': [52.29958465640118, 50.0649722906938], 'lon': [20.927704121901673, 19.988522784913144]}
df = DataFrame(data=d)
actual_data = []
actual_data = OWMApi.get_actual_weather_data(df['lat'][0], df['lon'][0])
df = DataFrame(actual_data).transpose()
values = df.values
values = values.astype('float32')
scaler = load('scalers/scaler-' + city[0] + '.joblib')
values_all = values[:, 0:5]
values_all = scaler.transform(values_all)
for i in range(5, 21, 5):
    values_cut = values[:, i:(i+5)]
    values_cut = scaler.transform(values_cut)
    values_all = np.concatenate([values_all, values_cut], axis=1)

values_all = values_all.reshape((values_all.shape[0], N_DAYS, N_FEATURES))
# load model from single file
model = load_model('models/lstm_model-' + city[0] + '.h5')
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

my_image = Image.open("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/map.png")
title_font = ImageFont.truetype('OrelegaOne-Regular.ttf', 50)
image_editable = ImageDraw.Draw(my_image)
image_editable.text((337, 337), "%d °C" % result, (0, 0, 0), font=title_font)
image_editable.text((200, 200), "%d °C" % result, (0, 0, 0), font=title_font)
my_image.save("result.jpg")
print(result)
