import random
import pylab as pl
import numpy as np
import math

L = 10
Ef = [[0 for i in range(L)]for j in range(L)]      #Eflip, with unit J
s  = [[1 for i in range(L)]for j in range(L)]      #spin
step = 1000
Mag = []                                           #Magnetization
mag = [1 for i in range(step)]
T  = 1                                             #with unit J/kb
beta = 1/T                                         #with unit 1/J
T0 = []

def mcstep():
    #calflipenergy
    for i in range(L):
        for j in range(L):
            x = random.random()
            if i==L-1:
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
def showresult():
    pl.plot(T0,Mag,'+',label='M')
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
    for j in range(step):               # To reach equilibrium
        mcstep()    
    for k in range(step):               # For calculate
        mag[k] = np.sum(s)/(L*L)
        mcstep()    
    #calenergy()
    Mag.append(np.sum(mag)/step)
showresult()
