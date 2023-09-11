import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage, QPainter, QFontMetrics
from PySide6.QtWidgets import QTreeWidgetItem, QLabel, QFrame, QWidget, QSizePolicy
from PIL import Image, ImageDraw


class ZiJun:
    def generateGrid(width: int, height: int):
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        cellSize = 8
        for x in range(0, width, cellSize):
            for y in range(0, height, cellSize):
                if (x // cellSize) % 2 == (y // cellSize) % 2:
                    draw.rectangle([x, y, x + cellSize, y + cellSize], fill="white")
                else:
                    draw.rectangle(
                        [x, y, x + cellSize, y + cellSize], fill=(204, 204, 204)
                    )
        return QPixmap.fromImage(
            QImage(
                image.tobytes(),
                image.width,
                image.height,
                image.width * 3,
                QImage.Format_RGB888,
            )
        )

    def loadImage(path):
        image = []
        temp = [path]
        while temp:
            current = temp.pop(0)
            for name in os.listdir(current):
                path = os.path.join(current, name)
                if os.path.isdir(path):
                    temp.append(path)
                if os.path.splitext(path)[-1].lower() in (
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".gif",
                    ".bmp",
                ):
                    image.append(path)
        return image
