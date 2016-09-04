import math
from PIL import Image, ImageChops


def norm(*args) :
    return math.sqrt(sum([a*a for a in args]))


class ImageDifference() :
    def __init__(self, img_data1, img_data2):
        self.img_data1 = img_data1
        self.img_data2 = img_data2

        self.img1 = Image.open(self.img_data1)
        self.img2 = Image.open(self.img_data2)

    def difference(self, f_name=None):
        chop = ImageChops.difference(self.img1, self.img2)
        if f_name is not None :
            chop.save('test.jpg', 'JPEG')

        px_data = chop.load()
        width, height = chop.size
        rms = sum([norm(*px_data[x,y]) for x in range(width) for y in range(height)])/float(width*height)

        return rms




