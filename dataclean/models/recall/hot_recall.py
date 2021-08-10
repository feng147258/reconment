#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 4:11 PM
# @Author  : zhuyingjun
# @File    : hot_recall.py

import math
import matplotlib.pyplot as plt

def decay_function(alpha=0.01, init=10000, deltaT=100):
    data =[]
    for t in range(deltaT):
        if len(data) == 0:
            temp = init/ math.pow(t+1,alpha)
        else:
            temp = data[-1]/math.pow(t+1,alpha)
        data.append(temp)
    plt.plot([t for t in range(deltaT)],data,label = 'alpha = {}'.format(alpha))



if __name__ == '__main__':
    init = 10000
    deltaT = 60
    plt.figure(figsize=(20, 8))
    decay_function(.0001,init,deltaT)
    decay_function(.002, init, deltaT)
    decay_function(.004, init, deltaT)

    decay_function(.02, init, deltaT)
    decay_function(.1, init, deltaT)
    decay_function(.5, init, deltaT)

    plt.xticks([t for t in  range(deltaT)])
    plt.grid()
    plt.legend()
    plt.show()  #如果需要看到曲线图，可以打开






