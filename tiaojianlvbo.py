# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/2/24 11:05
# @File:tiaojianlvbo.py
# @Software:PyCharm
# 条件滤波

import datareader

x, y, z = datareader.DataReader()
with open("tiaojian.txt", 'w') as file2write:
    for i in range(len(x)):
        if int(x[i]) > -3000 and int(x[i]) < 8000 and int(y[i]) > 4000 and int(y[i]) < 10000 and int(z[i]) > 40 and int(
                z[i]) < 2000:
            file2write.write(str(x[i]) + " " + str(y[i]) + " " + str(z[i]) + "\n")
