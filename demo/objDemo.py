#coding=utf8
#抽出公共类
class wuping :
    #初始化函数
    def __init__(self,mianji):
        self.__zhanyonMJ=mianji
    #设置
    def SetMJ(self,mianji):
        self.__zhanyonMJ=mianji
    #获取
    def GetMj(self):

          return  self.__zhanyonMJ

#桌子
class Desk(wuping):
   pass

#杯子
class Cup(wuping):
    pass
#家
class Home:
    #家的默认面积
    def __init__(self,mianji):
        self.zongMj=mianji

    def GetShenYuMJ(self,wuping):
            if self.zongMj > wuping.GetMj() :
                self.zongMj=self.zongMj-wuping.GetMj()
                print("剩下的面积是%d"%(self.zongMj-wuping.GetMj()))
                print("剩下的面积是%d"%(self.zongMj))



samcup=Cup(10)
rdesk=Desk(20)
fz=Home(140)
fz.GetShenYuMJ(rdesk)



