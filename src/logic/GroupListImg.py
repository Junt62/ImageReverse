import os
from PySide6.QtWidgets import QTreeWidgetItem, QLineEdit
from PySide6.QtGui import QFontMetrics

from util.ZiJun import ZiJun


class GroupListImg:
    def __init__(self, parent):
        self.parent = parent
        self.parent.listImgTree.currentItemChanged.connect(
            self.listImgTreeCurrentItemChanged
        )
        self.generateTable()

    def loadImage(self):
        self.parent.listImgTree.clear()
        maxWidth = [32, 80, 100]
        first = True
        image = ZiJun.loadImage(self.parent.inputImgPath.text())

        for index, path in enumerate(image):
            # 读取项目与生成项目
            file = os.path.basename(path)
            path = os.path.dirname(path)
            itemList = [str(index), file, path]
            item = QTreeWidgetItem(self.parent.listImgTree, itemList)

            # 获取项目列表中最大列宽
            for i in range(3):
                fontMatrics = QFontMetrics(self.parent.listImgTree.font())
                textWidth = fontMatrics.horizontalAdvance(itemList[i])
                maxWidth[i] = max(maxWidth[i], textWidth)

            # 如果是第一次生成项目，那么选中当前项目
            if first:
                first = False
                self.parent.listImgTree.setCurrentItem(item)

        # 设置列宽
        for i in range(3):
            self.parent.listImgTree.setColumnWidth(i, maxWidth[i] + 10)

        # 调用函数显示小预览图
        self.parent.groupImgSmall.showImg(len(image))
        self.parent.groupMessage.successMessage(f"读取文件夹完成，发现 {len(image)} 张图片")

    def generateTable(self):
        # 设置列标题
        self.parent.listImgTree.setColumnCount(3)
        self.parent.listImgTree.setHeaderLabels(["序号", "名称", "路径"])

        # 隐藏树根节点
        self.parent.listImgTree.setIndentation(0)

        # 设置基础列宽
        self.parent.listImgTree.setColumnWidth(0, 42)
        self.parent.listImgTree.setColumnWidth(1, 90)
        self.parent.listImgTree.setColumnWidth(2, 110)

    def listImgTreeCurrentItemChanged(self):
        item = self.parent.listImgTree.currentItem()
        if item:
            self.parent.groupImgBig.showImg(os.path.join(item.text(2), item.text(1)))
