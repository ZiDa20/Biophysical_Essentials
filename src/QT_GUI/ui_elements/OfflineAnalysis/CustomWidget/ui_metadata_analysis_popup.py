# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'metadata_analysis_popup.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MetadataPopup(object):
    def setupUi(self, MetadataPopup):
        if not MetadataPopup.objectName():
            MetadataPopup.setObjectName(u"MetadataPopup")
        MetadataPopup.resize(878, 573)
        self.gridLayout_2 = QGridLayout(MetadataPopup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.metadata_all = QGridLayout()
        self.metadata_all.setObjectName(u"metadata_all")
        self.button_layout = QGridLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.quit = QPushButton(MetadataPopup)
        self.quit.setObjectName(u"quit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)
        self.quit.setMinimumSize(QSize(120, 0))
        self.quit.setMaximumSize(QSize(150, 16777215))

        self.button_layout.addWidget(self.quit, 2, 0, 1, 1)

        self.submit = QPushButton(MetadataPopup)
        self.submit.setObjectName(u"submit")
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setMinimumSize(QSize(120, 0))
        self.submit.setMaximumSize(QSize(150, 16777215))

        self.button_layout.addWidget(self.submit, 1, 0, 1, 1)

        self.edit = QPushButton(MetadataPopup)
        self.edit.setObjectName(u"edit")
        sizePolicy.setHeightForWidth(self.edit.sizePolicy().hasHeightForWidth())
        self.edit.setSizePolicy(sizePolicy)
        self.edit.setMinimumSize(QSize(120, 0))
        self.edit.setMaximumSize(QSize(150, 16777215))

        self.button_layout.addWidget(self.edit, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.button_layout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.metadata_all.addLayout(self.button_layout, 0, 1, 1, 1)

        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")
        self.table_widget = QWidget(MetadataPopup)
        self.table_widget.setObjectName(u"table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy1)
        self.gridLayout_8 = QGridLayout(self.table_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.final_table_layout = QGridLayout()
        self.final_table_layout.setObjectName(u"final_table_layout")

        self.gridLayout_8.addLayout(self.final_table_layout, 0, 0, 1, 1)


        self.table_layout.addWidget(self.table_widget, 0, 0, 1, 1)


        self.metadata_all.addLayout(self.table_layout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.metadata_all, 1, 0, 1, 1)

        self.edit_label = QLabel(MetadataPopup)
        self.edit_label.setObjectName(u"edit_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit_label.sizePolicy().hasHeightForWidth())
        self.edit_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.edit_label, 0, 0, 1, 1)


        self.retranslateUi(MetadataPopup)

        QMetaObject.connectSlotsByName(MetadataPopup)
    # setupUi

    def retranslateUi(self, MetadataPopup):
        MetadataPopup.setWindowTitle(QCoreApplication.translate("MetadataPopup", u"Form", None))
        self.quit.setText(QCoreApplication.translate("MetadataPopup", u"Quit", None))
        self.submit.setText(QCoreApplication.translate("MetadataPopup", u"Submit", None))
        self.edit.setText(QCoreApplication.translate("MetadataPopup", u"Edit", None))
        self.edit_label.setText(QCoreApplication.translate("MetadataPopup", u"Edit your MetaData", None))
    # retranslateUi

