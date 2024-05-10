# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_function_table.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(442, 730)
        Form.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 2, 0, 2)
        self.remove_functions = QPushButton(self.groupBox)
        self.remove_functions.setObjectName(u"remove_functions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.remove_functions.sizePolicy().hasHeightForWidth())
        self.remove_functions.setSizePolicy(sizePolicy1)
        self.remove_functions.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.remove_functions, 1, 0, 1, 1)

        self.normalization_combo_box = QComboBox(self.groupBox)
        icon = QIcon()
        icon.addFile(u"../../../../../../../Biophysical_Essentials/QT_GUI/Button/dark_mode/offline_analysis/edit_meta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.normalization_combo_box.addItem(icon, "")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.setObjectName(u"normalization_combo_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.normalization_combo_box.sizePolicy().hasHeightForWidth())
        self.normalization_combo_box.setSizePolicy(sizePolicy2)
        self.normalization_combo_box.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.normalization_combo_box, 0, 0, 1, 1)

        self.analysis_stacked_widget = QTabWidget(self.groupBox)
        self.analysis_stacked_widget.setObjectName(u"analysis_stacked_widget")
        self.analysis_stacked_widget.setTabPosition(QTabWidget.East)
        self.analysis_stacked_widget.setTabsClosable(True)

        self.gridLayout_9.addWidget(self.analysis_stacked_widget, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)


        self.retranslateUi(Form)

        self.analysis_stacked_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Analysis Selector", None))
        self.remove_functions.setText(QCoreApplication.translate("Form", u"Remove Cursor Bounds", None))
        self.normalization_combo_box.setItemText(0, QCoreApplication.translate("Form", u"CSlow Auto Normlization", None))
        self.normalization_combo_box.setItemText(1, QCoreApplication.translate("Form", u"CSlow Manual Normalization", None))
        self.normalization_combo_box.setItemText(2, QCoreApplication.translate("Form", u"Other", None))

        self.normalization_combo_box.setCurrentText(QCoreApplication.translate("Form", u"CSlow Auto Normlization", None))
    # retranslateUi

