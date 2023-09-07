import os
from PIL import Image, ImageDraw
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QImage, QWheelEvent


class GroupImgBig:
    def __init__(self, parent):
        self.parent = parent
        self.generateBackground()
        self.dragOffset = QPoint()
        self.parent.labelOffset = QPoint()
        self.parent.pixmapScale = 100
        self.parent.scrollAreaImgBig.setCursor(Qt.SizeAllCursor)
        self.parent.scrollAreaImgBig.mousePressEvent = self.mousePressEvent
        self.parent.scrollAreaImgBig.mouseReleaseEvent = self.mouseReleaseEvent
        self.parent.scrollAreaImgBig.mouseMoveEvent = self.mouseMoveEvent
        self.parent.scrollAreaImgBig.wheelEvent = self.wheelEvent

    def generateBackground(self):
        imageWidth = self.parent.labelImgBigBack.width()
        imageHeight = self.parent.labelImgBigBack.height()
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
        self.parent.labelImgBigBack.setPixmap(QPixmap.fromImage(qtImage))

    def showImg(self, item: str):
        if os.path.splitext(item)[-1].lower() in (
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
        ):
            self.parent.pixmap = QPixmap(item)

            # 设置pixmap的缩放
            scaledPixmap = self.parent.pixmap.scaled(
                self.parent.pixmap.width() * (self.parent.pixmapScale / 100),
                self.parent.pixmap.height() * (self.parent.pixmapScale / 100),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.parent.labelImgBigShow.setPixmap(scaledPixmap)
            self.parent.labelImgBigText.setText(
                f"点击拖动图片，使用滚轮缩放({self.parent.pixmapScale}%)"
            )

            # 设置label的大小
            pixmapWidth = self.parent.pixmap.width()
            pixmapHeight = self.parent.pixmap.height()
            self.parent.labelImgBigShow.setFixedSize(pixmapWidth * 4, pixmapHeight * 4)

            # 设置label的位置
            pos = QPoint(
                -(pixmapWidth * 2 - self.parent.scrollAreaImgBig.width() / 2),
                -(pixmapHeight * 2 - self.parent.scrollAreaImgBig.height() / 2),
            )
            self.parent.labelImgBigShow.move(pos + self.parent.labelOffset)

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
            # 拖动pixmap时计算的偏移
            newPos = self.parent.labelImgBigShow.pos() + event.pos() - self.dragOffset
            self.parent.labelImgBigShow.move(newPos)

            # 记录偏移，使得每次更新pixmap时保留原来的位置
            self.parent.labelOffset = (
                self.parent.labelOffset + event.pos() - self.dragOffset
            )

            self.dragOffset = event.pos()

    def wheelEvent(self, event: QWheelEvent):
        if not self.parent.labelImgBigShow.pixmap().isNull():
            angle = event.angleDelta().y()
            if angle > 0:
                if self.parent.pixmapScale >= 1600:
                    self.parent.pixmapScale = 1600
                else:
                    self.parent.pixmapScale += 5
            else:
                if self.parent.pixmapScale < 50:
                    self.parent.pixmapScale -= 1
                    if self.parent.pixmapScale <= 1:
                        self.parent.pixmapScale = 1
                else:
                    self.parent.pixmapScale -= 5
            scaledPixmap = self.parent.pixmap.scaled(
                self.parent.pixmap.width() * (self.parent.pixmapScale / 100),
                self.parent.pixmap.height() * (self.parent.pixmapScale / 100),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.parent.labelImgBigShow.setPixmap(scaledPixmap)
            self.parent.labelImgBigText.setText(
                f"点击拖动图片，使用滚轮缩放({self.parent.pixmapScale}%)"
            )
