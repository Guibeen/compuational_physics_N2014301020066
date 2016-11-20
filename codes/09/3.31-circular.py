import math
x_0=0.5
y_0=0
v_x_0=1
v_y_0=0.1
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
alpha=0.0
v_x_1=[]
x_1_1=[]


for i in range(int(end_t/dt)):
    x.append(x[i]+v_x[i]*dt)
    y.append(y[i]+v_y[i]*dt)
    v_x.append(v_x[i])
    v_y.append(v_y[i])
    t.append(t[i]+dt)
    if abs(x[i+1]-1)<0.0001:
       print(x[i+1])
       a=-x[i+1]
       b=0
       v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
       v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
    else:
       if y[i+1]<0:
          if  x[i+1]**2.0+(y[i+1]+alpha/2.0)**2.0>1:
           while abs(x[i+1]**2+(y[i+1]+alpha/2.0)**2-1)>0.0001:
              #print abs(x[i+1]**2+y[i+1]**2-1)              
              X=(x[i]+x[i+1])/2
              Y=(y[i]+y[i+1])/2
              a=X/((X**2+(Y+alpha/2.0)**2)**0.5)
              b=(Y+alpha/2.0)/((X**2+(Y+alpha/2.0)**2)**0.5)
              v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
              v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              #v_y[i+1]=-((2.0*a**3-2.0*a)/b)*v_x[i+1]-(2*a**2-1)*v_y[i+1]
              if X**2+(Y+alpha/2.0)**2>1:
                 x[i+1]=X
                 y[i+1]=Y
                 continue
              else:
                 x[i]=X
                 y[i]=Y
                 continue
       else:
          if  x[i+1]**2.0+(y[i+1]-alpha/2.0)**2.0>1:
           while abs(x[i+1]**2+(y[i+1]-alpha/2.0)**2-1)>0.0001:
              #print abs(x[i+1]**2+y[i+1]**2-1)
              X=(x[i]+x[i+1])/2
              Y=(y[i]+y[i+1])/2
              a=X/((X**2+(Y-alpha/2.0)**2)**0.5)
              b=(Y-alpha/2.0)/((X**2+(Y-alpha/2.0)**2)**0.5)
              v_x[i+1]=(1-2*a**2)*v_x[i]-2*a*b*v_y[i]
              v_y[i+1]=(1-2*b**2)*v_y[i]-2*a*b*v_x[i]
              #v_y[i+1]=-((2.0*a**3-2.0*a)/b)*v_x[i+1]-(2*a**2-1)*v_y[i+1]
              if X**2+(Y-alpha/2.0)**2>1:
                 x[i+1]=X
                 y[i+1]=Y
                 continue
              else:
                 x[i]=X
                 y[i]=Y
                 continue

    if abs(y[i]-0)<0.0001:
       p=x[i]
       q=v_x[i]
       v_x_1.append(q)
       x_1_1.append(p)

print(v_x[30])
x_1=[-1]
y_1=[0]
x_2=[-1]
y_2=[0]
dx=0.01
for j in range(199):
    x_1.append(x_1[j]+dx)
    y_1.append(alpha/2.0+(1-x_1[j+1]**2)**0.5)
    x_2.append(x_2[j]+dx)
    y_2.append(-alpha/2.0-(1-x_2[j+1]**2)**0.5)


import matplotlib.pyplot as plt
fig= plt.figure(figsize=(7,6))
#fig= plt.figure(figsize=(7,6))
#plt.scatter(x_1_1,v_x_1,marker='+',color='b',label='phase space plot')
plt.plot(x,y,'--' ,label='orbit')
plt.plot(x_1,y_1,'--',label='bianary')
plt.plot(x_2,y_2,'--',label='bianary')
plt.title(u'$v_x/v_y=1/0.002,a=0.001,scan-point-y=0$',fontsize=16) 
plt.xlabel(u'x',fontsize=14)
plt.ylabel(u'y',fontsize=14)
plt.xlim(-1.17,1.17)
plt.ylim(-1.0,1.0)
plt.legend(fontsize=12,loc='best')
plt.show(fig)
