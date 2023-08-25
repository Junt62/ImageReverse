import os
from PySide6.QtWidgets import QFileDialog

from logic.GroupMessage import GroupMessage


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
            GroupMessage.successMessage("已设置素材路径")
        else:
            GroupMessage.normalMessage("未选择新的素材路径")

    def btnSavePathClicked(self):
        path = QFileDialog.getExistingDirectory(self.parent, "选择路径", os.getcwd())
        path = path.replace("/", "\\")
        if path:
            self.parent.inputSavePath.setText(path)
            GroupMessage.successMessage("已设置保存位置")
        else:
            GroupMessage.normalMessage("未选择新的保存位置")
