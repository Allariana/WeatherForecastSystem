from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/image/map3.png")
my_image2 = Image.open("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/image/map3a.png")
title_font = ImageFont.truetype('image/OrelegaOne-Regular.ttf', 50)
image_editable = ImageDraw.Draw(my_image)
image_editable2 = ImageDraw.Draw(my_image2)
image_editable.text((348, 240), "28 °C", (0, 0, 0), font=title_font) #warsaw
image_editable.text((319, 420), "28 °C", (0, 0, 0), font=title_font) #krakow
image_editable.text((170, 6), "24 °C", (0, 0, 0), font=title_font) #gdansk
my_image.save("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/web-app/src/main/resources/static/today.png")
image_editable2.text((348, 240), "27 °C", (0, 0, 0), font=title_font) #warsaw
image_editable2.text((319, 420), "28 °C", (0, 0, 0), font=title_font) #krakow
image_editable2.text((170, 6), "25 °C", (0, 0, 0), font=title_font) #gdansk
my_image2.save("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/web-app/src/main/resources/static/tomorrow.png")