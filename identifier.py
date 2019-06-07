class Identifier(object):
    __userPasswd = {"001":"12345", }
    def __init__(self, userId):
        self.userId = userId
    @property
    def userPasswd(self):
        return self.__userPasswd
    #@userPasswd.setter
    def setUserPasswd(self, key, password):
        self.__userPasswd[key] = password
    def passwdIdentify(self):
        count = 1
        while True:
            pw = input("请输入密码： ")
            if str(pw) == self.__userPasswd.get(self.userId):
                return True
            else:
                print("第%d次输入错误，错误三次将被锁定" %(count))
                if count == 3:
                    print("已锁定，请解锁后再尝试")
                    return "lock"
                count += 1
                



