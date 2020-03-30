# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/2/24 10:35
# @File:datareader.py
# @Software:PyCharm
# 读数据

def DataReader():
    xlist = []
    ylist = []
    zlist = []
    file1 = 'points1.txt'
    file2 = 'points2.txt'
    with open(file1, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            x, y, z = [float(i) for i in lines.split()]
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
    with open(file2, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            x, y, z = [float(i) for i in lines.split()]
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
    # return xlist, ylist, zlist
    with open("or.txt", 'w') as file2write:
        for i in range(len(xlist)):
            file2write.write(str(xlist[i]) + " " + str(ylist[i]) + " " + str(zlist[i])+"\n")

DataReader()