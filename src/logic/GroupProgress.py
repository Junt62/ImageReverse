from contextlib import contextmanager
import os
import shutil
from PIL import Image
from PySide6.QtWidgets import QTreeWidgetItem
from logic.GroupListImg import GroupListImg

from logic.GroupMessage import GroupMessage


class GroupProgress:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnReadImg.clicked.connect(self.btnReadImgClicked)
        self.parent.btnChangeStructure.clicked.connect(self.btnChangeStructureClicked)
        self.parent.btnImageReverse.clicked.connect(self.btnImageReverseClicked)

    def btnReadImgClicked(self):
        if not self.parent.inputImgPath.text():
            GroupMessage.errorMessage(self, "未设置素材路径")
            return
        GroupListImg.loadImage(self)

    def btnChangeStructureClicked(self):
        if not self.parent.inputImgPath.text():
            GroupMessage.errorMessage(self, "未设置素材路径")
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

    def btnImageReverseClicked(self):
        if not self.parent.inputImgPath.text():
            GroupMessage.errorMessage(self, "未设置素材路径")
            return
        GroupMessage.normalMessage(self, "btnImageReverseClicked")

    @contextmanager
    def tryExceptFileNotFoundError(self):
        try:
            yield
        except FileNotFoundError:
            pass
