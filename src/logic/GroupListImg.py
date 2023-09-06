import os
from PySide6.QtWidgets import QTreeWidgetItem
from logic.GroupImgBig import GroupImgBig
from logic.GroupImgSmall import GroupImgSmall
from logic.GroupMessage import GroupMessage
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class GroupListImg:
    def __init__(self, parent):
        self.parent = parent
        self.groupMessage = GroupMessage(self.parent)
        self.groupImgBig = GroupImgBig(self.parent)
        self.groupImgSmall = GroupImgSmall(self.parent)
        self.parent.listImgTree.currentItemChanged.connect(
            self.listImgTreeCurrentItemChanged
        )

    def loadImage(self, path):
        start = path
        self.parent.listImgTree.clear()
        first = True
        count = 0
        temp = [start]
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
                    count += 1
                    item = QTreeWidgetItem(self.parent.listImgTree, [name, current])
                    self.parent.listImgTree.addTopLevelItem(item)
                    if first:
                        self.parent.listImgTree.setCurrentItem(item)
                        first = False
        self.groupImgSmall.showImg(count)
        self.groupMessage.successMessage(f"读取文件夹完成，发现 {count} 张图片")

    def listImgTreeCurrentItemChanged(self):
        item = self.parent.listImgTree.currentItem()
        if item:
            self.groupImgBig.showImg(item.text(1) + "\\" + item.text(0))
