# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_meta_data_group.ui'
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

class Ui_assign_meta_data_group(object):
    def setupUi(self, assign_meta_data_group):
        if not assign_meta_data_group.objectName():
            assign_meta_data_group.setObjectName(u"assign_meta_data_group")
        assign_meta_data_group.resize(1034, 525)
        self.gridLayout = QGridLayout(assign_meta_data_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.meta_data_template_layout = QGridLayout()
        self.meta_data_template_layout.setObjectName(u"meta_data_template_layout")

        self.gridLayout.addLayout(self.meta_data_template_layout, 2, 1, 3, 4)

        self.label = QLabel(assign_meta_data_group)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.load_template = QPushButton(assign_meta_data_group)
        self.load_template.setObjectName(u"load_template")

        self.gridLayout.addWidget(self.load_template, 5, 1, 1, 1)

        self.save_to_template_button = QPushButton(assign_meta_data_group)
        self.save_to_template_button.setObjectName(u"save_to_template_button")

        self.gridLayout.addWidget(self.save_to_template_button, 5, 2, 1, 1)

        self.continue_loading = QPushButton(assign_meta_data_group)
        self.continue_loading.setObjectName(u"continue_loading")

        self.gridLayout.addWidget(self.continue_loading, 5, 3, 1, 1)


        self.retranslateUi(assign_meta_data_group)

        QMetaObject.connectSlotsByName(assign_meta_data_group)
    # setupUi

    def retranslateUi(self, assign_meta_data_group):
        assign_meta_data_group.setWindowTitle(QCoreApplication.translate("assign_meta_data_group", u"Form", None))
        self.label.setText(QCoreApplication.translate("assign_meta_data_group", u"Assign meta data annotation to each experiment !", None))
        self.load_template.setText(QCoreApplication.translate("assign_meta_data_group", u"Load Template", None))
        self.save_to_template_button.setText(QCoreApplication.translate("assign_meta_data_group", u"Save to Template and Conitnue", None))
        self.continue_loading.setText(QCoreApplication.translate("assign_meta_data_group", u"Continue", None))
    # retranslateUi