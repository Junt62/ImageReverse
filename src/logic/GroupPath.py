import os
from PySide6.QtWidgets import QFileDialog

from util.ZiJun import ZiJun


class GroupPath:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnImgPath.clicked.connect(self.btnImgPathClicked)
        self.parent.btnSavePath.clicked.connect(self.btnSavePathClicked)
        self.parent.inputImgPath.editingFinished.connect(
            self.inputImgPathEditingFinished
        )

    def inputImgPathEditingFinished(self):
        self.formatPath()

    def btnImgPathClicked(self):
        if self.parent.inputImgPath.text():
            previous = self.parent.inputImgPath.text()
        else:
            previous = os.getcwd()
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", previous)
        if path:
            self.parent.inputImgPath.setText(path)
            self.formatPath()

    def btnSavePathClicked(self):
        if self.parent.inputImgPath.text():
            previous = self.parent.inputImgPath.text()
        else:
            previous = os.getcwd()
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", previous)
        if path:
            self.parent.inputImgPath.setText(path)
            self.formatPath()

    def formatPath(self):
        path = self.parent.inputImgPath.text()
        if path:
            path = path.replace("/", "\\")
            while path[-1] == "\\":
                path = path[:-1]
                if path == "":
                    break
        self.parent.inputImgPath.setText(path)

        if not path:
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return

        if not os.path.isdir(path):
            self.parent.groupMessage.errorMessage(f"错误的路径： {path}")
            return

        if len(path) == 2 and path[1] == ":":
            self.parent.groupMessage.errorMessage("不可设置盘符为素材路径")
            return

        self.parent.groupMessage.normalMessage("读取图片中...")

        folder = path.split("\\")[-1]
        self.parent.inputSavePath.setText(path + "\\处理后")
        self.parent.groupListImg.loadImage()
        self.parent.groupMessage.normalMessage(f"设置素材文件夹： {folder}")
        self.parent.groupMessage.normalMessage(f"设置保存文件夹： {folder}" + "\\处理后")
