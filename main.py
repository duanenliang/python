import time
from view import View
from atm import Atm

def main():
    #infoList = []
    atm = Atm()
    view = View("1", "123", "userlist.txt")
    signal = view.printLoginView()

    atm.loadData(view.dataPath)
    while signal == True:
        signal1 = view.printUserView()
        if str(signal1) == "1":
            atm.kaiHu()
        elif str(signal1) == "2":
            atm.chaXun()
        elif str(signal1) == "3":
            atm.quKan()
        elif str(signal1) == "4":
            atm.cunKuan()
        elif str(signal1) == "5":
            atm.zhuanZhang()
        elif str(signal1) == "6":
            atm.gaiMiMa()
        elif str(signal1) == "7":
            atm.suoDing()
        elif str(signal1) == "8":
            atm.jieSuo()
        elif str(signal1) == "9":
            atm.buKa()
        elif str(signal1) == "10":
            atm.xiaoHu()
        elif str(signal1) == "t":
            if view.printLogOutView() == True:
                atm.chiJiuHua(view.dataPath)
                break
        else:
            print("输入有误")
        time.sleep(3)
    else:
        print("The error code is %s ." % signal)

if __name__ == "__main__":
    main()