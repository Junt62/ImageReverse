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
        MainForm.resize(1280, 720)
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
        self.inputSavePath = QLineEdit(self.groupPath)
        self.inputSavePath.setObjectName(u"inputSavePath")

        self.groupPathLayout.addWidget(self.inputSavePath, 1, 1, 1, 1)

        self.inputImgPath = QLineEdit(self.groupPath)
        self.inputImgPath.setObjectName(u"inputImgPath")

        self.groupPathLayout.addWidget(self.inputImgPath, 0, 1, 1, 1)

        self.btnImgPath = QPushButton(self.groupPath)
        self.btnImgPath.setObjectName(u"btnImgPath")
        self.btnImgPath.setMinimumSize(QSize(68, 23))
        self.btnImgPath.setMaximumSize(QSize(68, 23))

        self.groupPathLayout.addWidget(self.btnImgPath, 0, 0, 1, 1)

        self.btnSavePath = QPushButton(self.groupPath)
        self.btnSavePath.setObjectName(u"btnSavePath")
        self.btnSavePath.setMinimumSize(QSize(68, 23))
        self.btnSavePath.setMaximumSize(QSize(68, 23))

        self.groupPathLayout.addWidget(self.btnSavePath, 1, 0, 1, 1)

        self.groupProgress = QGroupBox(MainForm)
        self.groupProgress.setObjectName(u"groupProgress")
        self.groupProgress.setGeometry(QRect(4, 134, 263, 133))
        self.gridLayout = QGridLayout(self.groupProgress)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 0, 3, 3)
        self.inputPositionOldY = QLineEdit(self.groupProgress)
        self.inputPositionOldY.setObjectName(u"inputPositionOldY")

        self.gridLayout.addWidget(self.inputPositionOldY, 0, 3, 1, 1)

        self.barProgress = QProgressBar(self.groupProgress)
        self.barProgress.setObjectName(u"barProgress")
        self.barProgress.setMinimumSize(QSize(0, 16))
        self.barProgress.setMaximumSize(QSize(16777215, 16))
        self.barProgress.setValue(0)
        self.barProgress.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.barProgress, 7, 0, 1, 6)

        self.inputPositionNewX = QLineEdit(self.groupProgress)
        self.inputPositionNewX.setObjectName(u"inputPositionNewX")

        self.gridLayout.addWidget(self.inputPositionNewX, 1, 2, 1, 1)

        self.inputPositionNewY = QLineEdit(self.groupProgress)
        self.inputPositionNewY.setObjectName(u"inputPositionNewY")

        self.gridLayout.addWidget(self.inputPositionNewY, 1, 3, 1, 1)

        self.labelPositionOld = QLabel(self.groupProgress)
        self.labelPositionOld.setObjectName(u"labelPositionOld")

        self.gridLayout.addWidget(self.labelPositionOld, 0, 0, 1, 2)

        self.inputPositionOldX = QLineEdit(self.groupProgress)
        self.inputPositionOldX.setObjectName(u"inputPositionOldX")

        self.gridLayout.addWidget(self.inputPositionOldX, 0, 2, 1, 1)

        self.btnReadPosition = QPushButton(self.groupProgress)
        self.btnReadPosition.setObjectName(u"btnReadPosition")

        self.gridLayout.addWidget(self.btnReadPosition, 2, 0, 1, 1)

        self.btnApplyPosition = QPushButton(self.groupProgress)
        self.btnApplyPosition.setObjectName(u"btnApplyPosition")

        self.gridLayout.addWidget(self.btnApplyPosition, 2, 2, 1, 1)

        self.btnAutoAlignment = QPushButton(self.groupProgress)
        self.btnAutoAlignment.setObjectName(u"btnAutoAlignment")

        self.gridLayout.addWidget(self.btnAutoAlignment, 2, 3, 1, 1)

        self.btnOpenFolder = QPushButton(self.groupProgress)
        self.btnOpenFolder.setObjectName(u"btnOpenFolder")

        self.gridLayout.addWidget(self.btnOpenFolder, 5, 0, 1, 1)

        self.btnChangeStructure = QPushButton(self.groupProgress)
        self.btnChangeStructure.setObjectName(u"btnChangeStructure")

        self.gridLayout.addWidget(self.btnChangeStructure, 5, 2, 1, 1)

        self.btnImgReverse = QPushButton(self.groupProgress)
        self.btnImgReverse.setObjectName(u"btnImgReverse")

        self.gridLayout.addWidget(self.btnImgReverse, 5, 3, 1, 1)

        self.labelPositionNew = QLabel(self.groupProgress)
        self.labelPositionNew.setObjectName(u"labelPositionNew")

        self.gridLayout.addWidget(self.labelPositionNew, 1, 0, 1, 1)

        self.groupMessage = QGroupBox(MainForm)
        self.groupMessage.setObjectName(u"groupMessage")
        self.groupMessage.setGeometry(QRect(4, 267, 263, 208))
        self.groupMessageLayout = QGridLayout(self.groupMessage)
        self.groupMessageLayout.setSpacing(0)
        self.groupMessageLayout.setObjectName(u"groupMessageLayout")
        self.groupMessageLayout.setContentsMargins(4, 0, 4, 5)
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
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.listImgTree.setHeaderItem(__qtreewidgetitem)
        self.listImgTree.setObjectName(u"listImgTree")
        self.listImgTree.setEnabled(True)
        self.listImgTree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.groupListImgLayout.addWidget(self.listImgTree, 0, 0, 1, 1)

        self.groupImgTable = QGroupBox(MainForm)
        self.groupImgTable.setObjectName(u"groupImgTable")
        self.groupImgTable.setGeometry(QRect(671, 0, 605, 716))
        self.groupImgTable.setMinimumSize(QSize(605, 0))
        self.groupImgTable.setMaximumSize(QSize(605, 16777215))
        self.groupImgSmallLayout = QGridLayout(self.groupImgTable)
        self.groupImgSmallLayout.setSpacing(1)
        self.groupImgSmallLayout.setObjectName(u"groupImgSmallLayout")
        self.groupImgSmallLayout.setContentsMargins(4, 0, 4, 4)
        self.scrollImgTable = QScrollArea(self.groupImgTable)
        self.scrollImgTable.setObjectName(u"scrollImgTable")
        self.scrollImgTable.setMinimumSize(QSize(595, 0))
        self.scrollImgTable.setMaximumSize(QSize(595, 16777215))
        self.scrollImgTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollImgTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollImgTable.setWidgetResizable(True)
        self.scrollImgTable.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollImgTableWidget = QWidget()
        self.scrollImgTableWidget.setObjectName(u"scrollImgTableWidget")
        self.scrollImgTableWidget.setGeometry(QRect(0, 0, 576, 693))
        self.scrollAreaImgSmallWidgetLayout = QGridLayout(self.scrollImgTableWidget)
        self.scrollAreaImgSmallWidgetLayout.setSpacing(0)
        self.scrollAreaImgSmallWidgetLayout.setObjectName(u"scrollAreaImgSmallWidgetLayout")
        self.scrollAreaImgSmallWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImgTableBack = QLabel(self.scrollImgTableWidget)
        self.labelImgTableBack.setObjectName(u"labelImgTableBack")
        self.labelImgTableBack.setFrameShape(QFrame.Panel)
        self.labelImgTableBack.setFrameShadow(QFrame.Raised)
        self.labelImgTableBack.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.scrollAreaImgSmallWidgetLayout.addWidget(self.labelImgTableBack, 0, 0, 1, 1)

        self.scrollImgTable.setWidget(self.scrollImgTableWidget)

        self.groupImgSmallLayout.addWidget(self.scrollImgTable, 0, 0, 1, 1)

        self.groupImgPreview = QGroupBox(MainForm)
        self.groupImgPreview.setObjectName(u"groupImgPreview")
        self.groupImgPreview.setGeometry(QRect(271, 67, 396, 408))
        self.groupImgPreview.setMinimumSize(QSize(396, 408))
        self.groupImgPreview.setMaximumSize(QSize(396, 408))
        self.groupImgBigLayout = QGridLayout(self.groupImgPreview)
        self.groupImgBigLayout.setSpacing(1)
        self.groupImgBigLayout.setObjectName(u"groupImgBigLayout")
        self.groupImgBigLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.groupImgBigLayout.setContentsMargins(4, 0, 4, 4)
        self.scrollImgPreview = QScrollArea(self.groupImgPreview)
        self.scrollImgPreview.setObjectName(u"scrollImgPreview")
        self.scrollImgPreview.setMinimumSize(QSize(386, 386))
        self.scrollImgPreview.setMaximumSize(QSize(386, 386))
        self.scrollImgPreview.viewport().setProperty("cursor", QCursor(Qt.SizeAllCursor))
        self.scrollImgPreview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollImgPreview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollImgPreview.setWidgetResizable(True)
        self.scrollImgPreviewWidget = QWidget()
        self.scrollImgPreviewWidget.setObjectName(u"scrollImgPreviewWidget")
        self.scrollImgPreviewWidget.setGeometry(QRect(0, 0, 384, 384))
        self.labelImgPreviewShow = QLabel(self.scrollImgPreviewWidget)
        self.labelImgPreviewShow.setObjectName(u"labelImgPreviewShow")
        self.labelImgPreviewShow.setGeometry(QRect(0, 0, 384, 384))
        self.labelImgPreviewShow.setAlignment(Qt.AlignCenter)
        self.labelImgPreviewBack = QLabel(self.scrollImgPreviewWidget)
        self.labelImgPreviewBack.setObjectName(u"labelImgPreviewBack")
        self.labelImgPreviewBack.setGeometry(QRect(0, 0, 384, 384))
        self.labelImgPreviewBack.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaImgBigWidgetLayout = QGridLayout(self.scrollImgPreviewWidget)
        self.scrollAreaImgBigWidgetLayout.setSpacing(0)
        self.scrollAreaImgBigWidgetLayout.setObjectName(u"scrollAreaImgBigWidgetLayout")
        self.scrollAreaImgBigWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImgPreviewText = QLabel(self.scrollImgPreviewWidget)
        self.labelImgPreviewText.setObjectName(u"labelImgPreviewText")
        self.labelImgPreviewText.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.scrollAreaImgBigWidgetLayout.addWidget(self.labelImgPreviewText, 0, 0, 1, 1)

        self.scrollImgPreview.setWidget(self.scrollImgPreviewWidget)
        self.labelImgPreviewBack.raise_()
        self.labelImgPreviewShow.raise_()
        self.labelImgPreviewText.raise_()

        self.groupImgBigLayout.addWidget(self.scrollImgPreview, 0, 0, 1, 1)

        self.groupImgBigLayout.setColumnStretch(0, 3)
        self.groupDisplaySetting = QGroupBox(MainForm)
        self.groupDisplaySetting.setObjectName(u"groupDisplaySetting")
        self.groupDisplaySetting.setGeometry(QRect(4, 67, 263, 68))
        self.gridLayout_2 = QGridLayout(self.groupDisplaySetting)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 0, 3, 3)
        self.labelDisplayColor = QLabel(self.groupDisplaySetting)
        self.labelDisplayColor.setObjectName(u"labelDisplayColor")

        self.gridLayout_2.addWidget(self.labelDisplayColor, 2, 0, 1, 1)

        self.inputDisplayType = QLineEdit(self.groupDisplaySetting)
        self.inputDisplayType.setObjectName(u"inputDisplayType")
        self.inputDisplayType.setReadOnly(True)

        self.gridLayout_2.addWidget(self.inputDisplayType, 0, 1, 1, 2)

        self.btnChangeDisplayType = QPushButton(self.groupDisplaySetting)
        self.btnChangeDisplayType.setObjectName(u"btnChangeDisplayType")

        self.gridLayout_2.addWidget(self.btnChangeDisplayType, 0, 3, 1, 1)

        self.inputDisplayColor = QLineEdit(self.groupDisplaySetting)
        self.inputDisplayColor.setObjectName(u"inputDisplayColor")
        self.inputDisplayColor.setReadOnly(True)

        self.gridLayout_2.addWidget(self.inputDisplayColor, 2, 1, 1, 2)

        self.labelDisplayType = QLabel(self.groupDisplaySetting)
        self.labelDisplayType.setObjectName(u"labelDisplayType")

        self.gridLayout_2.addWidget(self.labelDisplayType, 0, 0, 1, 1)

        self.btnChangeDisplayColor = QPushButton(self.groupDisplaySetting)
        self.btnChangeDisplayColor.setObjectName(u"btnChangeDisplayColor")

        self.gridLayout_2.addWidget(self.btnChangeDisplayColor, 2, 3, 1, 1)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"\u5e8f\u5217\u5e27\u56fe\u7247\u7ffb\u8f6c\u5de5\u5177", None))
        self.groupPath.setTitle(QCoreApplication.translate("MainForm", u"\u8def\u5f84\u9009\u62e9", None))
        self.btnImgPath.setText(QCoreApplication.translate("MainForm", u"\u7d20\u6750\u8def\u5f84", None))
        self.btnSavePath.setText(QCoreApplication.translate("MainForm", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.groupProgress.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u64cd\u4f5c", None))
        self.inputPositionOldY.setText(QCoreApplication.translate("MainForm", u"Y=0", None))
        self.inputPositionNewX.setText(QCoreApplication.translate("MainForm", u"X=0", None))
        self.inputPositionNewY.setText(QCoreApplication.translate("MainForm", u"Y=0", None))
        self.labelPositionOld.setText(QCoreApplication.translate("MainForm", u" \u539f\u59cb\u5750\u6807:", None))
        self.inputPositionOldX.setText(QCoreApplication.translate("MainForm", u"X=0", None))
        self.btnReadPosition.setText(QCoreApplication.translate("MainForm", u"\u8bfb\u53d6\u5750\u6807", None))
        self.btnApplyPosition.setText(QCoreApplication.translate("MainForm", u"\u5e94\u7528\u5750\u6807", None))
        self.btnAutoAlignment.setText(QCoreApplication.translate("MainForm", u"\u4e00\u952e\u5bf9\u9f50", None))
        self.btnOpenFolder.setText(QCoreApplication.translate("MainForm", u"\u6253\u5f00\u6587\u4ef6", None))
        self.btnChangeStructure.setText(QCoreApplication.translate("MainForm", u"\u8c03\u6574\u7ed3\u6784", None))
        self.btnImgReverse.setText(QCoreApplication.translate("MainForm", u"\u7ffb\u8f6c\u56fe\u7247", None))
        self.labelPositionNew.setText(QCoreApplication.translate("MainForm", u" \u65b0\u7684\u5750\u6807:", None))
        self.groupMessage.setTitle(QCoreApplication.translate("MainForm", u"\u6d88\u606f\u8f93\u51fa", None))
        self.groupListImg.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u5217\u8868", None))
        self.groupImgTable.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u5217\u8868", None))
        self.groupImgPreview.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u9884\u89c8", None))
        self.labelImgPreviewText.setText(QCoreApplication.translate("MainForm", u"\u70b9\u51fb\u62d6\u52a8\u56fe\u7247\uff0c\u4f7f\u7528\u6eda\u8f6e\u7f29\u653e(100%)", None))
        self.groupDisplaySetting.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u64cd\u4f5c", None))
        self.labelDisplayColor.setText(QCoreApplication.translate("MainForm", u" \u80cc\u666f\u989c\u8272:", None))
        self.inputDisplayType.setText(QCoreApplication.translate("MainForm", u"\u539f\u56fe\u663e\u793a", None))
        self.btnChangeDisplayType.setText(QCoreApplication.translate("MainForm", u"\u5207\u6362\u663e\u793a", None))
        self.inputDisplayColor.setText(QCoreApplication.translate("MainForm", u"\u900f\u660e", None))
        self.labelDisplayType.setText(QCoreApplication.translate("MainForm", u" \u663e\u793a\u65b9\u5f0f:", None))
        self.btnChangeDisplayColor.setText(QCoreApplication.translate("MainForm", u"\u5207\u6362\u989c\u8272", None))
    # retranslateUi

