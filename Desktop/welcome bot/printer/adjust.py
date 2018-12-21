from PIL import Image

def scale_and_resize():
    img=Image.open("white.jpg")
    width, height = img.size
    img.resize((350,250)).save("white2.jpg")

if __name__ == '__main__':
    scale_and_resize()
