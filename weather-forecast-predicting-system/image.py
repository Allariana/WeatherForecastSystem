from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/image/map3.png")
title_font = ImageFont.truetype('image/OrelegaOne-Regular.ttf', 50)
image_editable = ImageDraw.Draw(my_image)
image_editable.text((348, 240), "13 °C", (0, 0, 0), font=title_font)
image_editable.text((319, 420), "13 °C", (0, 0, 0), font=title_font)
image_editable.text((170, 6), "16 °C", (0, 0, 0), font=title_font)
my_image.save("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/web-app/src/main/resources/static/result.png")