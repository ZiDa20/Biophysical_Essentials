import sys
import os
sys.path.append(os.getcwd()[:-3] + "QT_GUI")
import pandas as pd 
#from start import *
from tkinter_camera import * 
from settings_window import Ui_Settings
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from functools import partial

class SettingsWindow(QWidget,Ui_Settings):
    def __init__(self,parent = None):
        self.parent = parent
        QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.default_mode = MainWindow().get_darkmode()
        #self.switch_modes(self.default_mode)

        settings_buttons = [self.Set_default_user, self.initialize_devices, self.plot_appearance, self.save_location, self.connect_to_webserver]
        for index, button in enumerate(settings_buttons):
            button.clicked.connect(partial(self.stackedWidget_4.setCurrentIndex, index))
        self.pushButton_13.clicked.connect(self.initialize_camera)
    

    def switch_modes(self, default_mode):
        with open('Menu_button.css') as file:
            self.setStyleSheet(self.start.styleSheet() +file.read().format(**os.environ))


    def initialize_camera(self):
        """ Basler camera initalizing  
        ToDO: Error handling, add multiple camera possibilites for capturing in the dropdown menu"""

        print("stuff worked")
        self.camera = BayerCamera()
        #initialize the camera 
        camera_status = self.camera.init_camera()
        self.scence_trial = QGraphicsScene(self) # generate a graphics scence in which the image can be putted
        if camera_status is None: # initialization of the camera and error response if not correctly initialized
            print("Camera is working")
        else:
            print("Camera is connected")


    def quit(self):
        self.close()
    


    

