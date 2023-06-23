# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_function_table.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(468, 801)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.analysi_grid = QGridLayout()
        self.analysi_grid.setObjectName(u"analysi_grid")
        self.analysis_stacked_widget = QTabWidget(self.groupBox)
        self.analysis_stacked_widget.setObjectName(u"analysis_stacked_widget")
        self.analysis_stacked_widget.setTabPosition(QTabWidget.East)

        self.analysi_grid.addWidget(self.analysis_stacked_widget, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.analysi_grid, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.select_series_analysis_functions = QPushButton(self.groupBox)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy1)
        self.select_series_analysis_functions.setMinimumSize(QSize(0, 0))
        self.select_series_analysis_functions.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.select_series_analysis_functions, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.normalization_combo_box = QComboBox(self.groupBox)
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.setObjectName(u"normalization_combo_box")

        self.gridLayout_2.addWidget(self.normalization_combo_box, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.button_grid = QGridLayout()
        self.button_grid.setObjectName(u"button_grid")

        self.gridLayout_9.addLayout(self.button_grid, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.analysis_stacked_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Analysis", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"How to normalize", None))
#if QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setAccessibleName(QCoreApplication.translate("Form", u"analysis_grid_bt", None))
#endif // QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setText(QCoreApplication.translate("Form", u"Analysis Function", None))
        self.label.setText(QCoreApplication.translate("Form", u"Select the Analysis Function", None))
        self.normalization_combo_box.setItemText(0, QCoreApplication.translate("Form", u"CSlow Auto", None))
        self.normalization_combo_box.setItemText(1, QCoreApplication.translate("Form", u"CSlow Manual", None))
        self.normalization_combo_box.setItemText(2, QCoreApplication.translate("Form", u"Configure", None))

        self.checkBox.setText(QCoreApplication.translate("Form", u"On", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Cursor Bounds", None))
    # retranslateUi

