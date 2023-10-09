import sys, ctypes
from PySide6.QtWidgets import QApplication
from logic.MainForm import MainForm


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.setWindowTitle("序列帧图片翻转工具v1.3 github@junt62")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Picture Reverse")
    window.show()
    sys.exit(app.exec())
