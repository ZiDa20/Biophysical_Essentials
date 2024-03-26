from Frontend.OfflineAnalysis.CustomWidget.construction_side_dialog import Ui_Dialog
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtGui import QPixmap, QColor, Qt

class ConstrcutionSideDialog(QDialog, Ui_Dialog):

    def __init__(self, frontend_style, parent=None):    
        super().__init__(parent)
        self.setupUi(self)
        frontend_style.set_pop_up_dialog_style_sheet(self)
        if frontend_style.default_mode == 1:
            image_path = r":Frontend/Button/light_mode/offline_analysis/construction_white.png"  # Replace with the actual path to your PNG image
        else:
            image_path = r":Frontend/Button/dark_mode/offline_analysis/construction_dark.png"  # Replace with the actual path to your PNG image

        pixmap = QPixmap(image_path)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        self.verticalLayout.addWidget(image_label,alignment=Qt.AlignmentFlag.AlignCenter)
        self.pushButton.clicked.connect(self.close)
        self.exec()

