from PIL import Image, ImageDraw, ImageFont
import os
def done():
    try:
        img2 = Image.open("new.jpg")
        img = Image.open("white1.jpg")
        print(img.size)
        img.paste(img2,(220,35))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('/home/pi/Desktop/welcome bot/printer/Roboto-Bold.ttf',size=100)
        (x,y)=(100,50)
        (x1,y1)=(100,55)
        z=open("details",'r')
        bit=z.read()
        message = bit
        print(message)
        color = 'rgb(0,0,0)'
        draw.text((x,y), "\n", fill=color, font=font)
        
        draw.text((x,y), message, fill=color, font=font)
        img.save("idcard.jpg")
        os.system("lpr -o fit-to-page -P Usb-Printer idcard.jpg")
        print("done")
    except IOError:
        print(IOError)
        pass
    print("done")
