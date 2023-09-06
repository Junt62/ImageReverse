from logic.GroupMessage import GroupMessage
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QLabel, QFrame
import sys
from PIL import Image, ImageDraw


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent
        self.groupMessage = GroupMessage(self.parent)
        self.generateBackground(551)
        # self.showImg(12)

    def generateBackground(self, height):
        target = self.parent.labelImgSmallBack
        imageWidth = 401
        imageHeight = height
        cellSize = 10
        image = Image.new("RGB", (imageWidth, imageHeight), "white")
        draw = ImageDraw.Draw(image)
        for x in range(0, imageWidth, cellSize):
            for y in range(0, imageHeight, cellSize):
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
        target.setFixedSize(imageWidth, imageHeight)
        target.setPixmap(QPixmap.fromImage(qtImage))

    def generateMatrix(self, quantity):
        if quantity != 0:
            rows = quantity // 4 + 1
        else:
            rows = 0
        labels = {}
        i = 0
        for row in range(rows):
            for col in range(4):
                i += 1
                label = QLabel(str(i), self.parent.scrollAreaImgSmallWidget)
                label.setGeometry(col * 100 - 1, row * 100 - 1, 101, 101)
                label.setFrameShape(QFrame.StyledPanel)
                print(i, label.parent())
                item = self.parent.listImgTree.currentItem()
                if item:
                    img = QImage(item.text(1) + "\\" + item.text(0))
                    pixmap = QPixmap.fromImage(img)
                    label.setPixmap(pixmap)
                labels[(col, row)] = label
        a = self.parent.scrollAreaImgSmallWidget.findChildren(QLabel)
        # for child in a:
        #     print(child.text())
        height = (rows) * 100
        if height <= 551:
            self.parent.scrollAreaImgSmallWidget.setFixedHeight(549)
            self.generateBackground(551)
        else:
            self.parent.scrollAreaImgSmallWidget.setFixedHeight(height - 2)
            self.generateBackground(height)

    def showImg(self, quantity):
        self.generateMatrix(quantity)
