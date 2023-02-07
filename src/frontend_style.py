import os 
from qbstyles import mpl_style
import matplotlib as mpl

class Frontend_Style():
    """class that will provide all the frontend styles to be used in common by all frontend classes with the same instance"""

    def __init__(self):

        # style 0 = white mode
        # style 1 = dark mode
        self.canvas = []
        self.ax = []
        self.current_style = 1                                                              
                                  
        self.light_style = None

        self.dark_style = u"QWidget{ background-color: rgba(4,7,26, 200);\ } \n" \
                           "QPushButton{ padding: 5px 10px; " \
                           "             border-width: 0px ;" \
                           "             border-radius: 10px ; " \
                           "             border-color: #fff5cc;"\
                           "             border-radius:10px;" \
                           "             color:white; " \
                           "             background-color: #151E3D;}" \
                           "QPushButton:hover{ background-color: \"#e6e6e6\";} " \
                           "QPushButton[accessibleName=\"big_square\"] {min-width: 10em;" \
                           "              min-height: 10em;}" \
                          "QLabel{background-color: rgba(0,0,0,0%);}" \
                          "QComboBox{selection-color: #151E3D; selection-background-color: #151E3D; background= #151E3D; " \
                          "color=#151E3D;}" \

    def get_dark_style(self):
        return self.dark_style

    def get_light_style(self):
        return self.light_style

    def get_sideframe_dark(self):
        return self.sideframe_dark_style

    def set_pop_up_dialog_style_sheet(self,dialog):
        '''
        According to the global value of self.theme_mode the correct style sheet for a given popup dialog will be set.
        :param popup_dialog: dialog object which stylesheet will be set
        :return:
        '''
        if self.current_style == 0:
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button.css") as file:
                dialog.setStyleSheet(file.read().format(**os.environ))

        else:
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                dialog.setStyleSheet(file.read().format(**os.environ))
            
                    
    def get_color_plots(self):
        return "black" if self.current_style == 1 else "white"
        

    def set_mpl_style_dark(self):
        mpl_style(True)
        mpl.rcParams["figure.facecolor"] = "#121212"
        mpl.rcParams["axes.facecolor"] = "#1f2933"


    def set_mpl_style_white(self):
        mpl_style(False)
        mpl.rcParams["figure.facecolor"] = "#ffffff"
        mpl.rcParams["axes.facecolor"] = "#ffffff"
