import os
from PySide6.QtWidgets import QTreeWidgetItem, QLineEdit
from PySide6.QtGui import QFontMetrics


class GroupListImg:
    def __init__(self, parent):
        self.parent = parent
        self.parent.listImgTree.currentItemChanged.connect(
            self.listImgTreeCurrentItemChanged
        )
        self.generateTable()

    def generateTable(self):
        # 设置列标题
        self.parent.listImgTree.setColumnCount(3)
        self.parent.listImgTree.setHeaderLabels(["序号", "名称", "路径"])

        # 隐藏树根节点
        self.parent.listImgTree.setIndentation(0)

        # 设置基础列宽
        self.parent.listImgTree.setColumnWidth(0, 32)
        self.parent.listImgTree.setColumnWidth(1, 80)
        self.parent.listImgTree.setColumnWidth(2, 100)

    def loadImage(self, path):
        self.parent.listImgTree.clear()
        maxWidth = [36, 60, 100]
        start = path
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
                    itemList = [str(count), name, current]
                    item = QTreeWidgetItem(self.parent.listImgTree, itemList)

                    # 获取项目列表中最大列宽
                    for i in range(3):
                        fontMatrics = QFontMetrics(self.parent.listImgTree.font())
                        textWidth = fontMatrics.horizontalAdvance(itemList[i])
                        maxWidth[i] = max(maxWidth[i], textWidth)

                    # 如果是第一次生成项目，那么选中当前项目
                    if first:
                        self.parent.listImgTree.setCurrentItem(item)
                        first = False

        # 设置列宽
        for i in range(3):
            self.parent.listImgTree.setColumnWidth(i, maxWidth[i] + 10)

        # 调用函数显示小预览图
        self.parent.groupImgSmall.showImg(count)
        self.parent.groupMessage.successMessage(f"读取文件夹完成，发现 {count} 张图片")

    def listImgTreeCurrentItemChanged(self):
        item = self.parent.listImgTree.currentItem()
        if item:
            self.parent.groupImgBig.showImg(item.text(2) + "\\" + item.text(1))
