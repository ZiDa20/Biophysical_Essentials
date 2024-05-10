from pypylon import pylon
from typing import Optional, Union
import numpy as np
import picologging

NUMBER: int = 1

class BayerCamera():
    """_summary_: This is the BaslerCamera Loader Module
    """

    def __init__(self):
        """ establish the connection to the camera"""
        self.logger = picologging.getLogger(__name__)
        self.camera: Optional[pylon.InstantCamera] = None
        self.online_analysis = None
        self._cancel = None

    @property
    def cancel(self):
        """Getter for cancel property

        Returns:
            Optional[bool]: returns the cancel property
        """
        return self._cancel
    
    @cancel.setter
    def cancel(self, value):
        self._cancel = value

    def init_camera(self) -> Optional[bool]:
        """Initalize the Bayer Cameras
        Here additional interface should be added

        Returns:
            bool: If True Camera is connected properly
        """
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()
            self.logger.info("Camera connected")
            return True
        except Exception:
            self.logger.error("Camera not connected, failed connection process")
            return None

    def grab_video(self) -> Union[None, np.ndarray]:
        """Get the Picture 1 frame a time

        Returns:
            self.img: if image taken should be returned and shown
            else None is returned
        """
        self.camera.StartGrabbingMax(NUMBER)
        grabResult = self.camera.RetrieveResult(6000, pylon.TimeoutHandling_ThrowException)
        if not grabResult.GrabSucceeded():
            return None
        img = grabResult.Array
        return img

    def save_fig(self) -> None:
        """
        Should set the last taken image into the online analysis for furture use
        and savefig options """
        #save the image into the class
        self.online_analysis.image_labbook = self.img
        #plt.savefig(bm.set_batch_path())

