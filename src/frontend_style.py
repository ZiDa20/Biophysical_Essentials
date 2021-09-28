class Frontend_Style():

    def __init__(self):
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

