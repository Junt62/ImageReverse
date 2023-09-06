import os
from PIL import Image, ImageDraw
from logic.GroupMessage import GroupMessage
from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QPixmap, QImage, QPainter, QWheelEvent
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class GroupImgBig:
    def __init__(self, parent):
        self.parent = parent
        self.dragOffset = None
        self.parent.scrollAreaImgBig.setCursor(Qt.SizeAllCursor)
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
            self.parent.pixmap = QPixmap(item)
            self.parent.labelImgBigShow.setPixmap(self.parent.pixmap)
            scrollWidth = self.parent.scrollAreaImgBig.width()
            scrollHeight = self.parent.scrollAreaImgBig.height()
            pixmapWidth = self.parent.pixmap.width()
            pixmapHeight = self.parent.pixmap.height()
            self.parent.labelImgBigShow.setFixedSize(pixmapWidth * 4, pixmapHeight * 4)
            pos = QPoint(
                -(pixmapWidth * 2 - scrollWidth / 2),
                -(pixmapHeight * 2 - scrollHeight / 2),
            )
            self.parent.labelImgBigShow.move(pos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragOffset = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragOffset = QPoint()

    def mouseMoveEvent(self, event):
        if (
            event.buttons() == Qt.LeftButton
            and not self.parent.labelImgBigShow.pixmap().isNull()
        ):
            newPos = self.parent.labelImgBigShow.pos() + event.pos() - self.dragOffset
            self.parent.labelImgBigShow.move(newPos)
            self.dragOffset = event.pos()

    def wheelEvent(self, event: QWheelEvent):
        pixmapSize = self.parent.labelImgBigShow.pixmap().size()
        angle = event.angleDelta().y()
        if angle > 0:
            pixmapSize += QSize(
                self.parent.pixmap.width() * 0.1, self.parent.pixmap.height() * 0.1
            )
        else:
            pixmapSize -= QSize(
                self.parent.pixmap.width() * 0.1, self.parent.pixmap.height() * 0.1
            )
        newPixmap = self.parent.pixmap.scaled(pixmapSize)
        self.parent.labelImgBigShow.setPixmap(newPixmap)
