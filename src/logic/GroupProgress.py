import os, shutil, datetime
from PIL import Image
from contextlib import contextmanager
from PySide6.QtWidgets import QLabel, QFrame, QPushButton, QWidget


class GroupProgress:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnReadImg.clicked.connect(self.btnReadImgClicked)
        self.parent.btnChangeStructure.clicked.connect(self.btnChangeStructureClicked)
        self.parent.btnImgReverse.clicked.connect(self.btnImgReverseClicked)
        # self.button = QPushButton("init", self.parent.scrollAreaImgSmallWidget)
        # self.button.setGeometry(50, 50, 100, 30)

    def btnReadImgClicked(self):
        if not self.parent.inputImgPath.text():
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return
        elif not os.path.exists(self.parent.inputImgPath.text()):
            self.parent.groupMessage.errorMessage("素材路径不存在")
            return
        self.parent.groupListImg.loadImage(self.parent.inputImgPath.text())

    def btnChangeStructureClicked(self):
        if not self.parent.inputImgPath.text():
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return
        elif not os.path.exists(self.parent.inputImgPath.text()):
            self.parent.groupMessage.errorMessage("素材路径不存在")
            return
        self.parent.newFolder = self.parent.inputSavePath.text()
        self.parent.tempFolder = os.path.join(self.parent.newFolder, "temp")
        self.parent.fillFolder = os.path.join(self.parent.newFolder, "fill")

        with self.tryExceptFileNotFoundError():
            shutil.rmtree(self.parent.newFolder)
        with self.tryExceptFileNotFoundError():
            shutil.rmtree(self.parent.tempFolder)
        with self.tryExceptFileNotFoundError():
            shutil.rmtree(self.parent.fillFolder)
        os.mkdir(self.parent.newFolder)
        os.mkdir(self.parent.tempFolder)
        os.mkdir(self.parent.fillFolder)
        for i in range(600):
            value = str(i).zfill(5)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            image.save(self.parent.fillFolder + "\\" + value + ".png")

    def btnImgReverseClicked(self):
        # time = datetime.datetime.now().strftime("%H:%M:%S")
        # button = QPushButton(f"{time}", self.parent.scrollAreaImgSmallWidget)
        # button.setGeometry(50, 100, 100, 30)
        # for child in self.parent.scrollAreaImgSmallWidget.findChildren(QWidget):
        #     print(
        #         f"text:{child.text()}, parent:{child.parent().objectName()}, x:{child.x()}, y:{child.y()}"
        #     )
        if not self.parent.inputImgPath.text():
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return
        elif not os.path.exists(self.parent.inputImgPath.text()):
            self.parent.groupMessage.errorMessage("素材路径不存在")
            return
        self.parent.groupMessage.normalMessage("btnImgReverseClicked")

    @contextmanager
    def tryExceptFileNotFoundError(self):
        try:
            yield
        except FileNotFoundError:
            pass
