from person import Person
from card import Card
import random, pickle, os, time


class Atm(object):
    def __init__(self):
        self.userList = {}
    def kaiHu(self):
        print(self.userList)
        name = input("请输入您的姓名：")
        userId = input("请输入身份证号：")
        userTelNum = input("请输入手机号码： ")
        cardId = self.createCardId()
        cardPasswd = input("请输入卡的密码： ")
        cardMoney = input("请输入预存金额： ")
        card = Card(cardId, cardPasswd, cardMoney)
        user = Person(userId, userTelNum, card, name)
        self.userList[card.cardId] = user
        print("开户成功\n您的卡号是 %s 请牢记！！" % (user.card.cardId))
        time.sleep(3)
    def chaXun(self):
        cardId = input("请输入卡号：")
        if not self.userList.get(cardId):
            print("您输入的卡号不存在")
            return False
        passwd = input("请输入密码：")
        if passwd != self.userList.get(cardId).card.cardPasswd:
            print("密码错误")
            return False
        userDuiXiang = self.userList.get(cardId)
        print("姓名：%s\t余额：%s\t身份证号：%s" \
              %(userDuiXiang.name, userDuiXiang.card.cardMoney, userDuiXiang.userId))
        time.sleep(1)
    def quKuan(self):
        pass
    def cunKuan(self):
        pass
    def zhuanZhang(self):
        pass
    def gaiMima(self):
        pass
    def suoDing(self):
        pass
    def jieSuo(self):
        pass
    def buKa(self):
        pass
    def xiaoHu(self):
        pass
    def chiJiuHua(self, fileName):
        absFilePath = os.path.join(os.getcwd(), fileName)
        temFile = open(absFilePath, "wb")
        pickle.dump(self.userList, temFile)
        temFile.close()
    def loadData(self, destDict):
        dataFilePath = os.path.join(os.getcwd(), destDict)
        temFile = open(dataFilePath, "rb")
        self.userList = pickle.load(temFile)
        temFile.close()
    def createCardId(self):
        while True:
            string1 = str(random.randrange(1, 9))
            for i in range(5):
                str1 = random.randrange(0, 9)
                string1 += str(str1)
                i += 1
            if not self.userList.get(string1):
                return string1









