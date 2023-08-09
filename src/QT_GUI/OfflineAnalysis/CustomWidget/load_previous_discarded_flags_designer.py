# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_previous_data_selection_dialog.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(955, 605)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(10)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QSize(16777215, 25))
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_4.addWidget(self.comboBox, 1, 0, 1, 1)

        self.id_to_show = QLabel(self.groupBox_3)
        self.id_to_show.setObjectName(u"id_to_show")
        self.id_to_show.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.id_to_show, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(10)

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.selected_data_treeview = QTreeView(self.groupBox)
        self.selected_data_treeview.setObjectName(u"selected_data_treeview")
        self.selected_data_treeview.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.selected_data_treeview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.discarded_data_treeview = QTreeView(self.groupBox_2)
        self.discarded_data_treeview.setObjectName(u"discarded_data_treeview")
        self.discarded_data_treeview.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.discarded_data_treeview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.apply_selection = QPushButton(Dialog)
        self.apply_selection.setObjectName(u"apply_selection")

        self.horizontalLayout.addWidget(self.apply_selection)

        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Load Discarded Flags", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"In the dropdown below, select the Analysis ID you would like to load the information about discarded data from !", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Select", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Default", None))

        self.id_to_show.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Current Analysis ID", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Previous Analysis", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Data Preview", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Selected Data", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Discarded Data", None))
        self.apply_selection.setText(QCoreApplication.translate("Dialog", u"Apply Selection", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

