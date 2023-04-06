# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RedundantDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_RedundantDialog(object):
    def setupUi(self, RedundantDialog):
        if not RedundantDialog.objectName():
            RedundantDialog.setObjectName(u"RedundantDialog")
        RedundantDialog.resize(693, 370)
        self.gridLayout_2 = QGridLayout(RedundantDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(RedundantDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 2, 1, 1, 1, Qt.AlignHCenter)

        self.checkName = QPushButton(self.groupBox)
        self.checkName.setObjectName(u"checkName")

        self.gridLayout_4.addWidget(self.checkName, 1, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.redundant_label = QLabel(self.groupBox)
        self.redundant_label.setObjectName(u"redundant_label")
        font = QFont()
        font.setPointSize(12)
        self.redundant_label.setFont(font)

        self.gridLayout_6.addWidget(self.redundant_label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.line_2 = QFrame(RedundantDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(RedundantDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(RedundantDialog)
        self.buttonBox.accepted.connect(RedundantDialog.accept)
        self.buttonBox.rejected.connect(RedundantDialog.reject)

        QMetaObject.connectSlotsByName(RedundantDialog)
    # setupUi

    def retranslateUi(self, RedundantDialog):
        RedundantDialog.setWindowTitle(QCoreApplication.translate("RedundantDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("RedundantDialog", u"Redundant Data", None))
        self.label_2.setText(QCoreApplication.translate("RedundantDialog", u"Please Rename the File:", None))
        self.checkBox.setText(QCoreApplication.translate("RedundantDialog", u"Permantely discard entry in Offline Analysis", None))
        self.checkName.setText(QCoreApplication.translate("RedundantDialog", u"Check Name", None))
        self.redundant_label.setText(QCoreApplication.translate("RedundantDialog", u"You have already a file with the same experiment name in the database! \n"
" This can be because you loaded the same file twice or because of file name duplication !", None))
    # retranslateUi

