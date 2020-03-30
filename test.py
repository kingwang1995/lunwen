# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/2/28 9:28
# @File:test.py
# @Software:PyCharm

xlist = []
ylist = []
zlist = []
file1 = 'pts1.txt'
file2 = 'pts2.txt'
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

with open("2.txt", 'w') as file2write:
    for i in range(len(xlist)):
        if int(xlist[i]) > -3000 and int(xlist[i]) < 8000 and int(ylist[i]) > 4000 and int(ylist[i]) < 10000 and int(
                zlist[i]) > 40 and int(zlist[i]) < 2000:
            file2write.write(str(xlist[i]) + " " + str(ylist[i]) + " " + str(zlist[i]) + "\n")
