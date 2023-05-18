# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_existing_analysis_popup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)

class Ui_MetadataPopup(object):
    def setupUi(self, MetadataPopup):
        if not MetadataPopup.objectName():
            MetadataPopup.setObjectName(u"MetadataPopup")
        MetadataPopup.setWindowModality(Qt.NonModal)
        MetadataPopup.resize(1130, 772)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MetadataPopup.sizePolicy().hasHeightForWidth())
        MetadataPopup.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(MetadataPopup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.popup_stacked = QStackedWidget(MetadataPopup)
        self.popup_stacked.setObjectName(u"popup_stacked")
        self.LoadAnalysis = QWidget()
        self.LoadAnalysis.setObjectName(u"LoadAnalysis")
        self.gridLayout = QGridLayout(self.LoadAnalysis)
        self.gridLayout.setObjectName(u"gridLayout")
        self.metadata_all = QGridLayout()
        self.metadata_all.setObjectName(u"metadata_all")
        self.line_3 = QFrame(self.LoadAnalysis)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.metadata_all.addWidget(self.line_3, 2, 0, 1, 1)

        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")
        self.groupBox = QGroupBox(self.LoadAnalysis)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.final_table_layout = QGridLayout()
        self.final_table_layout.setObjectName(u"final_table_layout")

        self.gridLayout_7.addLayout(self.final_table_layout, 0, 0, 1, 1)


        self.table_layout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.metadata_all.addLayout(self.table_layout, 3, 0, 1, 1)

        self.button_layout = QGridLayout()
        self.button_layout.setObjectName(u"button_layout")

        self.metadata_all.addLayout(self.button_layout, 3, 1, 1, 1)

        self.line_4 = QFrame(self.LoadAnalysis)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.metadata_all.addWidget(self.line_4, 0, 0, 1, 1)

        self.popup_frame = QFrame(self.LoadAnalysis)
        self.popup_frame.setObjectName(u"popup_frame")
        self.popup_frame.setFrameShape(QFrame.StyledPanel)
        self.popup_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.popup_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.popup_frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.submit = QPushButton(self.popup_frame)
        self.submit.setObjectName(u"submit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy1)
        self.submit.setMinimumSize(QSize(120, 0))
        self.submit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.submit, 0, 6, 1, 1)

        self.line = QFrame(self.popup_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 0, 2, 1, 1)

        self.OfflineAnalysisID = QComboBox(self.popup_frame)
        self.OfflineAnalysisID.setObjectName(u"OfflineAnalysisID")

        self.gridLayout_4.addWidget(self.OfflineAnalysisID, 0, 4, 1, 1)

        self.label_6 = QLabel(self.popup_frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 3, 1, 1)

        self.SelectDB = QPushButton(self.popup_frame)
        self.SelectDB.setObjectName(u"SelectDB")

        self.gridLayout_4.addWidget(self.SelectDB, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 5, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.metadata_all.addWidget(self.popup_frame, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.metadata_all, 1, 0, 1, 1)

        self.popup_stacked.addWidget(self.LoadAnalysis)
        self.APAnimation = QWidget()
        self.APAnimation.setObjectName(u"APAnimation")
        self.gridLayout_9 = QGridLayout(self.APAnimation)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.gridLayout_9.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.popup_stacked.addWidget(self.APAnimation)
        self.ExportAnalysis = QWidget()
        self.ExportAnalysis.setObjectName(u"ExportAnalysis")
        self.gridLayout_6 = QGridLayout(self.ExportAnalysis)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.metadata_all_2 = QGridLayout()
        self.metadata_all_2.setObjectName(u"metadata_all_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.ExportAnalysis)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 1, 3, 1, 1)

        self.label = QLabel(self.ExportAnalysis)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.Path = QLineEdit(self.ExportAnalysis)
        self.Path.setObjectName(u"Path")

        self.gridLayout_5.addWidget(self.Path, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.ExportAnalysis)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.comboBox, 1, 4, 1, 1)

        self.ExportDb = QPushButton(self.ExportAnalysis)
        self.ExportDb.setObjectName(u"ExportDb")
        sizePolicy1.setHeightForWidth(self.ExportDb.sizePolicy().hasHeightForWidth())
        self.ExportDb.setSizePolicy(sizePolicy1)
        self.ExportDb.setMinimumSize(QSize(120, 0))
        self.ExportDb.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.ExportDb, 1, 5, 1, 1)

        self.line_2 = QFrame(self.ExportAnalysis)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 1, 6, 1, 1)

        self.SetPath = QPushButton(self.ExportAnalysis)
        self.SetPath.setObjectName(u"SetPath")

        self.gridLayout_5.addWidget(self.SetPath, 1, 2, 1, 1)

        self.label_4 = QLabel(self.ExportAnalysis)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)


        self.metadata_all_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.table_layout_2 = QGridLayout()
        self.table_layout_2.setObjectName(u"table_layout_2")
        self.groupBox_2 = QGroupBox(self.ExportAnalysis)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_10 = QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_10.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.table_layout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.metadata_all_2.addLayout(self.table_layout_2, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.metadata_all_2, 0, 0, 1, 1)

        self.popup_stacked.addWidget(self.ExportAnalysis)

        self.gridLayout_2.addWidget(self.popup_stacked, 1, 0, 1, 1)


        self.retranslateUi(MetadataPopup)

        self.popup_stacked.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MetadataPopup)
    # setupUi

    def retranslateUi(self, MetadataPopup):
        MetadataPopup.setWindowTitle(QCoreApplication.translate("MetadataPopup", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("MetadataPopup", u"Table of available Analyses", None))
        self.label_2.setText(QCoreApplication.translate("MetadataPopup", u"Here you can select the Database ", None))
        self.submit.setText(QCoreApplication.translate("MetadataPopup", u"Open Analysis", None))
        self.label_6.setText(QCoreApplication.translate("MetadataPopup", u"Select Offline Analysis ID", None))
        self.SelectDB.setText(QCoreApplication.translate("MetadataPopup", u"Select Database", None))
        self.label_3.setText(QCoreApplication.translate("MetadataPopup", u"Set Offline Analysis ID", None))
        self.label.setText(QCoreApplication.translate("MetadataPopup", u"Set the Export Path", None))
        self.Path.setText("")
        self.ExportDb.setText(QCoreApplication.translate("MetadataPopup", u"Export DataBase", None))
        self.SetPath.setText(QCoreApplication.translate("MetadataPopup", u"Set Path", None))
        self.label_4.setText(QCoreApplication.translate("MetadataPopup", u"Open previous Analysis", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MetadataPopup", u"Table View of Available Offline Analysis IDs", None))
    # retranslateUi

