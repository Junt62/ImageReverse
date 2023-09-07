from logic.GroupMessage import GroupMessage
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QFrame,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)
from PIL import Image, ImageDraw


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent
        self.generateBackground()

    def generateBackground(self, height=576):
        width = self.parent.labelImgSmallBack.width()
        cellSize = 10
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
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

        # 获取图片列表
        listImgTree = []
        for i in range(self.parent.listImgTree.topLevelItemCount()):
            listImgTree.append(self.parent.listImgTree.topLevelItem(i))

        # 生成画布格子，并展示预览图
        labels = {}
        i = 0
        for row in range(quantity // 8 + 1):
            for col in range(8):
                label = QLabel(self.parent.scrollAreaImgSmallWidget)
                label.setGeometry(col * 63 - 1, row * 63 - 1, 64, 64)
                label.setFrameShape(QFrame.StyledPanel)

                # self.grid55.addWidget(label)
                if i < len(listImgTree):
                    img = QImage(listImgTree[i].text(1) + "\\" + listImgTree[i].text(0))
                    label.setPixmap(QPixmap.fromImage(img))
                labels[(col, row)] = label
                i += 1

        # 设置画布的长度
        height = (quantity // 8 + 1) * 63
        if height <= 576:
            self.parent.scrollAreaImgSmallWidget.setFixedHeight(574)
            self.generateBackground()
        else:
            self.parent.scrollAreaImgSmallWidget.setFixedHeight(height - 2)
            self.generateBackground(height)

    def showImg(self, quantity):
        self.generateMatrix(quantity)
