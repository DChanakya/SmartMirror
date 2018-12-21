from PIL import Image, ImageDraw, ImageFont
from sending import demo
try:
    img2 = Image.open("/home/pi/Desktop/welcome bot/v5/new.jpg")
    img = Image.open("/home/pi/Desktop/welcome bot/v5/print.jpg")
    img.paste(img2,(220,35))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/home/pi/Desktop/welcomebot/Roboto-Bold.ttf',size=30)
    (x,y)=(100,50)
    message = demo()
    color = 'rgb(0,0,0)'
    draw.text((x,y), message, fill=color, font=font)
    img.save("niceone.jpg")
    print("done")
except IOError:
    print(IOError)
    pass
print("done")
