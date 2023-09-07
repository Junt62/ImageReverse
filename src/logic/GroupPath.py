import os
from PySide6.QtWidgets import QFileDialog


class GroupPath:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnImgPath.clicked.connect(self.btnImgPathClicked)
        self.parent.btnSavePath.clicked.connect(self.btnSavePathClicked)
        self.parent.inputImgPath.editingFinished.connect(
            self.inputImgPathEditingFinished
        )

    def inputImgPathEditingFinished(self):
        path = self.parent.inputImgPath.text()
        path = path.replace("/", "\\")
        folder = path.split("\\")[-1]
        if path != "":
            if os.path.isdir(path):
                self.parent.inputSavePath.setText(path + "处理后")
                self.parent.groupMessage.normalMessage(f"设置素材文件夹： {folder}")
                self.parent.groupMessage.normalMessage(f"设置保存文件夹： {folder}" + "处理后")
            else:
                self.parent.groupMessage.errorMessage(f"错误的路径： {path}")

    def btnImgPathClicked(self):
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", os.getcwd())
        if path:
            path = path.replace("/", "\\")
            folder = path.split("\\")[-1]
            self.parent.inputImgPath.setText(path)
            self.parent.inputSavePath.setText(path + "处理后")
            self.parent.groupMessage.normalMessage(f"设置素材文件夹： {folder}")
            self.parent.groupMessage.normalMessage(f"设置保存文件夹： {folder}" + "处理后")

    def btnSavePathClicked(self):
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", os.getcwd())
        if path:
            path = path.replace("/", "\\")
            folder = path.split("\\")[-1]
            self.parent.inputSavePath.setText(path)
            self.parent.groupMessage.normalMessage(f"设置保存文件夹： {folder}")
