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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QWidget)
import res.resources_rc

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(1257, 720)
        MainForm.setMinimumSize(QSize(1257, 720))
        MainForm.setMaximumSize(QSize(1257, 720))
        icon = QIcon()
        icon.addFile(u":/picture/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.gridLayoutWidget = QWidget(MainForm)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1260, 721))
        self.MainFormLayout = QGridLayout(self.gridLayoutWidget)
        self.MainFormLayout.setObjectName(u"MainFormLayout")
        self.MainFormLayout.setHorizontalSpacing(4)
        self.MainFormLayout.setVerticalSpacing(0)
        self.MainFormLayout.setContentsMargins(4, 0, 4, 4)
        self.groupDisplaySetting = QGroupBox(self.gridLayoutWidget)
        self.groupDisplaySetting.setObjectName(u"groupDisplaySetting")
        self.groupDisplaySetting.setMaximumSize(QSize(240, 16777215))
        self.groupDisplaySettingLayout = QGridLayout(self.groupDisplaySetting)
        self.groupDisplaySettingLayout.setSpacing(2)
        self.groupDisplaySettingLayout.setObjectName(u"groupDisplaySettingLayout")
        self.groupDisplaySettingLayout.setContentsMargins(3, 0, 3, 3)
        self.inputDisplayType = QLineEdit(self.groupDisplaySetting)
        self.inputDisplayType.setObjectName(u"inputDisplayType")
        self.inputDisplayType.setReadOnly(True)

        self.groupDisplaySettingLayout.addWidget(self.inputDisplayType, 1, 1, 1, 2)

        self.btnChangeDisplayType = QPushButton(self.groupDisplaySetting)
        self.btnChangeDisplayType.setObjectName(u"btnChangeDisplayType")

        self.groupDisplaySettingLayout.addWidget(self.btnChangeDisplayType, 1, 3, 1, 1)

        self.labelDisplayType = QLabel(self.groupDisplaySetting)
        self.labelDisplayType.setObjectName(u"labelDisplayType")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDisplayType.sizePolicy().hasHeightForWidth())
        self.labelDisplayType.setSizePolicy(sizePolicy)

        self.groupDisplaySettingLayout.addWidget(self.labelDisplayType, 1, 0, 1, 1)

        self.labelDisplayColor = QLabel(self.groupDisplaySetting)
        self.labelDisplayColor.setObjectName(u"labelDisplayColor")
        sizePolicy.setHeightForWidth(self.labelDisplayColor.sizePolicy().hasHeightForWidth())
        self.labelDisplayColor.setSizePolicy(sizePolicy)

        self.groupDisplaySettingLayout.addWidget(self.labelDisplayColor, 3, 0, 1, 1)

        self.inputDisplayColor = QLineEdit(self.groupDisplaySetting)
        self.inputDisplayColor.setObjectName(u"inputDisplayColor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputDisplayColor.sizePolicy().hasHeightForWidth())
        self.inputDisplayColor.setSizePolicy(sizePolicy1)
        self.inputDisplayColor.setReadOnly(True)

        self.groupDisplaySettingLayout.addWidget(self.inputDisplayColor, 3, 1, 1, 2)

        self.btnChangeDisplayColor = QPushButton(self.groupDisplaySetting)
        self.btnChangeDisplayColor.setObjectName(u"btnChangeDisplayColor")

        self.groupDisplaySettingLayout.addWidget(self.btnChangeDisplayColor, 3, 3, 1, 1)


        self.MainFormLayout.addWidget(self.groupDisplaySetting, 1, 0, 1, 1)

        self.groupPath = QGroupBox(self.gridLayoutWidget)
        self.groupPath.setObjectName(u"groupPath")
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


        self.MainFormLayout.addWidget(self.groupPath, 0, 0, 1, 2)

        self.groupProgress = QGroupBox(self.gridLayoutWidget)
        self.groupProgress.setObjectName(u"groupProgress")
        self.groupProgress.setMaximumSize(QSize(240, 16777215))
        self.groupProgressLayout = QGridLayout(self.groupProgress)
        self.groupProgressLayout.setSpacing(2)
        self.groupProgressLayout.setObjectName(u"groupProgressLayout")
        self.groupProgressLayout.setContentsMargins(3, 0, 3, 3)
        self.inputPositionNewY = QLineEdit(self.groupProgress)
        self.inputPositionNewY.setObjectName(u"inputPositionNewY")
        sizePolicy1.setHeightForWidth(self.inputPositionNewY.sizePolicy().hasHeightForWidth())
        self.inputPositionNewY.setSizePolicy(sizePolicy1)

        self.groupProgressLayout.addWidget(self.inputPositionNewY, 1, 3, 1, 1)

        self.btnReadPosition = QPushButton(self.groupProgress)
        self.btnReadPosition.setObjectName(u"btnReadPosition")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnReadPosition.sizePolicy().hasHeightForWidth())
        self.btnReadPosition.setSizePolicy(sizePolicy2)

        self.groupProgressLayout.addWidget(self.btnReadPosition, 2, 0, 1, 1)

        self.inputPositionNewX = QLineEdit(self.groupProgress)
        self.inputPositionNewX.setObjectName(u"inputPositionNewX")
        sizePolicy1.setHeightForWidth(self.inputPositionNewX.sizePolicy().hasHeightForWidth())
        self.inputPositionNewX.setSizePolicy(sizePolicy1)

        self.groupProgressLayout.addWidget(self.inputPositionNewX, 1, 2, 1, 1)

        self.inputPositionOldY = QLineEdit(self.groupProgress)
        self.inputPositionOldY.setObjectName(u"inputPositionOldY")
        sizePolicy1.setHeightForWidth(self.inputPositionOldY.sizePolicy().hasHeightForWidth())
        self.inputPositionOldY.setSizePolicy(sizePolicy1)

        self.groupProgressLayout.addWidget(self.inputPositionOldY, 0, 3, 1, 1)

        self.btnSpace1 = QPushButton(self.groupProgress)
        self.btnSpace1.setObjectName(u"btnSpace1")
        sizePolicy2.setHeightForWidth(self.btnSpace1.sizePolicy().hasHeightForWidth())
        self.btnSpace1.setSizePolicy(sizePolicy2)

        self.groupProgressLayout.addWidget(self.btnSpace1, 5, 0, 1, 1)

        self.labelPositionOld = QLabel(self.groupProgress)
        self.labelPositionOld.setObjectName(u"labelPositionOld")
        sizePolicy.setHeightForWidth(self.labelPositionOld.sizePolicy().hasHeightForWidth())
        self.labelPositionOld.setSizePolicy(sizePolicy)

        self.groupProgressLayout.addWidget(self.labelPositionOld, 0, 0, 1, 2)

        self.btnApplyPosition = QPushButton(self.groupProgress)
        self.btnApplyPosition.setObjectName(u"btnApplyPosition")
        sizePolicy2.setHeightForWidth(self.btnApplyPosition.sizePolicy().hasHeightForWidth())
        self.btnApplyPosition.setSizePolicy(sizePolicy2)

        self.groupProgressLayout.addWidget(self.btnApplyPosition, 2, 2, 1, 1)

        self.labelPositionNew = QLabel(self.groupProgress)
        self.labelPositionNew.setObjectName(u"labelPositionNew")
        sizePolicy.setHeightForWidth(self.labelPositionNew.sizePolicy().hasHeightForWidth())
        self.labelPositionNew.setSizePolicy(sizePolicy)

        self.groupProgressLayout.addWidget(self.labelPositionNew, 1, 0, 1, 1)

        self.btnImgReverse = QPushButton(self.groupProgress)
        self.btnImgReverse.setObjectName(u"btnImgReverse")
        sizePolicy2.setHeightForWidth(self.btnImgReverse.sizePolicy().hasHeightForWidth())
        self.btnImgReverse.setSizePolicy(sizePolicy2)

        self.groupProgressLayout.addWidget(self.btnImgReverse, 5, 3, 1, 1)

        self.btnImgAlignment = QPushButton(self.groupProgress)
        self.btnImgAlignment.setObjectName(u"btnImgAlignment")
        sizePolicy2.setHeightForWidth(self.btnImgAlignment.sizePolicy().hasHeightForWidth())
        self.btnImgAlignment.setSizePolicy(sizePolicy2)

        self.groupProgressLayout.addWidget(self.btnImgAlignment, 2, 3, 1, 1)

        self.btnStructure = QPushButton(self.groupProgress)
        self.btnStructure.setObjectName(u"btnStructure")
        sizePolicy2.setHeightForWidth(self.btnStructure.sizePolicy().hasHeightForWidth())
        self.btnStructure.setSizePolicy(sizePolicy2)

        self.groupProgressLayout.addWidget(self.btnStructure, 5, 2, 1, 1)

        self.inputPositionOldX = QLineEdit(self.groupProgress)
        self.inputPositionOldX.setObjectName(u"inputPositionOldX")
        sizePolicy1.setHeightForWidth(self.inputPositionOldX.sizePolicy().hasHeightForWidth())
        self.inputPositionOldX.setSizePolicy(sizePolicy1)

        self.groupProgressLayout.addWidget(self.inputPositionOldX, 0, 2, 1, 1)


        self.MainFormLayout.addWidget(self.groupProgress, 2, 0, 1, 1)

        self.groupImgTable = QGroupBox(self.gridLayoutWidget)
        self.groupImgTable.setObjectName(u"groupImgTable")
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
        self.scrollImgTableWidgetLayout = QGridLayout(self.scrollImgTableWidget)
        self.scrollImgTableWidgetLayout.setSpacing(0)
        self.scrollImgTableWidgetLayout.setObjectName(u"scrollImgTableWidgetLayout")
        self.scrollImgTableWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImgTableBack = QLabel(self.scrollImgTableWidget)
        self.labelImgTableBack.setObjectName(u"labelImgTableBack")
        self.labelImgTableBack.setFrameShape(QFrame.Panel)
        self.labelImgTableBack.setFrameShadow(QFrame.Raised)
        self.labelImgTableBack.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.scrollImgTableWidgetLayout.addWidget(self.labelImgTableBack, 0, 0, 1, 1)

        self.scrollImgTable.setWidget(self.scrollImgTableWidget)

        self.groupImgSmallLayout.addWidget(self.scrollImgTable, 0, 2, 1, 1)


        self.MainFormLayout.addWidget(self.groupImgTable, 0, 2, 5, 1)

        self.groupListImg = QGroupBox(self.gridLayoutWidget)
        self.groupListImg.setObjectName(u"groupListImg")
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


        self.MainFormLayout.addWidget(self.groupListImg, 4, 0, 1, 2)

        self.groupMessage = QGroupBox(self.gridLayoutWidget)
        self.groupMessage.setObjectName(u"groupMessage")
        self.groupMessage.setMaximumSize(QSize(240, 16777215))
        self.groupMessageLayout = QGridLayout(self.groupMessage)
        self.groupMessageLayout.setSpacing(0)
        self.groupMessageLayout.setObjectName(u"groupMessageLayout")
        self.groupMessageLayout.setContentsMargins(4, 0, 4, 5)
        self.inputMessage = QTextEdit(self.groupMessage)
        self.inputMessage.setObjectName(u"inputMessage")
        self.inputMessage.setReadOnly(True)
        self.inputMessage.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.groupMessageLayout.addWidget(self.inputMessage, 0, 0, 1, 1)


        self.MainFormLayout.addWidget(self.groupMessage, 3, 0, 1, 1)

        self.groupImgPreview = QGroupBox(self.gridLayoutWidget)
        self.groupImgPreview.setObjectName(u"groupImgPreview")
        self.groupImgPreview.setMinimumSize(QSize(396, 0))
        self.groupImgPreview.setMaximumSize(QSize(396, 16777215))
        self.groupImgPreviewLayout = QGridLayout(self.groupImgPreview)
        self.groupImgPreviewLayout.setSpacing(1)
        self.groupImgPreviewLayout.setObjectName(u"groupImgPreviewLayout")
        self.groupImgPreviewLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.groupImgPreviewLayout.setContentsMargins(4, 0, 4, 4)
        self.scrollImgPreview = QScrollArea(self.groupImgPreview)
        self.scrollImgPreview.setObjectName(u"scrollImgPreview")
        self.scrollImgPreview.setMinimumSize(QSize(386, 0))
        self.scrollImgPreview.setMaximumSize(QSize(386, 16777215))
        self.scrollImgPreview.viewport().setProperty("cursor", QCursor(Qt.SizeAllCursor))
        self.scrollImgPreview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollImgPreview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollImgPreview.setWidgetResizable(True)
        self.scrollImgPreviewWidget = QWidget()
        self.scrollImgPreviewWidget.setObjectName(u"scrollImgPreviewWidget")
        self.scrollImgPreviewWidget.setGeometry(QRect(0, 0, 384, 392))
        self.labelImgPreviewShow = QLabel(self.scrollImgPreviewWidget)
        self.labelImgPreviewShow.setObjectName(u"labelImgPreviewShow")
        self.labelImgPreviewShow.setGeometry(QRect(0, 0, 384, 401))
        self.labelImgPreviewShow.setAlignment(Qt.AlignCenter)
        self.labelImgPreviewBack = QLabel(self.scrollImgPreviewWidget)
        self.labelImgPreviewBack.setObjectName(u"labelImgPreviewBack")
        self.labelImgPreviewBack.setGeometry(QRect(0, 0, 384, 401))
        self.labelImgPreviewBack.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollImgPreviewWidgetLayout = QGridLayout(self.scrollImgPreviewWidget)
        self.scrollImgPreviewWidgetLayout.setSpacing(0)
        self.scrollImgPreviewWidgetLayout.setObjectName(u"scrollImgPreviewWidgetLayout")
        self.scrollImgPreviewWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.labelImgPreviewText = QLabel(self.scrollImgPreviewWidget)
        self.labelImgPreviewText.setObjectName(u"labelImgPreviewText")
        self.labelImgPreviewText.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.scrollImgPreviewWidgetLayout.addWidget(self.labelImgPreviewText, 0, 0, 1, 1)

        self.scrollImgPreview.setWidget(self.scrollImgPreviewWidget)
        self.labelImgPreviewBack.raise_()
        self.labelImgPreviewShow.raise_()
        self.labelImgPreviewText.raise_()

        self.groupImgPreviewLayout.addWidget(self.scrollImgPreview, 0, 0, 1, 1)

        self.groupImgPreviewLayout.setColumnStretch(0, 3)

        self.MainFormLayout.addWidget(self.groupImgPreview, 1, 1, 3, 1)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"\u5e8f\u5217\u5e27\u56fe\u7247\u7ffb\u8f6c\u5de5\u5177", None))
        self.groupDisplaySetting.setTitle(QCoreApplication.translate("MainForm", u"\u9884\u89c8\u8bbe\u7f6e", None))
        self.inputDisplayType.setText(QCoreApplication.translate("MainForm", u"\u539f\u56fe\u663e\u793a", None))
        self.btnChangeDisplayType.setText(QCoreApplication.translate("MainForm", u"\u5207\u6362\u663e\u793a", None))
        self.labelDisplayType.setText(QCoreApplication.translate("MainForm", u" \u663e\u793a\u65b9\u5f0f:", None))
        self.labelDisplayColor.setText(QCoreApplication.translate("MainForm", u" \u80cc\u666f\u989c\u8272:", None))
        self.inputDisplayColor.setText(QCoreApplication.translate("MainForm", u"\u900f\u660e", None))
        self.btnChangeDisplayColor.setText(QCoreApplication.translate("MainForm", u"\u5207\u6362\u80cc\u666f", None))
        self.groupPath.setTitle(QCoreApplication.translate("MainForm", u"\u8def\u5f84\u9009\u62e9", None))
        self.btnImgPath.setText(QCoreApplication.translate("MainForm", u"\u7d20\u6750\u8def\u5f84", None))
        self.btnSavePath.setText(QCoreApplication.translate("MainForm", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.groupProgress.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u64cd\u4f5c", None))
        self.inputPositionNewY.setText(QCoreApplication.translate("MainForm", u"Y=0", None))
        self.btnReadPosition.setText(QCoreApplication.translate("MainForm", u"\u8bfb\u53d6\u5750\u6807", None))
        self.inputPositionNewX.setText(QCoreApplication.translate("MainForm", u"X=0", None))
        self.inputPositionOldY.setText(QCoreApplication.translate("MainForm", u"Y=0", None))
        self.btnSpace1.setText(QCoreApplication.translate("MainForm", u"\u4fdd\u7559\u6309\u94ae", None))
        self.labelPositionOld.setText(QCoreApplication.translate("MainForm", u" \u539f\u59cb\u5750\u6807:", None))
        self.btnApplyPosition.setText(QCoreApplication.translate("MainForm", u"\u5e94\u7528\u5750\u6807", None))
        self.labelPositionNew.setText(QCoreApplication.translate("MainForm", u" \u65b0\u7684\u5750\u6807:", None))
        self.btnImgReverse.setText(QCoreApplication.translate("MainForm", u"\u7ffb\u8f6c\u56fe\u7247", None))
        self.btnImgAlignment.setText(QCoreApplication.translate("MainForm", u"\u5bf9\u9f50\u56fe\u7247", None))
        self.btnStructure.setText(QCoreApplication.translate("MainForm", u"\u8c03\u6574\u7ed3\u6784", None))
        self.inputPositionOldX.setText(QCoreApplication.translate("MainForm", u"X=0", None))
        self.groupImgTable.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u5217\u8868", None))
        self.groupListImg.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u5217\u8868", None))
        self.groupMessage.setTitle(QCoreApplication.translate("MainForm", u"\u6d88\u606f\u8f93\u51fa", None))
        self.groupImgPreview.setTitle(QCoreApplication.translate("MainForm", u"\u56fe\u7247\u9884\u89c8", None))
        self.labelImgPreviewText.setText(QCoreApplication.translate("MainForm", u"\u70b9\u51fb\u62d6\u52a8\u56fe\u7247\uff0c\u4f7f\u7528\u6eda\u8f6e\u7f29\u653e(100%)", None))
    # retranslateUi

