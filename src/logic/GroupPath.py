import os
from PySide6.QtWidgets import QFileDialog


class GroupPath:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnImgPath.clicked.connect(self.btnImgPathClicked)
        self.parent.btnSavePath.clicked.connect(self.btnSavePathClicked)

    def btnImgPathClicked(self):
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", os.getcwd())
        path = path.replace("/", "\\")
        if path:
            self.parent.inputImgPath.setText(path)
            self.parent.inputSavePath.setText(path + "_处理后")

    def btnSavePathClicked(self):
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", os.getcwd())
        path = path.replace("/", "\\")
        if path:
            self.parent.inputSavePath.setText(path)
