# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SeriesItem.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_OfflineTree(object):
    def setupUi(self, OfflineTree):
        if not OfflineTree.objectName():
            OfflineTree.setObjectName(u"OfflineTree")
        OfflineTree.resize(291, 623)
        self.gridLayout = QGridLayout(OfflineTree)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.TreeLayout1 = QGridLayout()
        self.TreeLayout1.setObjectName(u"TreeLayout1")
        self.SeriesItems = QTreeWidget(OfflineTree)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.SeriesItems.setHeaderItem(__qtreewidgetitem)
        self.SeriesItems.setObjectName(u"SeriesItems")

        self.TreeLayout1.addWidget(self.SeriesItems, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.TreeLayout1, 0, 0, 1, 1)


        self.retranslateUi(OfflineTree)

        QMetaObject.connectSlotsByName(OfflineTree)
    # setupUi

    def retranslateUi(self, OfflineTree):
        OfflineTree.setWindowTitle(QCoreApplication.translate("OfflineTree", u"Form", None))
    # retranslateUi

