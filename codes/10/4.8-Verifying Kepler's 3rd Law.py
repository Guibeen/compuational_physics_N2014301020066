import math
import pylab as pl
x_0 = 1.0
y_0 = 0.0
v_x_0 = 0
v_y_0 = 1*math.pi
GMs = 4*math.pi**2
r_0 = 1.0
wht = 2.0
dt = 0.0001
x = []
y = []
v_x = []
v_y = []
r = []
t = [0]
T = [0.0]
A = [1.0]
x.append(x_0)
y.append(y_0)
v_x.append(v_x_0)
v_y.append(v_y_0)
r.append(r_0)

for i in range(int(wht/dt)):
    v_x.append(v_x[-1]-GMs*x[-1]*dt/r[-1]**3)
    v_y.append(v_y[-1]-GMs*y[-1]*dt/r[-1]**3)
    x.append(x[-1]+v_x[-1]*dt)
    y.append(y[-1]+v_y[-1]*dt)
    r.append((x[-1]**2+y[-1]**2)**0.5)
    t.append(t[-1]+dt)
    
    #计算近日点与远日点，以及到达的时间
    if (y[-1]*y[-2]>0):
        continue
    elif (y[-1]==0):
        T.append(t[-1])
        A.append(x[-1])
    elif (y[-1]*y[-2]<0):
        y[-1]=y[-2]
        x[-1]=x[-2]
        v_x[-1]=v_x[-2]
        v_y[-1]=v_y[-2]
        while (1):
            v_x.append(v_x[-1]-GMs*x[-1]*dt*0.01/r[-1]**3)
            v_y.append(v_y[-1]-GMs*y[-1]*dt*0.01/r[-1]**3)
            x.append(x[-1]+v_x[-1]*dt*0.01)
            y.append(y[-1]+v_y[-1]*dt*0.01)
            t.append(t[-1]+dt*0.01)
            if (y[-1]*y[-2]<=0):
                T.append(t[-1])
                A.append(x[-1])
                break
T_1 = []
A_1 = []
print('前三个周期的半长轴的立方与周期的平方的比值依次为：')
for k in range(3):
    T_1.append(T[2*k+2]-T[2*k])
    A_1.append((abs(A[2*k])+abs(A[2*k+1]))/2)
    
    print(float(A_1[-1]**3/T_1[-1]**2))
    
pl.plot(x,y)
pl.title(u'$x=1,y=0,v_x=0,v_y=\pi$',fontsize=14)
pl.xlabel(u'x(AU)',fontsize=14)
pl.ylabel(u'y(AU)',fontsize=14)
pl.xlim(-0.5,1.3)
pl.ylim(-0.6,0.6)
