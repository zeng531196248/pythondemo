#coding=utf-8
while True:
    num=input("请输入一个数字..")
    def displayNumType(num):
     if num > 10 :
        print(num)
     else:
        print("输入的数字过小")
    displayNumType(int(num))