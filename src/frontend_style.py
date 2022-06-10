class Frontend_Style():
    """class that will provide all the frontend styles to be used in common by all frontend classes with the same instance"""


    def __init__(self):

        # style 0 = white mode
        # style 1 = dark mode
        self.current_style = 1

        self.sideframe_light_style = u"QWidget{background-color: \"#e6e6e6\";}\n" \
                                "QPushButton{padding: 10px 10px;"\
                                "	        border: none;" \
                                "	        border-radius:5px;" \
                                "	        background-color: \"#e6e6e6\";}"\
                                "QPushButton:hover{background-color: \"#54545a\";}"


        self.sideframe_dark_style = u"QWidget{background-color: \"#232629\";}\n" \
                                "QPushButton{padding: 10px 10px;"\
                                "	        padding-left: 20px;" \
                                "	        border: none;" \
                                "	        border-radius:5px;" \
                                "	        background-color: \"#232629\";}"\
                                "QPushButton:hover{background-color: \"#54545a\";}"
                                  
                                  
        self.light_style = u"QWidget{ background-color: \"#e6e6e6\"; }\n" \
                           "QPushButton{ padding: 10px 10px; " \
                           "             border None ;" \
                           "             border-radius:5px;" \
                           "             color:#2986cc; " \
                           "             background-color: \"#e6e6e6\";}" \
                           "QPushButton:hover{ background-color: \"#2986cc\";} " \
                           "QDialog{background-color: \"#ffffff\"; }"


        self.dark_style = u"QWidget{ background-color: \"#232629\";\ } \n" \
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
    
    def get_sideframe_light(self):
        return self.sideframe_light_style

    def get_sideframe_dark(self):
        return self.sideframe_dark_style

    def set_pop_up_dialog_style_sheet(self,dialog):
        '''
        According to the global value of self.theme_mode the correct style sheet for a given popup dialog will be set.
        :param popup_dialog: dialog object which stylesheet will be set
        :return:
        '''
        if self.current_style == 0:
            dialog.setStyleSheet(self.light_style)
        else:
            dialog.setStyleSheet(self.dark_style)
