# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageReverse.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLayout,
    QLineEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QWidget)
import resources.resources_rc

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.setEnabled(True)
        MainForm.setMinimumSize(QSize(1280, 720))
        MainForm.setMaximumSize(QSize(1280, 720))
        icon = QIcon()
        icon.addFile(u":/picture/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.groupPath = QGroupBox(MainForm)
        self.groupPath.setObjectName(u"groupPath")
        self.groupPath.setGeometry(QRect(4, 0, 663, 68))
        self.groupPath.setMinimumSize(QSize(0, 68))
        self.groupPath.setMaximumSize(QSize(16777215, 68))
        self.groupPathLayout = QGridLayout(self.groupPath)
        self.groupPathLayout.setSpacing(1)
        self.groupPathLayout.setObjectName(u"groupPathLayout")
        self.groupPathLayout.setContentsMargins(3, 0, 3, 3)
        self.inputImgPath = QLineEdit(self.groupPath)
        self.inputImgPath.setObjectName(u"inputImgPath")

        self.groupPathLayout.addWidget(self.inputImgPath, 0, 0, 1, 1)

        self.btnSavePath = QPushButton(self.groupPath)
        self.btnSavePath.setObjectName(u"btnSavePath")

        self.groupPathLayout.addWidget(self.btnSavePath, 1, 1, 1, 1)

        self.inputSavePath = QLineEdit(self.groupPath)
        self.inputSavePath.setObjectName(u"inputSavePath")

        self.groupPathLayout.addWidget(self.inputSavePath, 1, 0, 1, 1)

        self.btnImgPath = QPushButton(self.groupPath)
        self.btnImgPath.setObjectName(u"btnImgPath")

        self.groupPathLayout.addWidget(self.btnImgPath, 0, 1, 1, 1)

        self.groupProgress = QGroupBox(MainForm)
        self.groupProgress.setObjectName(u"groupProgress")
        self.groupProgress.setGeometry(QRect(4, 67, 263, 116))
        self.groupProgressLayout = QGridLayout(self.groupProgress)
        self.groupProgressLayout.setSpacing(1)
        self.groupProgressLayout.setObjectName(u"groupProgressLayout")
        self.groupProgressLayout.setContentsMargins(3, 0, 3, 3)
        self.btnReadImg = QPushButton(self.groupProgress)
        self.btnReadImg.setObjectName(u"btnReadImg")

        self.groupProgressLayout.addWidget(self.btnReadImg, 0, 0, 1, 1)

        self.btnChangeStructure = QPushButton(self.groupProgress)
        self.btnChangeStructure.setObjectName(u"btnChangeStructure")

        self.groupProgressLayout.addWidget(self.btnChangeStructure, 1, 0, 1, 1)

        self.btnImgReverse = QPushButton(self.groupProgress)
        self.btnImgReverse.setObjectName(u"btnImgReverse")

        self.groupProgressLayout.addWidget(self.btnImgReverse, 2, 0, 1, 1)

        self.barProgress = QProgressBar(self.groupProgress)
        self.barProgress.setObjectName(u"barProgress")
        self.barProgress.setAlignment(Qt.AlignCenter)

        self.groupProgressLayout.addWidget(self.barProgress, 3, 0, 1, 1)

        self.groupMessage = QGroupBox(MainForm)
        self.groupMessage.setObjectName(u"groupMessage")
        self.groupMessage.setGeometry(QRect(4, 183, 263, 292))
        self.groupMessageLayout = QGridLayout(self.groupMessage)
        self.groupMessageLayout.setSpacing(1)
        self.groupMessageLayout.setObjectName(u"groupMessageLayout")
        self.groupMessageLayout.setContentsMargins(4, 0, 4, 4)
        self.inputMessage = QTextEdit(self.groupMessage)
        self.inputMessage.setObjectName(u"inputMessage")
        self.inputMessage.setReadOnly(True)
        self.inputMessage.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.groupMessageLayout.addWidget(self.inputMessage, 0, 0, 1, 1)

        self.groupListImg = QGroupBox(MainForm)
        self.groupListImg.setObjectName(u"groupListImg")
        self.groupListImg.setGeometry(QRect(4, 474, 663, 242))
        self.groupListImgLayout = QGridLayout(self.groupListImg)
        self.groupListImgLayout.setSpacing(1)
        self.groupListImgLayout.setObjectName(u"groupListImgLayout")
        self.groupListImgLayout.setContentsMargins(4, 0, 4, 4)
        self.listImgTree = QTreeWidget(self.groupListImg)
        self.listImgTree.setObjectName(u"listImgTree")
        self.listImgTree.setEnabled(True)
        self.listImgTree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.groupListImgLayout.addWidget(self.listImgTree, 0, 0, 1, 1)

        self.groupImgSmall = QGroupBox(MainForm)
        self.groupImgSmall.setObjectName(u"groupImgSmall")
        self.groupImgSmall.setGeometry(QRect(671, 0, 605, 716))
        self.groupImgSmall.setMinimumSize(QSize(605, 0))
        self.groupImgSmall.setMaximumSize(QSize(605, 16777215))
        self.groupImgSmallLayout = QGridLayout(self.groupImgSmall)
        self.groupImgSmallLayout.setSpacing(1)
        self.groupImgSmallLayout.setObjectName(u"groupImgSmallLayout")
        self.groupImgSmallLayout.setContentsMargins(4, 0, 4, 4)
        self.scrollAreaImgSmall = QScrollArea(self.groupImgSmall)
        self.scrollAreaImgSmall.setObjectName(u"scrollAreaImgSmall")
        self.scrollAreaImgSmall.setMinimumSize(QSize(595, 0))
        self.scrollAreaImgSmall.setMaximumSize(QSize(595, 16777215))
        self.scrollAreaImgSmall.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollAreaImgSmall.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaImgSmall.setWidgetResizable(True)
        self.scrollAreaImgSmall.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaImgSmallWidget = QWidget()
        self.scrollAreaImgSmallWidget.setObjectName(u"scrollAreaImgSmallWidget")
        self.scrollAreaImgSmallWidgetLayout = QGridLayout(self.scrollAreaImgSmallWidget)
        self.scrollAreaImgSmallWidgetLayout.setSpacing(0)
        self.scrollAreaImgSmallWidgetLayout.setObjectName(u"scrollAreaImgSmallWidgetLayout")
        self.scrollAreaImgSmallWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImgSmallBack = QLabel(self.scrollAreaImgSmallWidget)
        self.labelImgSmallBack.setObjectName(u"labelImgSmallBack")
        self.labelImgSmallBack.setFrameShape(QFrame.Panel)
        self.labelImgSmallBack.setFrameShadow(QFrame.Raised)
        self.labelImgSmallBack.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.scrollAreaImgSmallWidgetLayout.addWidget(self.labelImgSmallBack, 0, 0, 1, 1)

        self.scrollAreaImgSmall.setWidget(self.scrollAreaImgSmallWidget)

        self.groupImgSmallLayout.addWidget(self.scrollAreaImgSmall, 0, 0, 1, 1)

        self.groupImgBig = QGroupBox(MainForm)
        self.groupImgBig.setObjectName(u"groupImgBig")
        self.groupImgBig.setGeometry(QRect(271, 67, 396, 408))
        self.groupImgBig.setMinimumSize(QSize(396, 408))
        self.groupImgBig.setMaximumSize(QSize(396, 408))
        self.groupImgBigLayout = QGridLayout(self.groupImgBig)
        self.groupImgBigLayout.setSpacing(1)
        self.groupImgBigLayout.setObjectName(u"groupImgBigLayout")
        self.groupImgBigLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.groupImgBigLayout.setContentsMargins(4, 0, 4, 4)
        self.scrollAreaImgBig = QScrollArea(self.groupImgBig)
        self.scrollAreaImgBig.setObjectName(u"scrollAreaImgBig")
        self.scrollAreaImgBig.setMinimumSize(QSize(386, 386))
        self.scrollAreaImgBig.setMaximumSize(QSize(386, 386))
        self.scrollAreaImgBig.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaImgBig.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaImgBig.setWidgetResizable(True)
        self.scrollAreaImgBigWidget = QWidget()
        self.scrollAreaImgBigWidget.setObjectName(u"scrollAreaImgBigWidget")
        self.scrollAreaImgBigWidget.setGeometry(QRect(0, 0, 384, 384))
        self.labelImgBigShow = QLabel(self.scrollAreaImgBigWidget)
        self.labelImgBigShow.setObjectName(u"labelImgBigShow")
        self.labelImgBigShow.setGeometry(QRect(0, 0, 384, 384))
        self.labelImgBigShow.setAlignment(Qt.AlignCenter)
        self.labelImgBigBack = QLabel(self.scrollAreaImgBigWidget)
        self.labelImgBigBack.setObjectName(u"labelImgBigBack")
        self.labelImgBigBack.setGeometry(QRect(0, 0, 384, 384))
        self.labelImgBigBack.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaImgBigWidgetLayout = QGridLayout(self.scrollAreaImgBigWidget)
        self.scrollAreaImgBigWidgetLayout.setSpacing(0)
        self.scrollAreaImgBigWidgetLayout.setObjectName(u"scrollAreaImgBigWidgetLayout")
        self.scrollAreaImgBigWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImgBigText = QLabel(self.scrollAreaImgBigWidget)
        self.labelImgBigText.setObjectName(u"labelImgBigText")
        self.labelImgBigText.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.scrollAreaImgBigWidgetLayout.addWidget(self.labelImgBigText, 0, 0, 1, 1)

        self.scrollAreaImgBig.setWidget(self.scrollAreaImgBigWidget)
        self.labelImgBigBack.raise_()
        self.labelImgBigShow.raise_()
        self.labelImgBigText.raise_()

        self.groupImgBigLayout.addWidget(self.scrollAreaImgBig, 0, 0, 1, 1)

        self.groupImgBigLayout.setColumnStretch(0, 3)

        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"\u5e8f\u5217\u5e27\u56fe\u7247\u7ffb\u8f6c\u5de5\u5177", None))
        self.groupPath.setTitle(QCoreApplication.translate("MainForm", u"\u8def\u5f84\u9009\u62e9", None))
        self.btnSavePath.setText(QCoreApplication.translate("MainForm", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.btnImgPath.setText(QCoreApplication.translate("MainForm", u"\u7d20\u6750\u8def\u5f84", None))
        self.groupProgress.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u64cd\u4f5c", None))
        self.btnReadImg.setText(QCoreApplication.translate("MainForm", u"\u8bfb\u53d6\u56fe\u7247", None))
        self.btnChangeStructure.setText(QCoreApplication.translate("MainForm", u"\u8c03\u6574\u7ed3\u6784", None))
        self.btnImgReverse.setText(QCoreApplication.translate("MainForm", u"\u7ffb\u8f6c\u56fe\u7247", None))
        self.groupMessage.setTitle(QCoreApplication.translate("MainForm", u"\u6d88\u606f\u8f93\u51fa", None))
        self.groupListImg.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u5217\u8868", None))
        ___qtreewidgetitem = self.listImgTree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainForm", u"\u8def\u5f84", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainForm", u"\u540d\u79f0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainForm", u"\u5e8f\u53f7", None));
        self.groupImgSmall.setTitle(QCoreApplication.translate("MainForm", u"\u5c0f\u56fe\u9884\u89c8", None))
        self.groupImgBig.setTitle(QCoreApplication.translate("MainForm", u"\u5927\u56fe\u9884\u89c8", None))
        self.labelImgBigText.setText(QCoreApplication.translate("MainForm", u"\u70b9\u51fb\u62d6\u52a8\u56fe\u7247\uff0c\u4f7f\u7528\u6eda\u8f6e\u7f29\u653e(100%)", None))
    # retranslateUi

