#from pypylon import pylon
from PySide6.QtCore import QThread

#Switched to pyqt

class BayerCamera():

    def __init__(self):

        """ establish the connection to the camera"""
        self.camera = None
        self.cancel = None
        #self.online_analysis = online_analysis


    def init_camera(self):
        # initialize the camera
        try:
            #self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            #self.camera.Open()
            print("hello")
            return True
        except:
            print("returndd none")
            return None
   
    def grab_video(self):
        # Connect to camera and get the image
        
        NUMBER = 1
        self.camera.StartGrabbingMax(NUMBER)

        self.grabResult = self.camera.RetrieveResult(6000, pylon.TimeoutHandling_ThrowException)
       
        if self.grabResult.GrabSucceeded():
            self.img = self.grabResult.Array
            return self.img
            

        else:
            return None

        self.grabResult.Release()

        self.camera.Close()

    def save_fig(self, bm):
        """ save the drawed figure """        
        fig, ax = plt.subplots(figsize = (10,10))
        plt.imshow(self.img)
        #save the image into the class 
        self.online_analysis.image_labbook = self.img
        #plt.savefig(bm.set_batch_path())

