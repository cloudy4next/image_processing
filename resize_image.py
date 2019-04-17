from PIL import Image
import os, sys

path="/home/cloudy/Desktop/Daddy/"
paths="/home/cloudy/Desktop/new/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path+ item)
            f , e = os.path.splitext(paths + item)
            resized = im.resize((1200,960),Image.ANTIALIAS)
            resized.rotate(90).save( f + 'resized.jpg',quality =90 )
resize()
