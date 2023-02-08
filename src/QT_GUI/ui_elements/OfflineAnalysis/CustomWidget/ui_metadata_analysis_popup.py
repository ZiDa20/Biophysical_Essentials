# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metadata_analysis_popup.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MetadataPopup(object):
    def setupUi(self, MetadataPopup):
        if not MetadataPopup.objectName():
            MetadataPopup.setObjectName(u"MetadataPopup")
        MetadataPopup.resize(1303, 808)
        self.gridLayout_2 = QGridLayout(MetadataPopup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.submit = QPushButton(MetadataPopup)
        self.submit.setObjectName(u"submit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setMinimumSize(QSize(120, 0))
        self.submit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.submit, 0, 0, 1, 1, Qt.AlignBottom)

        self.quit = QPushButton(MetadataPopup)
        self.quit.setObjectName(u"quit")
        sizePolicy.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)
        self.quit.setMinimumSize(QSize(120, 0))
        self.quit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.quit, 0, 2, 1, 1, Qt.AlignBottom)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.line = QFrame(MetadataPopup)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.metadata_all = QGridLayout()
        self.metadata_all.setObjectName(u"metadata_all")
        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")
        self.table_widget = QWidget(MetadataPopup)
        self.table_widget.setObjectName(u"table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy1)
        self.gridLayout_8 = QGridLayout(self.table_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox = QGroupBox(self.table_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.final_table_layout = QGridLayout()
        self.final_table_layout.setObjectName(u"final_table_layout")
        self.final_table_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.final_table_layout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.final_table_layout, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SearchExperiment = QLineEdit(self.groupBox)
        self.SearchExperiment.setObjectName(u"SearchExperiment")
        self.SearchExperiment.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_3.addWidget(self.SearchExperiment, 0, 1, 1, 1)

        self.submitexp = QPushButton(self.groupBox)
        self.submitexp.setObjectName(u"submitexp")

        self.gridLayout_3.addWidget(self.submitexp, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)

        self.SearchSeries = QLineEdit(self.groupBox)
        self.SearchSeries.setObjectName(u"SearchSeries")
        self.SearchSeries.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_3.addWidget(self.SearchSeries, 0, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.submitser = QPushButton(self.groupBox)
        self.submitser.setObjectName(u"submitser")

        self.gridLayout_3.addWidget(self.submitser, 0, 5, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 1)


        self.table_layout.addWidget(self.table_widget, 0, 0, 1, 1)


        self.metadata_all.addLayout(self.table_layout, 0, 0, 1, 1)

        self.button_layout = QGridLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.button_layout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.metadata_all.addLayout(self.button_layout, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.metadata_all, 0, 0, 1, 1)


        self.retranslateUi(MetadataPopup)

        QMetaObject.connectSlotsByName(MetadataPopup)
    # setupUi

    def retranslateUi(self, MetadataPopup):
        MetadataPopup.setWindowTitle(QCoreApplication.translate("MetadataPopup", u"Form", None))
        self.submit.setText(QCoreApplication.translate("MetadataPopup", u"Submit", None))
        self.quit.setText(QCoreApplication.translate("MetadataPopup", u"Quit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MetadataPopup", u"Edit Series Specific Metadata", None))
        self.submitexp.setText(QCoreApplication.translate("MetadataPopup", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MetadataPopup", u"Select Series: ", None))
        self.label.setText(QCoreApplication.translate("MetadataPopup", u"Select Experiment: ", None))
        self.submitser.setText(QCoreApplication.translate("MetadataPopup", u"Search", None))
    # retranslateUi

