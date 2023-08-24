# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageReverse.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
import resources.resources_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(380, 220)
        Form.setMinimumSize(QSize(380, 220))
        Form.setMaximumSize(QSize(380, 600))
        icon = QIcon()
        icon.addFile(":/pictures/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 361, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 10)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.labelTarget = QLabel(self.verticalLayoutWidget)
        self.labelTarget.setObjectName("labelTarget")

        self.horizontalLayout_1.addWidget(self.labelTarget)

        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputTarget = QLineEdit(self.verticalLayoutWidget)
        self.inputTarget.setObjectName("inputTarget")

        self.horizontalLayout_2.addWidget(self.inputTarget)

        self.btnSelectTarget = QPushButton(self.verticalLayoutWidget)
        self.btnSelectTarget.setObjectName("btnSelectTarget")

        self.horizontalLayout_2.addWidget(self.btnSelectTarget)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelResult = QLabel(self.verticalLayoutWidget)
        self.labelResult.setObjectName("labelResult")

        self.horizontalLayout_3.addWidget(self.labelResult)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.inputResult = QLineEdit(self.verticalLayoutWidget)
        self.inputResult.setObjectName("inputResult")
        self.inputResult.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.inputResult)

        self.btnSelectResult = QPushButton(self.verticalLayoutWidget)
        self.btnSelectResult.setObjectName("btnSelectResult")
        self.btnSelectResult.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btnSelectResult)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelResetTarget = QLabel(self.verticalLayoutWidget)
        self.labelResetTarget.setObjectName("labelResetTarget")

        self.horizontalLayout_5.addWidget(self.labelResetTarget)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.barResetTarget = QProgressBar(self.verticalLayoutWidget)
        self.barResetTarget.setObjectName("barResetTarget")
        self.barResetTarget.setEnabled(False)
        self.barResetTarget.setValue(0)
        self.barResetTarget.setAlignment(Qt.AlignCenter)
        self.barResetTarget.setTextVisible(True)

        self.horizontalLayout_6.addWidget(self.barResetTarget)

        self.btnResetTarget = QPushButton(self.verticalLayoutWidget)
        self.btnResetTarget.setObjectName("btnResetTarget")
        self.btnResetTarget.setEnabled(False)
        self.btnResetTarget.setAutoDefault(False)
        self.btnResetTarget.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btnResetTarget)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelImageReverse = QLabel(self.verticalLayoutWidget)
        self.labelImageReverse.setObjectName("labelImageReverse")

        self.horizontalLayout_7.addWidget(self.labelImageReverse)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.barImageReverse = QProgressBar(self.verticalLayoutWidget)
        self.barImageReverse.setObjectName("barImageReverse")
        self.barImageReverse.setEnabled(False)
        self.barImageReverse.setValue(0)
        self.barImageReverse.setAlignment(Qt.AlignCenter)
        self.barImageReverse.setTextVisible(True)

        self.horizontalLayout_8.addWidget(self.barImageReverse)

        self.btnImageReverse = QPushButton(self.verticalLayoutWidget)
        self.btnImageReverse.setObjectName("btnImageReverse")
        self.btnImageReverse.setEnabled(False)
        self.btnImageReverse.setAutoDefault(False)
        self.btnImageReverse.setFlat(False)

        self.horizontalLayout_8.addWidget(self.btnImageReverse)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.retranslateUi(Form)

        self.btnResetTarget.setDefault(False)
        self.btnImageReverse.setDefault(False)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", "\u5e8f\u5217\u5e27\u56fe\u7247\u7ffb\u8f6c\u5de5\u5177", None
            )
        )
        self.labelTarget.setText(
            QCoreApplication.translate(
                "Form", "(1)\u8bf7\u8bbe\u7f6e\u76ee\u6807\u8def\u5f84\uff1a", None
            )
        )
        self.btnSelectTarget.setText(
            QCoreApplication.translate("Form", "\u9009\u62e9\u8def\u5f84", None)
        )
        self.labelResult.setText(
            QCoreApplication.translate(
                "Form", "(2)\u5904\u7406\u540e\u56fe\u7247\u8def\u5f84\uff1a", None
            )
        )
        self.btnSelectResult.setText(
            QCoreApplication.translate("Form", "\u4fdd\u5b58\u4f4d\u7f6e", None)
        )
        self.labelResetTarget.setText(
            QCoreApplication.translate(
                "Form", "(3)\u8c03\u6574\u56fe\u7247\u7ed3\u6784\uff1a", None
            )
        )
        self.btnResetTarget.setText(
            QCoreApplication.translate("Form", "\u8c03\u6574\u7ed3\u6784", None)
        )
        self.labelImageReverse.setText(
            QCoreApplication.translate(
                "Form", "(4)\u7ffb\u8f6c\u5e8f\u5217\u5e27\u56fe\u7247\uff1a", None
            )
        )
        self.btnImageReverse.setText(
            QCoreApplication.translate("Form", "\u7ffb\u8f6c\u56fe\u7247", None)
        )

    # retranslateUi
