"""
Created on Sun Nov 13 21:49:43 2016

@author: Administrator
"""
import random
import pylab as pl
import numpy as np
import math

L = 10
Ef = [[0 for i in range(L)]for j in range(L)]      # Eflip, with unit J
s  = [[1 for i in range(L)]for j in range(L)]      # spin
step = 1000
Mag = []                                           # Magnetization
te = []                                            # total energy
e  = []
T  = 4.0                                           # with unit J/kb
beta = 1/T                                         # with unit 1/J

for k in range(step):                              # Monte Carlo step
    Mag.append(np.sum(s)/(L*L))
    for i in range(L):
        for j in range(L):
            x = random.random()
            if i==L-1:                             # periodic boundary condition
                i=-1
            if j==L-1:
                j=-1
            Ef[i][j] = 2*(s[i-1][j]+s[i+1][j]+s[i][j-1]+s[i][j+1])*s[i][j]
            if Ef[i][j]<0:
                    s[i][j] = -1*s[i][j]
            elif x<math.exp(-Ef[i][j]*beta):
                    s[i][j] = -1*s[i][j]

    te.append(np.sum(Ef)/(-4))
    e.append(np.sum(Ef)/(-4*L*L))
t=[]
for i in range(step):
    t.append(i)
pl.plot(t,Mag,label='T='+str(T))
pl.legend()
#pl.plot(t,e)
pl.title('Ising model Magnetization vs.time')
pl.xlabel('time')
pl.xlim(0,1000)
pl.ylabel('Magnetization')
pl.ylim(-1,1)
pl.show()
