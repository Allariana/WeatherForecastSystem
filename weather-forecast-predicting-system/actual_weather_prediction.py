import OWMApi
from keras.models import load_model
from joblib import load
from pandas import DataFrame
import numpy as np
from numpy import concatenate
from PIL import Image, ImageFont, ImageDraw
from constants import *

city = ['warsaw', 'KRAKÓW-OBSERWATORIUM', 'BORUCINO']
d = {'lat': [52.29958465640118, 50.0649722906938, 54.36538821401951],
     'lon': [20.927704121901673, 19.988522784913144, 18.592691014184325],
     'x': [348, 319, 170], 'y': [240, 420, 6]}
df2 = DataFrame(data=d)

my_image = Image.open("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/"
                      "weather-forecast-predicting-system/image/map3.png")
title_font = ImageFont.truetype('image/OrelegaOne-Regular.ttf', 50)
image_editable = ImageDraw.Draw(my_image)

for j in range(0, 3):
    actual_data = []
    actual_data = OWMApi.get_actual_weather_data(df2['lat'][j], df2['lon'][j])
    df = DataFrame(actual_data).transpose()
    values = df.values
    values = values.astype('float32')
    scaler = load('scalers/scaler-' + city[j] + '.joblib')
    values_all = values[:, 0:5]
    values_all = scaler.transform(values_all)
    for i in range(5, 21, 5):
        values_cut = values[:, i:(i+5)]
        values_cut = scaler.transform(values_cut)
        values_all = np.concatenate([values_all, values_cut], axis=1)

    values_all = values_all.reshape((values_all.shape[0], N_DAYS, N_FEATURES))
    # load model from single file
    model = load_model('models/lstm_model-' + city[j] + '.h5')
    # make predictions
    yhat = model.predict(values_all)
    values_all = values_all.reshape((values_all.shape[0], N_DAYS*N_FEATURES))
    # invert scaling for forecast
    inv_yhat = concatenate((yhat, values_all[:, -(N_FEATURES-1):]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:, 0]
    result = int(round(inv_yhat[0]))
    print(result)
    image_editable.text((df2['x'][j], df2['y'][j]), "%d °C" % result, (0, 0, 0), font=title_font)

my_image.save("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/web-app/src/main/resources/static/result.png")

# f = open("result.txt", "w+")
# f.write("%d" % result)
# f.close()

