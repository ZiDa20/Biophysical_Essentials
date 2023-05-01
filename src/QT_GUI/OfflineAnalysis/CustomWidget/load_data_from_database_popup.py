# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_data_from_database_popup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1181, 786)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.load_data = QPushButton(Dialog)
        self.load_data.setObjectName(u"load_data")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_data.sizePolicy().hasHeightForWidth())
        self.load_data.setSizePolicy(sizePolicy)
        self.load_data.setMaximumSize(QSize(400, 40))

        self.gridLayout.addWidget(self.load_data, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QSize(400, 16777215))
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_5 = QGridLayout(self.page_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.available_labels = QGroupBox(self.page_7)
        self.available_labels.setObjectName(u"available_labels")
        sizePolicy.setHeightForWidth(self.available_labels.sizePolicy().hasHeightForWidth())
        self.available_labels.setSizePolicy(sizePolicy)
        self.available_labels.setMaximumSize(QSize(400, 16777215))
        self.available_labels.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.available_labels)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_grid = QGridLayout()
        self.label_grid.setObjectName(u"label_grid")

        self.gridLayout_2.addLayout(self.label_grid, 1, 0, 1, 1)

        self.category = QComboBox(self.available_labels)
        self.category.setObjectName(u"category")

        self.gridLayout_2.addWidget(self.category, 0, 0, 1, 1)

        self.switch_to_manual = QPushButton(self.available_labels)
        self.switch_to_manual.setObjectName(u"switch_to_manual")

        self.gridLayout_2.addWidget(self.switch_to_manual, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.available_labels, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_7 = QGridLayout(self.page_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox = QGroupBox(self.page_8)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.query_input = QTextEdit(self.groupBox)
        self.query_input.setObjectName(u"query_input")
        self.query_input.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_8.addWidget(self.query_input, 0, 0, 1, 1)

        self.execute_query = QPushButton(self.groupBox)
        self.execute_query.setObjectName(u"execute_query")

        self.gridLayout_8.addWidget(self.execute_query, 1, 0, 1, 1)

        self.query_output = QLineEdit(self.groupBox)
        self.query_output.setObjectName(u"query_output")

        self.gridLayout_8.addWidget(self.query_output, 2, 0, 1, 1)

        self.switch_to_auto = QPushButton(self.groupBox)
        self.switch_to_auto.setObjectName(u"switch_to_auto")

        self.gridLayout_8.addWidget(self.switch_to_auto, 3, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8)

        self.gridLayout.addWidget(self.stackedWidget, 4, 0, 1, 1)

        self.stackedWidget_2 = QStackedWidget(Dialog)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_6 = QGridLayout(self.page_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_3 = QGroupBox(self.page_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.diagram_grid = QGridLayout()
        self.diagram_grid.setObjectName(u"diagram_grid")

        self.gridLayout_4.addLayout(self.diagram_grid, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_9 = QGridLayout(self.page_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_2 = QGroupBox(self.page_10)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_11 = QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.gridLayout_9.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_10)

        self.gridLayout.addWidget(self.stackedWidget_2, 4, 2, 3, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.load_data.setText(QCoreApplication.translate("Dialog", u"Load Selection", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Descriptive Statistics and Experiment Selection", None))
        self.available_labels.setTitle(QCoreApplication.translate("Dialog", u"Available Data", None))
        self.switch_to_manual.setText(QCoreApplication.translate("Dialog", u"Switch To Manual Selection", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Data Query", None))
        self.query_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Input your SQL Query Here", None))
        self.execute_query.setText(QCoreApplication.translate("Dialog", u"Execute Query", None))
        self.switch_to_auto.setText(QCoreApplication.translate("Dialog", u"Switch To Automatic Selection", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Descriptive Statistics", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Requested Data", None))
    # retranslateUi