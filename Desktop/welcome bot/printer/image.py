from PIL import Image, ImageDraw, ImageFont
image = Image.open('white2.jpg')

draw = ImageDraw.Draw(image)
import os
img1 = Image.open('white.jpg', 'r').convert("RGBA")
img = Image.open('trail.jpg','r').convert("RGBA")
image.paste(img,(0,0),img)
##img1.show()
font = ImageFont.truetype('Roboto-Bold.ttf', size=30)

(x, y) = (0, 200)
message = "Happy Birthday!"
color = 'rgb(0, 0, 0)' # black color

draw.text((x, y), message, fill=color, font=font)

image.save('greeting_card.jpg')

image.show()
os.system("lpr -o fit-to-page greeting_card.jpg")
