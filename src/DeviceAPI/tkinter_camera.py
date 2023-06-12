from pypylon import pylon
#Switched to pyqt
from typing import Optional, Union
import numpy as np

class BayerCamera():
    """_summary_: This is the BaslerCamera Loader Module
    """

    def __init__(self):
        """ establish the connection to the camera"""
        self.camera: Optional[] = None
        self.cancel = None


    def init_camera(self) -> Optional[bool]:
        """Initalize the Bayer Cameras
        Here additional interface should be added

        Returns:
            bool: If True Camera is connected properly
        """
        try:
            #self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            #self.camera.Open()
            return True
        except Exception:
            return None

    def grab_video(self) -> Union[None, np.ndarray]:
        """Get the Picture 1 frame a time

        Returns:
            self.img: if image taken should be returned and shown
            else None is returned
        """

        NUMBER: int = 1
        self.camera.StartGrabbingMax(NUMBER)

        self.grabResult = self.camera.RetrieveResult(6000, pylon.TimeoutHandling_ThrowException)

        if not self.grabResult.GrabSucceeded():
            return None

        self.img = self.grabResult.Array
        return self.img

    def save_fig(self) -> None:
        """
        Should set the last taken image into the online analysis for furture use
        and savefig options """
        #save the image into the class
        self.online_analysis.image_labbook = self.img
        #plt.savefig(bm.set_batch_path())

