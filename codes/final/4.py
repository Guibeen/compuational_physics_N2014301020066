"""
Created on Wed Jan  4 19:34:02 2017

@author: M571575860
"""

##Different boundary conditions

import random
import pylab as pl
import numpy as np
import math

L = 10
T  = 1                                             #with unit J/kb
beta = 1/T                                         #with unit 1/J
T0 = []
step = 1000


Ef = [[0 for i in range(L)]for j in range(L)]      #Eflip, with unit J
s  = [[1 for i in range(L)]for j in range(L)]      #spin
Mag = []                                           #Magnetization
mag = [1 for i in range(step)]

Ef1 = [[0 for i in range(L)]for j in range(L)]      
s1  = [[1 for i in range(L)]for j in range(L)]      
Mag1 = []                                           
mag1 = [1 for i in range(step)]


def mcstep():
    #calflipenergy
    for i in range(L):
        for j in range(L):
            x = random.random()
            if i==L-1:                             #Period boundary condition
                i=-1
            if j==L-1:
                j=-1
            Ef[i][j] = 2*(s[i-1][j]+s[i+1][j]+s[i][j-1]+s[i][j+1])*s[i][j]
            #Monte Carlo
            if Ef[i][j]<0:
                s[i][j] = -1*s[i][j]
            elif x<math.exp(-Ef[i][j]*beta):
                s[i][j] = -1*s[i][j]
    return None

def mcstep1():
    #calflipenergy
    for i in range(L):
        for j in range(L):
            y = random.random()
            if 0<i<L-1:                           #Limited boundary condition
                left = s1[i-1][j]
                right = s1[i+1][j]
            elif i==0:
                left = 0
                right = s1[i+1][j]
            elif i==L-1:
                left = s1[i-1][j]
                right = 0
            if 0<j<L-1:
                above = s1[i][j+1]
                below = s1[i][j-1]
            elif j==0:
                above = s1[i][j+1]
                below = 0
            elif j==L-1:
                above = 0
                below = s1[i][j-1]
            Ef1[i][j] = 2*(left+right+above+below)*s1[i][j]
            #Monte Carlo
            if Ef1[i][j]<0:
                s1[i][j] = -1*s1[i][j]
            elif y<math.exp(-Ef1[i][j]*beta):
                s1[i][j] = -1*s1[i][j]
    return None


def calmag():
    mag.append(np.sum(s)/(L*L))
    return None
def showresult():
    pl.plot(T0,Mag,'.',label='PBC')
    pl.plot(T0,Mag1,'.',label='LBC')
    pl.legend()
    pl.title('Ising model Magnetization vs.temperature')
    pl.xlabel('temperature')
#    pl.xlim(0,1000)
    pl.ylabel('Magnetization')
#    pl.ylim(-0.1,1.1)
    pl.show()

for i in range(80):
    T = (1+i)/16
    beta = 1/T
    T0.append(T)
    for j in range(step):
        mcstep()
        mcstep1()
    for k in range(step):
        mag[k] = np.sum(s)/(L*L)
        mcstep()
        mag1[k] = np.sum(s1)/(L*L)
        mcstep1()
    Mag.append(np.sum(mag)/step)
    Mag1.append(np.sum(mag1)/step)
showresult()
