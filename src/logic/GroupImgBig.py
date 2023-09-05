import os
from PIL import Image, ImageDraw
from logic.GroupMessage import GroupMessage
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage


class GroupImgBig:
    def __init__(self, parent):
        self.parent = parent
        self.generateBackground()

    def generateBackground(self):
        target = self.parent.labelImgBigBack
        imageWidth = target.width()
        imageHeight = target.height()
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

    def showImg(self, item: str):
        if os.path.splitext(item)[-1].lower() in (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
        ):
            pixmap = QPixmap(item)
            self.parent.labelImgBigShow.setPixmap(pixmap)
