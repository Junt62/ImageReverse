from logic.GroupMessage import GroupMessage
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QLabel, QFrame
import sys
from PIL import Image, ImageDraw


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent
        self.generateBackground()
        self.generatedMatrix()

    def generateBackground(self):
        target = self.parent.labelImgSmallBack
        imageWidth = 401
        imageHeight = 551
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
        target.setPixmap(QPixmap.fromImage(qtImage))

    def generatedMatrix(self):
        labels = {}
        rows, cols = 11, 8
        for row in range(rows):
            for col in range(cols):
                label = QLabel("", self.parent.scrollAreaImgSmallWidget)
                label.setFrameShape(QFrame.StyledPanel)
                x, y = col * 50 - 1, row * 50 - 1
                label.setGeometry(x, y, 51, 51)
                labels[(col, row)] = label

    def showImg(self):
        GroupMessage.normalMessage(self, "showImgSmall")
