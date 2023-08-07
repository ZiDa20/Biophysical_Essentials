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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(465, 739)
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
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 2, 0, 2)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.select_series_analysis_functions = QPushButton(self.groupBox)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy1)
        self.select_series_analysis_functions.setMinimumSize(QSize(0, 0))
        self.select_series_analysis_functions.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.select_series_analysis_functions, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.normalization_combo_box = QComboBox(self.groupBox)
        icon = QIcon()
        icon.addFile(u"../QT_GUI/Button/dark_mode/offline_analysis/light_series.png", QSize(), QIcon.Normal, QIcon.Off)
        self.normalization_combo_box.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u"../QT_GUI/Button/dark_mode/offline_analysis/edit_meta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.normalization_combo_box.addItem(icon1, "")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.addItem("")
        self.normalization_combo_box.setObjectName(u"normalization_combo_box")
        self.normalization_combo_box.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.normalization_combo_box, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.analysis_stacked_widget = QTabWidget(self.groupBox)
        self.analysis_stacked_widget.setObjectName(u"analysis_stacked_widget")
        self.analysis_stacked_widget.setTabPosition(QTabWidget.East)
        self.analysis_stacked_widget.setTabsClosable(True)

        self.gridLayout_9.addWidget(self.analysis_stacked_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)


        self.retranslateUi(Form)

        self.analysis_stacked_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Analysis Selector", None))
#if QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setAccessibleName(QCoreApplication.translate("Form", u"analysis_grid_bt", None))
#endif // QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setText(QCoreApplication.translate("Form", u"S", None))
        self.normalization_combo_box.setItemText(0, QCoreApplication.translate("Form", u"Norm", None))
        self.normalization_combo_box.setItemText(1, QCoreApplication.translate("Form", u"CSlow Auto", None))
        self.normalization_combo_box.setItemText(2, QCoreApplication.translate("Form", u"CSlow Manual", None))
        self.normalization_combo_box.setItemText(3, QCoreApplication.translate("Form", u"Configure", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"Remove Cursor Bounds", None))
    # retranslateUi

