from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

from QT_GUI.OfflineAnalysis.CustomWidget.analysis_function_table_designer import Ui_Form

class Analysis_Function_Table(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.analysis_stacked_widget.hide()
        self.remove_functions.hide()
        #add this to promote

  