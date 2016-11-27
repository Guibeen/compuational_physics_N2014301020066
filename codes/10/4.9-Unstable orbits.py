import math
import pylab as pl
e = 0.75
beta = 2.01
x_0 = 1.0
y_0 = 0.0
v_x_0 = 0
v_y_0 = 2*math.pi*(1-e)**0.5
GMs = 4*math.pi**2
r_0 = (x_0**2+y_0**2)**0.5
wht = 5.0
dt = 0.0001
x = []
y = []
v_x = []
v_y = []
r = []
t = [0]
x.append(x_0)
y.append(y_0)
v_x.append(v_x_0)
v_y.append(v_y_0)
r.append(r_0)

for i in range(int(wht/dt)):
    v_x.append(v_x[-1]-GMs*x[-1]*dt/r[-1]**(beta+1))
    v_y.append(v_y[-1]-GMs*y[-1]*dt/r[-1]**(beta+1))
    x.append(x[-1]+v_x[-1]*dt)
    y.append(y[-1]+v_y[-1]*dt)
    r.append((x[-1]**2+y[-1]**2)**0.5)
    t.append(t[-1]+dt)

pl.plot(x,y)
pl.title(u'$e=0.75,beta=2.01$',fontsize=14)
pl.xlabel(u'x(AU)',fontsize=14)
pl.ylabel(u'y(AU)',fontsize=14)
pl.xlim(-0.3,0)
pl.ylim(-0,0.2)
