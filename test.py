from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Такого файлу не існує!")
        self.original.show()

    def mirror(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)


        temp_filename = self.filename.split(".")
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        

        rotated.save(new_filename)

    def crop(self):
        box = (25,10,60,40)
        cropped = self.original.crop(box)

        temp_filename = self.filename.split(".")
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        
        cropped.save(new_filename)

MyImage = ImageEditor("text2.jpg")
MyImage.open()

MyImage.mirror()
MyImage.crop()

for im in MyImage.changed:
    im.show()

      




    
