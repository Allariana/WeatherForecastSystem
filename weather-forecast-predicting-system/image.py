from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/map2.png")
title_font = ImageFont.truetype('OrelegaOne-Regular.ttf', 50)
image_editable = ImageDraw.Draw(my_image)
image_editable.text((350, 250), "15 °C", (0, 0, 0), font=title_font)
image_editable.text((317, 425), "15 °C", (0, 0, 0), font=title_font)
my_image.save("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/r.png")