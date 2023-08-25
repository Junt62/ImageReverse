import os
import shutil
from tkinter import Image
from PySide6.QtWidgets import QTreeWidgetItem

from logic.GroupMessage import GroupMessage


class GroupProgress:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnReadImg.clicked.connect(self.btnReadImgClicked)
        self.parent.btnChangeStructure.clicked.connect(self.btnChangeStructureClicked)
        self.parent.btnImageReverse.clicked.connect(self.btnImageReverseClicked)

    def btnReadImgClicked(self):
        if not self.parent.inputImgPath.text():
            a = GroupMessage
            a.errorMessage("未设置素材路径")
        else:
            start = self.parent.inputImgPath.text()
            self.parent.listImgTree.clear()
            temp = [start]
            while temp:
                current = temp.pop(0)
                for name in os.listdir(current):
                    path = os.path.join(current, name)
                    item = QTreeWidgetItem(self.parent.listImgTree, [name, current])
                    self.parent.listImgTree.addTopLevelItem(item)
                    if os.path.isdir(path):
                        temp.append(path)
            GroupMessage.successMessage(self, "读取文件夹完成")

    def btnChangeStructureClicked(self):
        self.parent.newFolder = self.parent.parent.inputSavePath.text()
        self.parent.tempFolder = os.path.join(self.parent.newFolder, "temp")
        self.parent.fillFolder = os.path.join(self.parent.newFolder, "fill")
        try:
            os.mkdir(self.parent.newFolder)
        except FileExistsError:
            shutil.rmtree(self.parent.newFolder)
            os.mkdir(self.parent.newFolder)
        try:
            os.mkdir(self.parent.tempFolder)
        except FileExistsError:
            shutil.rmtree(self.parent.tempFolder)
            os.mkdir(self.parent.tempFolder)
        try:
            os.mkdir(self.parent.fillFolder)
            for i in range(600):
                value = str(i).zfill(5)
                image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
                image.save(self.parent.fillFolder + "\\" + value + ".png")
        except FileExistsError:
            shutil.rmtree(self.parent.fillFolder)
            os.mkdir(self.parent.fillFolder)
            for i in range(600):
                value = str(i).zfill(5)
                image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
                image.save(self.parent.fillFolder + "\\" + value + ".png")

    def btnImageReverseClicked(self):
        pass
