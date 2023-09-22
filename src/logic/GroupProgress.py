import os, shutil
from PIL import Image
from contextlib import contextmanager

from util.ZiJun import ZiJun


class GroupProgress:
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
        "06暴击": "",
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

    def __init__(self, parent):
        self.parent = parent

        self.backgroundColor = "transparent"
        self.isShowImg = False

        self.parent.btnChangeDisplayType.setEnabled(False)
        self.parent.btnChangeDisplayColor.clicked.connect(
            self.btnChangeDisplayColorClicked
        )

        self.parent.btnReadPosition.setEnabled(False)
        self.parent.btnApplyPosition.setEnabled(False)
        self.parent.btnImgAlignment.setEnabled(False)
        self.parent.btnSpace1.setEnabled(False)
        self.parent.btnStructure.clicked.connect(self.btnStructureClicked)
        self.parent.btnImgReverse.clicked.connect(self.btnImgReverseClicked)

    def btnReadPositionClicked(self):
        if not self.parent.inputImgPath.text():
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return
        elif not os.path.exists(self.parent.inputImgPath.text()):
            self.parent.groupMessage.errorMessage("素材路径不存在")
            return
        self.parent.groupListImg.loadImage(self.parent.inputImgPath.text())

    def btnStructureClicked(self):
        if not self.parent.inputImgPath.text():
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return
        elif not os.path.exists(self.parent.inputImgPath.text()):
            self.parent.groupMessage.errorMessage("素材路径不存在")
            return

        self.parent.groupMessage.normalMessage("调整图片结构进行中...")

        # 设置路径
        oldFolder = self.parent.inputImgPath.text()
        newFolder = self.parent.inputSavePath.text()
        tempFolder = os.path.join(newFolder, "temp")
        fillFolder = os.path.join(newFolder, "fill")

        # 创建保存路径文件夹
        try:
            os.mkdir(newFolder)
        except FileExistsError:
            shutil.rmtree(newFolder)
            os.mkdir(newFolder)

        os.mkdir(tempFolder)
        os.mkdir(fillFolder)

        # 创建600张空白图片
        for i in range(600):
            value = str(i).zfill(5)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            image.save(fillFolder + "\\" + value + ".png")

        # 第一次循环复制文件夹至temp
        for name in os.listdir(oldFolder):
            oldPath = os.path.join(oldFolder, name)
            if os.path.isdir(oldPath) and name != "处理后":
                newPath = os.path.join(tempFolder, name)
                shutil.copytree(oldPath, newPath)

        # 第二次循环删除所有的Thumbs.db文件
        for name in os.listdir(tempFolder):
            path1 = os.path.join(tempFolder, name)
            if os.path.isdir(path1):
                for name2 in os.listdir(path1):
                    path2 = os.path.join(path1, name2)
                    if name2 == "Thumbs.db":
                        os.remove(path2)
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
                        if (
                            oldName2[-2:] == "0" + self.renameMapping2[oldName]
                            or oldName2[-1:] == "0"
                        ):
                            shutil.move(oldPath2, oldPath + "\\1上")
                        if (
                            oldName2[-2:] == "1" + self.renameMapping2[oldName]
                            or oldName2[-1:] == "1"
                        ):
                            shutil.copytree(oldPath2, oldPath + "\\8左上")
                            shutil.move(oldPath2, oldPath + "\\2右上")
                        if (
                            oldName2[-2:] == "2" + self.renameMapping2[oldName]
                            or oldName2[-1:] == "2"
                        ):
                            shutil.copytree(oldPath2, oldPath + "\\7左")
                            shutil.move(oldPath2, oldPath + "\\3右")
                        if (
                            oldName2[-2:] == "3" + self.renameMapping2[oldName]
                            or oldName2[-1:] == "3"
                        ):
                            shutil.copytree(oldPath2, oldPath + "\\6左下")
                            shutil.move(oldPath2, oldPath + "\\4右下")
                        if (
                            oldName2[-2:] == "4" + self.renameMapping2[oldName]
                            or oldName2[-1:] == "4"
                        ):
                            shutil.move(oldPath2, oldPath + "\\5下")
                    else:
                        try:
                            # 检测是否图片，并且按规则进行重命名
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

        # 第六次循环找出一共需要处理多少张图片并且制作进度条
        # countImage = 0
        # for oldName in os.listdir(tempFolder):
        #     oldPath = os.path.join(tempFolder, oldName)
        #     if os.path.isdir(oldPath) and oldName in self.renameMapping3:
        #         for oldName2 in os.listdir(oldPath):
        #             oldPath2 = os.path.join(oldPath, oldName2)
        #             if os.path.isdir(oldPath2) and oldName2 in self.renameMapping4:
        #                 for oldName3 in os.listdir(oldPath2):
        #                     countImage += 1

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
                                oldPath2 + f"\\{str(index).zfill(5)}.png",
                                newFolder,
                            )

                            # 更新序号
                            index += 1

        # 使用透明图片填充空白
        if isStandardConstruction:
            for name in os.listdir(fillFolder):
                path = os.path.join(fillFolder, name)
                target = os.path.join(newFolder, name)
                if not os.path.exists(target):
                    shutil.copy(path, newFolder)

        # 删除temp文件夹
        try:
            shutil.rmtree(fillFolder)
            shutil.rmtree(tempFolder)
        except FileNotFoundError:
            pass

        self.parent.groupMessage.successMessage("调整图片结构完成")

    def btnImgReverseClicked(self):
        if not self.parent.inputImgPath.text():
            self.parent.groupMessage.errorMessage("未设置素材路径")
            return
        elif not os.path.exists(self.parent.inputImgPath.text()):
            self.parent.groupMessage.errorMessage("素材路径不存在")
            return

        self.parent.groupMessage.normalMessage("翻转序列帧图片进行中...")

        # 设置图片路径
        target = self.parent.inputSavePath.text()

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

        self.parent.groupMessage.successMessage("翻转序列帧图片完成")

    @contextmanager
    def tryExceptFileNotFoundError(self):
        try:
            yield
        except FileNotFoundError:
            pass

    def btnChangeDisplayColorClicked(self):
        ZiJun.changeBackground(ZiJun, self.backWidth, self.backHeight)

        if self.backgroundColor == "black":
            self.backgroundColor = "white"
            return ZiJun.generateColor(width, height, QColor(0, 0, 0))
        elif self.backgroundColor == "white":
            self.backgroundColor = "red"
            return ZiJun.generateColor(width, height, QColor(255, 255, 255))
        elif self.backgroundColor == "red":
            self.backgroundColor = "green"
            return ZiJun.generateColor(width, height, QColor(255, 0, 0))
        elif self.backgroundColor == "green":
            self.backgroundColor = "blue"
            return ZiJun.generateColor(width, height, QColor(0, 255, 0))
        elif self.backgroundColor == "blue":
            self.backgroundColor = "grid"
            return ZiJun.generateColor(width, height, QColor(0, 0, 255))
        elif self.backgroundColor == "grid":
            self.backgroundColor = "black"
            return ZiJun.generateGrid(width, height)
