from logic.GroupMessage import GroupMessage


class GroupImgSmall:
    def __init__(self, parent):
        self.parent = parent

    def showImg(self):
        GroupMessage.normalMessage(self, "showImgSmall")
