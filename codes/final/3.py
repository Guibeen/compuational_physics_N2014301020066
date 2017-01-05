import random
import pylab as pl
import numpy as np
import math

L = 10
Ef = [[0 for i in range(L)]for j in range(L)]      #Eflip, with unit J
s  = [[1 for i in range(L)]for j in range(L)]      #spin
step = 1000
te = []                                            #total energy
e  = [0 for i in range(step)]
se = [0 for i in range(step)]
tse = []
cap = []
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
    pl.plot(T0,cap,'.')
    pl.title('Ising model heat capacity vs.temperature')
    pl.xlabel('Temperature')
#    pl.xlim(0,1000)
    pl.ylabel('Speciffic heat per spin')
#    pl.ylim(0,1.5)
    pl.show()
for i in range(50):
    T = 2.1+(1+i)/100
    beta = 1/T
    T0.append(T)
    for j in range(step):
        mcstep()
    for k in range(step):
        e[k] = np.sum(Ef)/(-4*L*L)
        se[k] = (np.sum(Ef)/(-4*L*L))**2
        mcstep()
    te.append(np.sum(e)/step)
    tse.append(np.sum(se)/step)
    cap.append(20*tse[-1]-20*(te[-1])**2)    
showresult()
