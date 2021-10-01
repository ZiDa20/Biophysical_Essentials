class Frontend_Style():
    """class that will provide all the frontend styles to be used in common by all frontend classes with the same instance"""


    def __init__(self):

        # style 0 = white mode
        # style 1 = dark mode
        self.current_style = 1

        self.light_style = u"QFrame{ background-color: \"#e6e6e6\"; }\n" \
                           "QPushButton{ padding: 5px 10px; " \
                           "             border: none;" \
                           "             border-radius:10px;" \
                           "             background-color: \"#e6e6e6\";}" \
                           "QPushButton:hover{ background-color: \"#ff8117\";} " \
                           "QDialog{background-color: \"#ffffff\"; }"


        self.dark_style = u"QFrame{ background-color: \"#232629\";\ } \n" \
                          "QPushButton{ padding: 5px 10px;\ " \
                          "             border: none; " \
                          "border-radius:10px; " \
                          "background-color: \"#232629\"; } " \
                          "QPushButton:hover{ background-color: \"#54545a\";\ }"




    def get_dark_style(self):
        return self.dark_style

    def get_light_style(self):
        return self.light_style

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
