import pylab as pl
import math
dx = 0.01
dt = 0.0001/3
r = 1.0
c = r*dx/dt
L = 1.0                # the length of the string
t = 1                  # the total time
ls = int(L/dx)         # length scope=33
ts = int(t/dt)         # time scope
k = 1000
y = [[0 for i in range(ls)]for j in range(ts)]
x = []
yo = []
for i in range(ls):
    y[0][i] = math.exp(-k*(i*dx-0.4-0.05)**2)
    y[1][i] = math.exp(-k*(i*dx-0.4-0.05)**2)
for n in range(1,ts-1):
    y[n][0] = 0
    y[n][-1] = 0
    for i in range(1,ls-1):
        y[n+1][i] = -1*y[n-1][i]+r**2*(y[n][i+1]+y[n][i-1])
for k in range(1,ts-1):
    x.append(k*dt)
    yo.append(y[k][5])
pl.figure(figsize=(6,5))
pl.plot(x,yo) 
pl.title('signal vercus time at ,exited at ')
pl.xlim(0.,0.035)
pl.ylim(-.6,.6)
pl.xlabel('time/s')
pl.ylabel('signal(arbitary units)')
pl.show()
