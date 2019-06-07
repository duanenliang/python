import time, pickle, os

def authenticate(strings):
    count = 1
    while True:
        pw = input("请输入密码： ")
        if str(pw) == strings:
            return True
        else:
            print("第%d次输入错误，错误三次将被锁定" % (count))
            if count == 3:
                print("已锁定，请10分钟后再尝试")
                time.sleep(10)
                return "lock"
            count += 1



class View(object):

    def __init__(self, admin, passwd, dataPath):
        self.__admin = admin
        self.__passwd = passwd
        self.dataPath = dataPath

    @property
    def passwd(self):
        return self.__passwd

    @property
    def admin(self):
        return self.__admin

    def printLoginView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*                                                 *")
        print("*                  欢迎使用                       *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")
        user = input("请输入您的管理员账号：")
        if user == self.admin:
            return authenticate(self.passwd)
        else:
            print("管理员账号有误")
            return 0

    def printLogOutView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*                                                 *")
        print("*                  退出验证                       *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")
        user = input("请输入您的管理员账号：")
        if user == self.admin:
            return authenticate(self.passwd)
        else:
            print("管理员账号有误")
            return 0




    def printUserView(self):
        print("***************************************************")
        print("*     开户(1)            查询(2)                  *")
        print("*     取款(3)            存款(4)                  *")
        print("*     转账(5)            改密码(6)                *")
        print("*     锁定(7)            解锁(8)                  *")
        print("*     补卡(9)            销户(10)                 *")
        print("*                  退出系统(t)                    *")
        print("***************************************************")
        time.sleep(1)
        return str(input("请输入对应的代号"))




