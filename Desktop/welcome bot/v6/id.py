from PIL import Image, ImageDraw, ImageFont
import os
while(1):
    if( os.stat("details.txt").st_size > 0 ):
        f=open("details.txt","r")
        message=f.read()
        f.close()
        f=open("details.txt","w")
        f.write("")
        f.close()
        break

img=Image.open("white.jpg")
width, height = img.size
img.resize((350,280)).save("white2.jpg")
img=Image.open("new.jpg")
width, height = img.size
img.resize((350,180)).save("trail.jpg")
image = Image.open('white2.jpg')

draw = ImageDraw.Draw(image)
img1 = Image.open('white.jpg', 'r').convert("RGBA")
img = Image.open('trail.jpg','r').convert("RGBA")
image.paste(img,(0,0),img)
##img1.show()
font = ImageFont.truetype('Roboto-Bold.ttf', size=30)

(x, y) = (0, 200)
#message = "Happy Birthday!"
color = 'rgb(0, 0, 0)' # black color

draw.text((x, y), message, fill=color, font=font)

image.save('greeting_card.jpg')

#image.show()
os.system("lpr -o portrait -o fit-to-page -P Printer greeting_card.jpg")

