from QT_GUI.OfflineAnalysis.CustomWidget.construction_side_dialog import Ui_Dialog
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtGui import QPixmap, QColor, Qt

class ConstrcutionSideDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):    
        super().__init__(parent)
        self.setupUi(self)

        image_path = r"..\QT_GUI\Button\light_mode\offline_analysis\construction.png"  # Replace with the actual path to your PNG image
        pixmap = QPixmap(image_path)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        self.verticalLayout.addWidget(image_label,alignment=Qt.AlignmentFlag.AlignCenter)
        self.pushButton.clicked.connect(self.close)
        self.exec()

