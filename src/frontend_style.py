import os 


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
            with open(os.getcwd() + "/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                dialog.setStyleSheet(file.read().format(**os.environ))

        else:
            dialog.setStyleSheet(self.dark_style)
                    
    def change_canvas_bright(self):
        """Changes the Appearance of the Plots generate in the OfflineAnalysis
        in the OfflinePlot Class 
        """
        if len(self.ax) > 0:
            for ax in self.ax:
                ax.spines['bottom'].set_color('black')
                ax.spines['left'].set_color('black') 
                ax.xaxis.label.set_color('black')
                ax.yaxis.label.set_color('black')
                ax.tick_params(axis='x', colors='black')
                ax.tick_params(axis='y', colors='black')
               
        
    def change_canvas_dark(self):  
        """Changes the Appearance of the Plots generate in the OfflineAnalysis
        in the OfflinePlot Class 
        """
        if len(self.ax) > 0:
            for ax in self.ax: # loops thorough each individual plot in the axis
                ax.spines['bottom'].set_color('white')
                ax.spines['left'].set_color('white') 
                ax.xaxis.label.set_color('white')
                ax.yaxis.label.set_color('white')
                ax.tick_params(axis='x', colors='white') 
                ax.tick_params(axis='y', colors='white')
                
    def get_color_plots(self):
        if self.current_style == 1:
            return "white"
        else:
            return "black"        
        
