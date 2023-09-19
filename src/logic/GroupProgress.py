import os, shutil
from PIL import Image
from contextlib import contextmanager

from util.ZiJun import ZiJun


class GroupProgress:
    def __init__(self, parent):
        self.parent = parent

        self.backgroundColor = "transparent"

        self.parent.btnReadPosition.clicked.connect(self.btnReadPositionClicked)
        self.parent.btnChangeStructure.clicked.connect(self.btnChangeStructureClicked)
        self.parent.btnImgReverse.clicked.connect(self.btnImgReverseClicked)
        self.parent.btnChangeDisplayColor.clicked.connect(
            self.btnChangeDisplayColorClicked
        )
        self.isShowImg = False

    def btnReadPositionClicked(self):
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

    def btnChangeDisplayColorClicked(self):
        ZiJun.changeBackground(ZiJun, self.backWidth, self.backHeight)

        if self.backgroundColor == "black":
            self.backgroundColor = "white"
            return ZiJun.generateColor(width, height, QColor(0, 0, 0))
        elif self.backgroundColor == "white":
            self.backgroundColor = "red"
            return ZiJun.generateColor(width, height, QColor(255, 255, 255))
        elif self.backgroundColor == "red":
            self.backgroundColor = "green"
            return ZiJun.generateColor(width, height, QColor(255, 0, 0))
        elif self.backgroundColor == "green":
            self.backgroundColor = "blue"
            return ZiJun.generateColor(width, height, QColor(0, 255, 0))
        elif self.backgroundColor == "blue":
            self.backgroundColor = "grid"
            return ZiJun.generateColor(width, height, QColor(0, 0, 255))
        elif self.backgroundColor == "grid":
            self.backgroundColor = "black"
            return ZiJun.generateGrid(width, height)
