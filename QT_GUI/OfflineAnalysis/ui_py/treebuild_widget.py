# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_Form(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(655, 872)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(550, 0))
        self.groupBox_4.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.swap_column = QPushButton(self.groupBox_4)
        self.swap_column.setObjectName(u"swap_column")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.swap_column.sizePolicy().hasHeightForWidth())
        self.swap_column.setSizePolicy(sizePolicy2)
        self.swap_column.setMaximumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.swap_column)

        self.meta_table = QPushButton(self.groupBox_4)
        self.meta_table.setObjectName(u"meta_table")
        sizePolicy2.setHeightForWidth(self.meta_table.sizePolicy().hasHeightForWidth())
        self.meta_table.setSizePolicy(sizePolicy2)
        self.meta_table.setMaximumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.meta_table)

        self.load_table = QPushButton(self.groupBox_4)
        self.load_table.setObjectName(u"load_table")
        sizePolicy2.setHeightForWidth(self.load_table.sizePolicy().hasHeightForWidth())
        self.load_table.setSizePolicy(sizePolicy2)
        self.load_table.setMaximumSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.load_table)

        self.hallo = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hallo)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.directory_tree_widget = QTabWidget(self.groupBox_4)
        self.directory_tree_widget.setObjectName(u"directory_tree_widget")
        sizePolicy.setHeightForWidth(self.directory_tree_widget.sizePolicy().hasHeightForWidth())
        self.directory_tree_widget.setSizePolicy(sizePolicy)
        self.selected_tree_view = QWidget()
        self.selected_tree_view.setObjectName(u"selected_tree_view")
        self.gridLayout_8 = QGridLayout(self.selected_tree_view)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.experiments_tree_view = QTreeWidget(self.selected_tree_view)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")
        self.experiments_tree_view.setFrameShape(QFrame.NoFrame)
        self.experiments_tree_view.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.experiments_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.selected_tree_view, "")
        self.discarde_tree_view = QWidget()
        self.discarde_tree_view.setObjectName(u"discarde_tree_view")
        self.gridLayout_2 = QGridLayout(self.discarde_tree_view)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.outfiltered_tree_view = QTreeWidget(self.discarde_tree_view)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")

        self.gridLayout_2.addWidget(self.outfiltered_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.discarde_tree_view, "")

        self.gridLayout_5.addWidget(self.directory_tree_widget, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.directory_tree_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Experiment Hierarchie", None))
        self.label.setText(QCoreApplication.translate("Form", u"Edit Experiment Data:", None))
        self.swap_column.setText(QCoreApplication.translate("Form", u"C", None))
        self.meta_table.setText(QCoreApplication.translate("Form", u"M", None))
        self.load_table.setText(QCoreApplication.translate("Form", u"L", None))
        ___qtreewidgetitem = self.experiments_tree_view.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Discard", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Group", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Object", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.selected_tree_view), QCoreApplication.translate("Form", u"Selected", None))
        ___qtreewidgetitem1 = self.outfiltered_tree_view.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Form", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Form", u"Group", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Object", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.discarde_tree_view), QCoreApplication.translate("Form", u"Discarded", None))
    # retranslateUi



class TreeBuild(Ui_Form):
    def __init__(self,parent = None):
        self.parent = parent
        QWidget.__init__(self,parent)
        self.setupUi(self)