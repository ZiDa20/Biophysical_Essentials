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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QWidget)

class Ui_MetadataPopup(object):
    def setupUi(self, MetadataPopup):
        if not MetadataPopup.objectName():
            MetadataPopup.setObjectName(u"MetadataPopup")
        MetadataPopup.resize(1303, 808)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MetadataPopup.sizePolicy().hasHeightForWidth())
        MetadataPopup.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(MetadataPopup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.metadata_all = QGridLayout()
        self.metadata_all.setObjectName(u"metadata_all")
        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")
        self.table_widget = QWidget(MetadataPopup)
        self.table_widget.setObjectName(u"table_widget")
        sizePolicy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy)
        self.table_widget.setMinimumSize(QSize(500, 500))
        self.gridLayout_8 = QGridLayout(self.table_widget)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.edit_label = QLabel(self.table_widget)
        self.edit_label.setObjectName(u"edit_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_label.sizePolicy().hasHeightForWidth())
        self.edit_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(15)
        self.edit_label.setFont(font)
        self.edit_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.edit_label, 0, 0, 1, 3)

        self.submit = QPushButton(self.table_widget)
        self.submit.setObjectName(u"submit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy2)
        self.submit.setMinimumSize(QSize(120, 0))
        self.submit.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_8.addWidget(self.submit, 2, 1, 1, 1)

        self.final_table_layout = QGridLayout()
        self.final_table_layout.setObjectName(u"final_table_layout")
        self.tableView = QTableView(self.table_widget)
        self.tableView.setObjectName(u"tableView")

        self.final_table_layout.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.final_table_layout, 1, 0, 1, 3)

        self.lineEdit = QLineEdit(self.table_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_8.addWidget(self.lineEdit, 2, 0, 1, 1)


        self.table_layout.addWidget(self.table_widget, 0, 0, 1, 1)


        self.metadata_all.addLayout(self.table_layout, 0, 0, 1, 1)

        self.button_layout = QGridLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.button_layout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.metadata_all.addLayout(self.button_layout, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.metadata_all, 1, 0, 1, 1)


        self.retranslateUi(MetadataPopup)

        QMetaObject.connectSlotsByName(MetadataPopup)
    # setupUi

    def retranslateUi(self, MetadataPopup):
        MetadataPopup.setWindowTitle(QCoreApplication.translate("MetadataPopup", u"Form", None))
        self.edit_label.setText(QCoreApplication.translate("MetadataPopup", u"Open Results From An Existing Analysis", None))
        self.submit.setText(QCoreApplication.translate("MetadataPopup", u"Open", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MetadataPopup", u"Enter the analysis id and click open", None))
    # retranslateUi

