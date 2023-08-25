from datetime import datetime
from PySide6.QtGui import QTextCharFormat, QColor


class GroupMessage:
    def __init__(self, parent):
        self.parent = parent

    def normalMessage(self, string: str):
        prefix = "[" + datetime.now().strftime("%H:%M:%S") + "] "
        self.parent.inputMessage.textCursor().insertText(prefix + string + "\n")

    def errorMessage(self, string: str):
        prefix = "[" + datetime.now().strftime("%H:%M:%S") + "] "
        format = QTextCharFormat()
        format.setForeground(QColor(255, 0, 0))
        self.parent.inputMessage.textCursor().insertText(prefix + string + "\n", format)

    def successMessage(self, string: str):
        prefix = "[" + datetime.now().strftime("%H:%M:%S") + "] "
        format = QTextCharFormat()
        format.setForeground(QColor(0, 170, 0))
        self.parent.inputMessage.textCursor().insertText(prefix + string + "\n", format)
