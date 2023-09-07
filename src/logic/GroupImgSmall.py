from logic.GroupMessage import GroupMessage
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QLabel, QFrame
from PIL import Image, ImageDraw
import math


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent
        self.generateBackground()
        # self.showImg(1)

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

        # 设置画布长度
        height = (quantity // 8 + 1) * 63
        if height <= 576:
            self.parent.scrollAreaImgSmallWidget.setFixedHeight(574)
            self.generateBackground()
        else:
            self.parent.scrollAreaImgSmallWidget.setFixedHeight(height - 2)
            self.generateBackground(height)

        # 将画布置于最底层
        # while self.parent.labelImgSmallBack.lower():
        #     pass

        # 生成画布格子，并展示预览图
        labels = {}
        i = 0
        for row in range(quantity // 8 + 1):
            for col in range(8):
                label = QLabel(f"{row},{col}", self.parent.scrollAreaImgSmallWidget)
                label.setGeometry(col * 63 - 1, row * 63 - 1, 64, 64)
                label.setFrameShape(QFrame.StyledPanel)

                if i < len(listImgTree):
                    img = QImage(listImgTree[i].text(1) + "\\" + listImgTree[i].text(0))
                    pixmap = QPixmap.fromImage(img)
                    ratio = pixmap.width() / pixmap.height()
                    if pixmap.width() > pixmap.height():
                        width = label.width()
                        height = math.sqrt(label.width() * ratio)
                    else:
                        width = math.sqrt(label.width() * ratio)
                        height = label.height()
                    pixmap.scaled(width, height)
                    label.setPixmap(pixmap)
                labels[(col, row)] = label
                i += 1

    def showImg(self, quantity):
        self.generateMatrix(quantity)
