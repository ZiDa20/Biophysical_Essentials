import os
from qbstyles import mpl_style
import matplotlib as mpl

class Frontend_Style():
    """class that will provide all the frontend styles to be used in common by all frontend classes with the same instance"""

    def __init__(self, app):

        # style 0 = white mode
        # style 1 = dark mode
        self.canvas = []
        self.app = app
        self.ax = []
        self._default_mode = 0
        self.change_to_lightmode()

    @property
    def default_mode(self):
        "returns the darkmode state"
        return self._default_mode

    @default_mode.setter
    def default_mode(self, mode: bool):
        """Darkmode/Lightmode setter

        Args:
            default_mode (int): 0 or 1 for dark or light mode
        """
        self._default_mode = mode

    def set_pop_up_dialog_style_sheet(self,dialog):
        '''
        According to the global value of self.theme_mode the correct style sheet for a given popup dialog will be set.
        :param popup_dialog: dialog object which stylesheet will be set
        :return:
        '''
        if self.default_mode == 0:
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button.css") as file:
                dialog.setStyleSheet(file.read().format(**os.environ))

        else:
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                dialog.setStyleSheet(file.read().format(**os.environ))

    def get_color_plots(self):
        return "black" if self.default_mode == 1 else "white"

    def set_mpl_style_dark(self):
        """Set the correct matplotlib dark style
        """
        mpl_style(True)
        mpl.rcParams["figure.facecolor"] = "#121212"
        mpl.rcParams["axes.facecolor"] = "#1f2933"

    def set_mpl_style_white(self):
        """Set the correct matplotlib style white mode
        """
        mpl_style(False)
        mpl.rcParams["figure.facecolor"] = "#ffffff"
        mpl.rcParams["axes.facecolor"] = "#ffffff"

    def change_to_lightmode(self):
        """DarkMode LightMode Switch
        """

        if self.default_mode == 1:
            self.default_mode = 0
            self.app.apply_stylesheet(self.app, 'dark_mode.xml', invert_secondary=False)
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button.css") as file:
                self.app.setStyleSheet(self.app.styleSheet() +file.read().format(**os.environ))

        else:
            self.default_mode = 1 # set the darkmode back to 1 for the switch
            self.app.apply_stylesheet(self.app, f"{os.getcwd()}/StyleFrontend/white_mode.xml", invert_secondary=False)
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                self.app.setStyleSheet(self.app.styleSheet() +file.read().format(**os.environ))



