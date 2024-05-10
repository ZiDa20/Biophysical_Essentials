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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

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
        self.analysis_stacked_widget = QStackedWidget(self.groupBox)
        self.analysis_stacked_widget.setObjectName(u"analysis_stacked_widget")
        self.analysis_stacked_widget.setEnabled(True)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.analysis_stacked_widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.analysis_stacked_widget.addWidget(self.page_4)

        self.analysi_grid.addWidget(self.analysis_stacked_widget, 0, 0, 1, 1)

        self.analysis_button_grid = QGridLayout()
        self.analysis_button_grid.setObjectName(u"analysis_button_grid")
        self.select_series_analysis_functions = QPushButton(self.groupBox)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy1)
        self.select_series_analysis_functions.setMinimumSize(QSize(150, 150))
        self.select_series_analysis_functions.setMaximumSize(QSize(150, 150))

        self.analysis_button_grid.addWidget(self.select_series_analysis_functions, 2, 0, 1, 1)


        self.analysi_grid.addLayout(self.analysis_button_grid, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.analysi_grid, 1, 0, 1, 1)

        self.normalization_group_box = QGroupBox(self.groupBox)
        self.normalization_group_box.setObjectName(u"normalization_group_box")
        self.normalization_group_box.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_30 = QGridLayout(self.normalization_group_box)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.normalization_combo_box = QComboBox(self.normalization_group_box)
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.setObjectName(u"normalization_combo_box")

        self.gridLayout_30.addWidget(self.normalization_combo_box, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.normalization_group_box, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Analysis", None))
#if QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setAccessibleName(QCoreApplication.translate("Form", u"analysis_grid_bt", None))
#endif // QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setText(QCoreApplication.translate("Form", u"+", None))
        self.normalization_group_box.setTitle(QCoreApplication.translate("Form", u"Normalization", None))
        self.normalization_combo_box.setItemText(0, QCoreApplication.translate("Form", u"CSlow Auto", None))
        self.normalization_combo_box.setItemText(1, QCoreApplication.translate("Form", u"CSlow Manual", None))
        self.normalization_combo_box.setItemText(2, QCoreApplication.translate("Form", u"Configure", None))

    # retranslateUi

