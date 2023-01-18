#from pypylon import pylon
import matplotlib.pyplot as plt
from pypylon import pylon
#Switched to pyqt

class BayerCamera():

    def __init__(self):
        """ establish the connection to the camera"""
        self.camera = None
        self.cancel = None
    

    def init_camera(self):
        """Initalize the Bayer Cameras 
        Here additional interface should be added

        Returns:
            bool: If True Camera is connected properly
        """
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()
            return True
        except:
            return None
   
    def grab_video(self):
        """Get the Picture 1 frame a time

        Returns:
            self.img: if image taken should be returned and shown
            else None is returned
        """
        
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
        """""" 
        fig, ax = plt.subplots(figsize = (10,10))
        plt.imshow(self.img)
        #save the image into the class 
        self.online_analysis.image_labbook = self.img
        #plt.savefig(bm.set_batch_path())

