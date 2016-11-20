import pylab as pl
x_0=1.2
y_0=0
v_x_0=0
v_y_0=0.5
dt=0.01
end_t=100
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
x.append(x_0)
y.append(y_0)
v_x.append(v_x_0)
v_y.append(v_y_0)
t.append(0)
q=1.6*10**-19
m=1*10**-19
b=1.0
E=1.0
for i in range(int(end_t/dt)):
    x.append(x[i]+v_x[i]*dt)
    y.append(y[i]+v_y[i]*dt)
    v_x.append(v_x[i]+q*b*v_y[i]*dt/m+q*E*dt/m)
    v_y.append(v_y[i]-q*b*v_x[i]*dt/m)
    t.append(t[i]+dt)
pl.plot(x,y)
pl.show
