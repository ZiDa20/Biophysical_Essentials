from PIL import ImageQt ,Image
import picologging
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class CameraHandler:
    def __init__(self, camera):
        self.camera = camera
        self.logger: picologging.Logger = picologging.getLogger(__name__)
        self.scence_trial = QGraphicsScene()
        self.image_list: list = []
        self._image_count: int = 0

    @property
    def image_count(self) -> int:
        """ return the image count"""
        return self._image_count

    @image_count.setter
    def image_count(self, value: int) -> None:
        """ set the image count"""
        self._image_count = value

    def check_camera_availability(self) -> bool:
        """ Basler camera initalizing
        ToDO: Error handling"""
        self.logger.info("Camera will be initialized") # log the event
        return self.camera.init_camera() # initialize the camera
#
    def start_camera_timer(self) -> None:
        """ added the asnychronous Qtimer for the Camera initalizion"""
        try:
            self.start_cam = QTimer() # create a timer
            self.start_cam.timeout.connect(self.start_camera) # connect the timer to the start camera function
            self.start_cam.start(33) # start the timer with a time interval of 222 ms
            self.logger.info("Qthread for Camera caption is running")
        except Exception as e:
            self.logger.error(f"Here is the Error description of the camera running task: {e}")

    def start_camera(self) -> None:
        """ grab the current picture one by one with 50 FPS """
        camera_image = self.camera.grab_video() # grab video retrieved np.array image
        self._image_count += 1 # increment the image count
        imgs = Image.fromarray(camera_image) # conversion
        image = imgs.resize((451,300), Image.ANTIALIAS) # resizing to be of appropriate size for the window
        imgqt = ImageQt.ImageQt(image) # convert to qt image
        camera_image_recording = QPixmap.fromImage(imgqt) # convert to qt pixmap
        self.scence_trial.clear()   # clear the scene
        self.scence_trial.addPixmap(self.camera_image_recording)

        if self.image_count % 10 == 0:
            self.append_image(camera_image_recording)

        return self.scence_trial

    def stop_camera(self):
        """ Stopping the Qthread for the Camera """
        # this should be the checkif the camera stopped afer clicking the button
        # button should be connected to this function
        try:
            self.start_cam.stop() # here the camera Qtimer is stopped
            self.logger("Camera Thread is stopped")
            return True
        except Exception as e:
            self.logger.error(f"Here is the Error description of the camera stopping task: {e}")
            return False


    def append_image(self, imgs):
        """ draw the video in the live feed
        args:
            imgs type: numpy array  of the current image
        """
        self.logger.info("Append image to to list")
        self.image_list.append(imgs)