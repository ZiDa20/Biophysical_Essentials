from PIL import ImageTk ,Image


##################################
#deprecated , should be removed --> mz
##################################
class HelperFunction():

    def __init__(self):
        self.SIZE_COL = 30
        self.SIZE_ROW = 30

    def resize(self, path):
        original_image = Image.open(path)
        image = original_image.resize((self.SIZE_COL, self.SIZE_ROW), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(image=image) 
        return img1
