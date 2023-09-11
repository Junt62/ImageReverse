import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtWidgets import QLabel, QFrame, QWidget, QSizePolicy

from util.ZiJun import ZiJun


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent
        self.backWidth = self.parent.labelImgSmallBack.width()
        self.backHeight = 693
        pixmap = ZiJun.generateGrid(self.backWidth, self.backHeight)
        self.parent.labelImgSmallBack.setFixedSize(self.backWidth, self.backHeight)
        self.parent.labelImgSmallBack.setPixmap(pixmap)

    def generateMatrix(self, quantity):
        # 冗余处理：0张图片时，不继续执行下面的代码
        if quantity == 0:
            return
        elif quantity % 8 == 0:
            quantity = quantity // 8
        else:
            quantity = quantity // 8 + 1

        # 获取图片列表
        imgItem = []
        for i in range(self.parent.listImgTree.topLevelItemCount()):
            imgItem.append(self.parent.listImgTree.topLevelItem(i))

        # 设置画布长度
        height = (quantity) * 72
        if height >= self.backHeight:
            pixmap = ZiJun.generateGrid(self.backWidth, height)
            self.parent.labelImgSmallBack.setFixedSize(self.backWidth, height)
            self.parent.labelImgSmallBack.setPixmap(pixmap)
        else:
            pixmap = ZiJun.generateGrid(self.backWidth, self.backHeight)
            self.parent.labelImgSmallBack.setFixedSize(self.backWidth, self.backHeight)
            self.parent.labelImgSmallBack.setPixmap(pixmap)
        self.parent.scrollAreaImgSmallWidget.setFixedHeight(height)
        self.parent.scrollAreaImgSmallWidget.setFixedWidth(
            self.parent.labelImgSmallBack.width()
        )

        # 清空grid中已有的QLabel组件
        for i in reversed(range(self.parent.scrollAreaImgSmallWidgetLayout.count())):
            item = self.parent.scrollAreaImgSmallWidgetLayout.itemAt(i)
            if item.widget().objectName() == "labelImgSmallBack":
                continue
            if item.widget() is not None:
                item.widget().deleteLater()

        # 生成画布格子，并展示预览图
        labels = {}
        i = 0
        for row in range(quantity):
            for col in range(8):
                if i < len(imgItem):
                    # 创建并设置QLabel属性
                    label = QLabel()
                    label.setMinimumSize(72, 72)
                    label.setMaximumSize(72, 72)
                    label.setFrameShape(QFrame.Panel)
                    label.setFrameShadow(QFrame.Raised)
                    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.parent.scrollAreaImgSmallWidgetLayout.addWidget(
                        label, row, col
                    )

                    # 创建并设置pixmap属性
                    img = QImage(os.path.join(imgItem[i].text(2), imgItem[i].text(1)))
                    pixmap = QPixmap.fromImage(img)
                    pixmap = pixmap.scaled(
                        label.width(),
                        label.height(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation,
                    )
                    label.setPixmap(pixmap)
                    labels[(col, row)] = label
                    i += 1

    def showImg(self, quantity):
        self.generateMatrix(quantity)
