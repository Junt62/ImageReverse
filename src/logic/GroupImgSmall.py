from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtWidgets import QLabel, QFrame, QWidget, QSizePolicy
from PIL import Image, ImageDraw


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent
        self.backgroundHeight = 693
        self.generateBackground()

    def generateBackground(self, height=693):
        width = self.parent.labelImgSmallBack.width()
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        cellSize = 10
        for x in range(0, width, cellSize):
            for y in range(0, height, cellSize):
                if (x // cellSize) % 2 == (y // cellSize) % 2:
                    draw.rectangle([x, y, x + cellSize, y + cellSize], fill="white")
                else:
                    draw.rectangle(
                        [x, y, x + cellSize, y + cellSize], fill=(204, 204, 204)
                    )
        qtImage = QImage(
            image.tobytes(),
            image.width,
            image.height,
            image.width * 3,
            QImage.Format_RGB888,
        )
        self.parent.labelImgSmallBack.setFixedSize(width, height)
        self.parent.labelImgSmallBack.setPixmap(QPixmap.fromImage(qtImage))

    def generateMatrix(self, quantity):
        # 冗余处理：0张图片时，不继续执行下面的代码
        if quantity == 0:
            return
        elif quantity % 6 == 0:
            quantity = quantity // 6
        else:
            quantity = quantity // 6 + 1

        # 获取图片列表
        listImgTree = []
        for i in range(self.parent.listImgTree.topLevelItemCount()):
            listImgTree.append(self.parent.listImgTree.topLevelItem(i))

        # 设置画布长度
        height = (quantity) * 95
        if height >= self.backgroundHeight:
            self.generateBackground(height)
        else:
            self.generateBackground(self.backgroundHeight)
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
            for col in range(6):
                if i < len(listImgTree):
                    # 创建并设置QLabel属性
                    label = QLabel()
                    label.setMinimumSize(96, 96)
                    label.setMaximumSize(96, 96)
                    label.setFrameShape(QFrame.Panel)
                    label.setFrameShadow(QFrame.Raised)
                    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.parent.scrollAreaImgSmallWidgetLayout.addWidget(
                        label, row, col
                    )

                    # 创建并设置pixmap属性
                    img = QImage(listImgTree[i].text(2) + "\\" + listImgTree[i].text(1))
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
