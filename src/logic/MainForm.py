from datetime import datetime
import os, re, time, shutil, threading
from PySide6.QtWidgets import QMainWindow, QFileDialog
from logic.GroupListImg import GroupListImg
from logic.GroupMessage import GroupMessage
from logic.GroupPath import GroupPath
from logic.GroupImgBig import GroupImgBig
from logic.GroupImgSmall import GroupImgSmall
from logic.GroupProgress import GroupProgress
from resources.ImageReverse_ui import Ui_Form
from PIL import Image


class MainForm(QMainWindow, Ui_Form):
    tempFolder = ""
    fillFolder = ""

    pattern = re.compile(r"^[A-Za-z]:\\[^\\\/:*?\"<>|]")
    thread = threading.Thread()
    renameMapping = {
        "待机": "01站立",
        "跑步": "03跑步",
        "战斗待机": "04面向",
        "攻击": "05攻击",
        "释放技能": "08施法",
        "死亡": "11死亡",
        "stand": "01站立",
        "run": "03跑步",
        "attack1": "05攻击",
        "attack2": "06暴击",
        "die": "11死亡",
    }
    renameMapping2 = {
        "01站立": "s",
        "03跑步": "r",
        "04面向": "h",
        "05攻击": "a",
        "08施法": "c",
        "11死亡": "d",
    }
    renameMapping3 = {
        "01站立": 0,  # 0-64
        "02走路": 64,  # 64-128
        "03跑步": 128,  # 128-192
        "04面向": 192,  # 192-200  # 8
        "05攻击": 200,  # 200-264
        "06暴击": 264,  # 264-328
        "07跳斩": 328,  # 328-392
        "08施法": 392,  # 392-456
        "09捡物": 456,  # 456-472  # 16
        "10受击": 472,  # 472-536
        "11死亡": 536,  # 536-600
    }
    renameMapping4 = {
        "1上",
        "2右上",
        "3右",
        "4右下",
        "5下",
        "6左下",
        "7左",
        "8左上",
    }

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.groupPath = GroupPath(self)
        self.groupProgress = GroupProgress(self)
        self.groupListimg = GroupListImg(self)
        self.groupImgBig = GroupImgBig(self)
        self.groupImgSmall = GroupImgSmall(self)
        self.groupMessage = GroupMessage(self)

        self.groupMessage.successMessage("软件初始化完成，可以开始操作")

        self.tempFolder = os.path.join(self.inputSavePath.text(), "temp")
        self.fillFolder = os.path.join(self.inputSavePath.text(), "fill")

        # self.btnSelectTarget.clicked.connect(self.btnSelectTargetClicked)
        # self.btnSelectResult.clicked.connect(self.btnSelectResultClicked)
        # self.btnResetTarget.clicked.connect(self.btnResetTargetClicked)
        # self.btnImageReverse.clicked.connect(self.btnImageReverseClicked)
        # self.inputTarget.textChanged.connect(self.inputTargetTextChanged)
        # self.inputResult.textChanged.connect(self.inputResultTextChanged)

    def btnSelectTargetClicked(self):
        fileAddress = QFileDialog.getExistingDirectory(self, "选择路径", os.getcwd())
        fileAddress = fileAddress.replace("/", "\\")
        if fileAddress:
            self.updateInputTarget(fileAddress)

    def btnSelectResultClicked(self):
        fileAddress = QFileDialog.getExistingDirectory(self, "选择路径", os.getcwd())
        fileAddress = fileAddress.replace("/", "\\")
        self.updateInputResult(fileAddress)

    def inputTargetTextChanged(self):
        path = self.inputTarget.text()
        if re.match(self.pattern, path):
            self.enableBtnSelectTarget(True, "(1)请设置目标路径：合法路径，可以进行下一步", "color: green;")
            self.enableBtnSelectResult(True)
            if "_处理后" in self.inputTarget.text():
                self.updateInputResult("")
                self.updateInputResult(path)
            else:
                self.updateInputResult("")
                self.updateInputResult(path + "_处理后")
        elif path == "":
            self.enableBtnSelectTarget(True)
            self.enableBtnSelectResult(False)
            self.enableBtnResetTarget(False)
        else:
            self.enableBtnSelectTarget(True, "(1)请设置目标路径：路径格式错误", "color: red;")
            self.enableBtnSelectResult(False)
            self.enableBtnResetTarget(False)

    def inputResultTextChanged(self):
        targetPath = self.inputTarget.text()
        resultPath = self.inputResult.text()
        if resultPath:
            if re.match(self.pattern, resultPath):
                self.enableBtnSelectResult(
                    True, "(2)处理后图片路径：合法路径，可以进行下一步", "color: green;"
                )
                if re.match(self.pattern, targetPath):
                    self.checkFolderImage(targetPath)
                else:
                    self.enableBtnSelectTarget(True, "(1)请设置目标路径：路径格式错误", "color: red;")
                    self.enableBtnSelectResult(False)
            else:
                self.enableBtnSelectResult(True, "(2)处理后图片路径：路径格式错误", "color: red;")
                self.enableBtnResetTarget(False)

    # 调整图片结构按钮按下后做的事情
    def btnResetTargetClicked(self):
        # 运行当前函数时后修改按钮和状态
        self.enableBtnResetTarget(False, "(3)调整图片结构：调整图片结构进行中...", "color: orange;")
        self.barResetTarget.setValue(2)  # 控制进度条

        # 创建文件夹
        oldFolder = self.inputTarget.text()
        newFolder = self.inputResult.text()
        tempFolder = os.path.join(self.inputResult.text(), "temp")
        imgFolder = os.path.join(self.inputResult.text(), "img")
        try:
            os.mkdir(newFolder)
        except FileExistsError:
            shutil.rmtree(newFolder)
            os.mkdir(newFolder)
        try:
            os.mkdir(tempFolder)
        except FileExistsError:
            shutil.rmtree(tempFolder)
            os.mkdir(tempFolder)
        try:
            os.mkdir(imgFolder)
            for i in range(600):
                value = str(i).zfill(5)
                image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
                image.save(imgFolder + "\\" + value + ".png")
        except FileExistsError:
            shutil.rmtree(imgFolder)
            os.mkdir(imgFolder)
            for i in range(600):
                value = str(i).zfill(5)
                image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
                image.save(imgFolder + "\\" + value + ".png")
        self.barResetTarget.setValue(5)  # 控制进度条

        # 第一次循环复制文件夹至temp
        for name in os.listdir(oldFolder):
            oldPath = os.path.join(oldFolder, name)
            if os.path.isdir(oldPath):
                newPath = os.path.join(tempFolder, name)
                shutil.copytree(oldPath, newPath)
        self.barResetTarget.setValue(8)  # 控制进度条

        # 第二次循环删除所有的Thumbs.db文件
        for name in os.listdir(tempFolder):
            path1 = os.path.join(tempFolder, name)
            if os.path.isdir(path1):
                for name2 in os.listdir(path1):
                    path2 = os.path.join(path1, name2)
                    if os.path.isdir(path2):
                        for name3 in os.listdir(path2):
                            path3 = os.path.join(path2, name3)
                            if name3 == "Thumbs.db":
                                os.remove(path3)

        # 第三次循环重命名动作文件夹
        for oldName in os.listdir(tempFolder):
            oldPath = os.path.join(tempFolder, oldName)
            if os.path.isdir(oldPath) and oldName in self.renameMapping:
                newName = self.renameMapping[oldName]
                newPath = os.path.join(tempFolder, newName)
                shutil.move(oldPath, newPath)
        self.barResetTarget.setValue(10)  # 控制进度条

        # 第四次循环重命名方向文件夹
        firstFloorImage = 0  # 统计第一层文件夹内的图片
        isStandardConstruction = True
        for oldName in os.listdir(tempFolder):
            oldPath = os.path.join(tempFolder, oldName)
            # \temp\01站立
            if os.path.isdir(oldPath) and oldName in self.renameMapping3:
                for oldName2 in os.listdir(oldPath):
                    oldPath2 = os.path.join(oldPath, oldName2)
                    #  \temp\01站立\body_0 +s|r|h|a|c|d
                    if os.path.isdir(oldPath2):
                        if oldName2[-2:] == "0" + self.renameMapping2[oldName]:
                            shutil.move(oldPath2, oldPath + "\\1上")
                        if oldName2[-2:] == "1" + self.renameMapping2[oldName]:
                            shutil.copytree(oldPath2, oldPath + "\\8左上")
                            shutil.move(oldPath2, oldPath + "\\2右上")
                        if oldName2[-2:] == "2" + self.renameMapping2[oldName]:
                            shutil.copytree(oldPath2, oldPath + "\\7左")
                            shutil.move(oldPath2, oldPath + "\\3右")
                        if oldName2[-2:] == "3" + self.renameMapping2[oldName]:
                            shutil.copytree(oldPath2, oldPath + "\\6左下")
                            shutil.move(oldPath2, oldPath + "\\4右下")
                        if oldName2[-2:] == "4" + self.renameMapping2[oldName]:
                            shutil.move(oldPath2, oldPath + "\\5下")
                    else:
                        try:
                            Image.open(oldPath2).close
                            newPath = os.path.join(
                                newFolder,
                                oldName,
                            )
                            newName = str(
                                newPath + f"\\{str(firstFloorImage).zfill(5)}.png",
                            )

                            if not os.path.exists(newPath):
                                os.makedirs(newPath)
                            shutil.move(oldPath2, newName)
                            firstFloorImage += 1
                            isStandardConstruction = False
                        except:
                            pass
        self.barResetTarget.setValue(13)  # 控制进度条

        # 第五次循环补齐方向文件夹中的图片至8张
        for oldName in os.listdir(tempFolder):
            oldPath = os.path.join(tempFolder, oldName)
            # \temp\01站立
            if os.path.isdir(oldPath) and oldName in self.renameMapping3:
                for oldName2 in os.listdir(oldPath):
                    oldPath2 = os.path.join(oldPath, oldName2)
                    # \temp\01站立\1上
                    if os.path.isdir(oldPath2) and oldName2 in self.renameMapping4:
                        count = 0
                        for oldName3 in os.listdir(oldPath2):
                            oldPath3 = os.path.join(oldPath2, oldName3)
                            # \temp\01站立\1上\00.png
                            if os.path.splitext(oldPath3)[1].lower() == ".png":
                                shutil.move(oldPath3, oldPath2 + "\\" + str(count))
                            count += 1
                        if count < 8 and count > 2:
                            for i in range(8 - count):
                                value = str(900 + i)
                                image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
                                image.save(oldPath2 + "\\" + value + ".png")
                        elif count == 1 and oldName == "面向":
                            pass
                        elif count == 2 and oldName == "捡物":
                            pass
        self.barResetTarget.setValue(15)  # 控制进度条

        # 第六次循环找出一共需要处理多少张图片并且制作进度条
        countImage = 0
        for oldName in os.listdir(tempFolder):
            oldPath = os.path.join(tempFolder, oldName)
            if os.path.isdir(oldPath) and oldName in self.renameMapping3:
                for oldName2 in os.listdir(oldPath):
                    oldPath2 = os.path.join(oldPath, oldName2)
                    if os.path.isdir(oldPath2) and oldName2 in self.renameMapping4:
                        for oldName3 in os.listdir(oldPath2):
                            countImage += 1

        # 第七次循环将图片按规则重命名并提取到同一文件夹
        countIndex = 0
        for oldName in os.listdir(tempFolder):
            oldPath = os.path.join(tempFolder, oldName)
            # \temp\01站立
            if os.path.isdir(oldPath) and oldName in self.renameMapping3:
                if oldName == "04面向":
                    index = self.renameMapping3["04面向"]  # 192
                elif oldName == "09捡物":
                    index = self.renameMapping3["09捡物"]  # 456
                else:
                    index = self.renameMapping3[oldName]
                for oldName2 in os.listdir(oldPath):
                    oldPath2 = os.path.join(oldPath, oldName2)
                    # \temp\01站立\1上
                    if os.path.isdir(oldPath2) and oldName2 in self.renameMapping4:
                        for oldName3 in os.listdir(oldPath2):
                            oldPath3 = os.path.join(oldPath2, oldName3)
                            # \temp\01站立\1上\00.png

                            # 重命名为标准序列帧图片命令格式
                            shutil.move(
                                oldPath3, oldPath2 + f"\\{str(index).zfill(5)}.png"
                            )

                            # 复制所有图片到最外层
                            shutil.copy(
                                oldPath2 + f"\\{str(index).zfill(5)}.png", newFolder
                            )

                            # 更新序号
                            index += 1

                            # 更新进度条 15~95
                            countIndex += 1
                            self.barResetTarget.setValue(
                                int((95 - 15) / countImage * countIndex) + 15
                            )

        # 使用透明图片填充空白
        if isStandardConstruction:
            for name in os.listdir(imgFolder):
                path = os.path.join(imgFolder, name)
                target = os.path.join(newFolder, name)
                if not os.path.exists(target):
                    shutil.copy(path, newFolder)
        self.barResetTarget.setValue(95)  # 控制进度条

        # 删除temp文件夹
        try:
            shutil.rmtree(imgFolder)
            shutil.rmtree(tempFolder)
        except FileNotFoundError:
            pass
        self.barResetTarget.setValue(98)  # 控制进度条

        # 将结果路径输入至目标路径
        self.updateInputTarget(self.inputResult.text())

        # 调用翻转图片检测
        self.checkFolderImage(self.inputResult.text())

        # 运行完当前函数后修改按钮和状态
        self.enableBtnResetTarget(True, "(3)调整图片结构：调整图片结构完成", "color: green;")
        self.barResetTarget.setValue(100)  # 控制进度条

    def btnImageReverseClicked(self):
        self.enableBtnImageReverse(False, "(4)翻转序列帧图片：翻转序列帧图片进行中...", "color: orange;")
        self.barImageReverse.setValue(0)
        target = self.inputTarget.text()

        # 将图片按规则进行反转
        index = 0
        for name in os.listdir(target):
            path = os.path.join(target, name)
            temp = os.path.join(target, "00040.png")

            # 检测当前帧是否需要翻转
            if index >= 40 and index < 64:  # 站立
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 104 and index < 128:  # 02走路
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 168 and index < 192:  # 03跑步
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 197 and index < 200:  # 04面向
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 240 and index < 264:  # 05攻击
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 304 and index < 328:  # 06暴击
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 368 and index < 392:  # 07跳斩
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 432 and index < 456:  # 08施法
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 466 and index < 472:  # 09捡物
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 512 and index < 536:  # 10受击
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )
            if index >= 576 and index < 600:  # 11死亡
                Image.open(path).transpose(Image.FLIP_LEFT_RIGHT).save(
                    path, overWrite=True
                )

            # 更新序号
            index += 1

            # 更新进度条
            self.barImageReverse.setValue(int((100 - 0) / 600 * index) + 0)

        self.enableBtnImageReverse(True, "(4)翻转序列帧图片：翻转序列帧图片完成", "color: green;")
        self.barImageReverse.setValue(100)

    def updateInputTarget(self, input):
        self.inputTarget.setText(input)

    def updateInputResult(self, input):
        self.inputResult.setText(input)

    def enableBtnSelectTarget(
        self, enable, message="(1)请设置目标路径：", color="color: black;"
    ):
        if enable:
            self.inputTarget.setEnabled(True)
            self.btnSelectTarget.setEnabled(True)
        else:
            self.inputTarget.setDisabled(True)
            self.btnSelectTarget.setDisabled(True)
        self.labelTarget.setText(message)
        self.labelTarget.setStyleSheet(color)

    def enableBtnSelectResult(
        self, enable, message="(2)处理后图片路径：", color="color: black;"
    ):
        if enable:
            self.inputResult.setEnabled(True)
            self.btnSelectResult.setEnabled(True)
        else:
            self.inputResult.setDisabled(True)
            self.btnSelectResult.setDisabled(True)
        self.labelResult.setText(message)
        self.labelResult.setStyleSheet(color)

    def enableBtnResetTarget(self, enable, message="(3)调整图片结构：", color="color: black;"):
        if enable:
            self.barResetTarget.setEnabled(True)
            self.btnResetTarget.setEnabled(True)
        else:
            self.barResetTarget.setDisabled(True)
            self.btnResetTarget.setDisabled(True)
        self.labelResetTarget.setText(message)
        self.labelResetTarget.setStyleSheet(color)

    def enableBtnImageReverse(
        self, enable, message="(4)翻转序列帧图片：", color="color: black;"
    ):
        if enable:
            self.barImageReverse.setEnabled(True)
            self.btnImageReverse.setEnabled(True)
        else:
            self.barImageReverse.setDisabled(True)
            self.btnImageReverse.setDisabled(True)
        self.labelImageReverse.setText(message)
        self.labelImageReverse.setStyleSheet(color)

    def checkFolderImage(self, path):
        count = self.countFolderImage(path)
        if count == 0:
            self.enableBtnSelectTarget(True, "(1)请设置目标路径：未检测到图片，请检查路径", "color: red;")
            self.enableBtnResetTarget(False)
            self.enableBtnImageReverse(False)
        elif count == 600:
            current = self.countFolderImage(path, False)
            if current == 600:
                self.enableBtnSelectTarget(
                    True, "(1)请设置目标路径：检测到 600 张图片，可以进行下一步", "color: green;"
                )
                self.enableBtnResetTarget(
                    False, "(3)调整图片结构：检测到 600 张图片,可以进行下一步", "color: green;"
                )
                self.enableBtnImageReverse(
                    True, "(4)翻转序列帧图片：检测到标准序列帧结构，可以翻转图片", "color: green;"
                )
            else:
                self.enableBtnSelectTarget(
                    True, "(1)请设置目标路径：检测到 600 张图片，可以进行下一步", "color: green;"
                )
                self.enableBtnResetTarget(
                    False, "(3)调整图片结构：检测到 600 张图片,可以进行下一步", "color: green;"
                )
                self.enableBtnImageReverse(
                    False, "(4)调整图片结构：未检测到标准序列帧结构，请检查文件夹", "color: red;"
                )
        elif count > 600:
            self.enableBtnSelectTarget(
                True, f"(1)请设置目标路径：检测到 {count} 张图片，请检查路径", "color: red;"
            )
            self.enableBtnResetTarget(False)
            self.enableBtnImageReverse(False)
        else:
            self.enableBtnSelectTarget(
                True, f"(1)请设置目标路径：检测到 {count} 张图片，可以进行下一步", "color: green;"
            )
            self.enableBtnResetTarget(
                True, f"(3)调整图片结构：检测到 {count} 张图片，可以调整图片结构", "color: orange;"
            )
            self.enableBtnImageReverse(False)

    def countFolderImage(self, path, recursion=True):
        count = 0
        try:
            for imgName in os.listdir(path):
                imgPath = os.path.join(path, imgName)
                if recursion:
                    if os.path.isfile(imgPath):
                        imgExtension = os.path.splitext(imgName)[1].lower()
                        if imgExtension in [".jpg", ".jpeg", ".png", ".bmp"]:
                            count += 1
                    elif os.path.isdir(imgPath):
                        count += self.countFolderImage(imgPath)
                else:
                    if os.path.isfile(imgPath):
                        imgExtension = os.path.splitext(imgName)[1].lower()
                        if imgExtension in [".jpg", ".jpeg", ".png", ".bmp"]:
                            count += 1
        except FileNotFoundError:
            pass
        return count

    def timeCheck(self):
        while True:
            self.inputResultTextChanged()
            time.sleep(1)
