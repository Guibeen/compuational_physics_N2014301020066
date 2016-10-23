#第六次作业


---
##摘要
在考虑海拔高度影响，使用绝热模型，并引入迎面风阻，但不考虑地球自转的情况下，实现了：

1. 找出使发射速度最小的角度以及相应的最小速度。
2. 引入误差（服从均匀分布）：发射角误差正负2°，速度误差5%，迎面风阻10%。找出使炮弹落点与打击目标距离差平方均值最小的发射速度与角度。

##正文

![背景](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/06/%E4%BD%9C%E4%B8%9A%E5%85%AD-%E5%8E%9F%E7%90%861.png)
######其中a取6.5e-3K/M,α取2.5

####欧勒法

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/06/%E4%BD%9C%E4%B8%9A%E5%85%AD-%E6%AC%A7%E5%8B%92%E6%B3%95.png)

###1. 使炮弹以最小速度击中目标
```python
import math
xx = 1000 #x position of the target,unit:m
yy = 100 #y position of the target,unit:m
g = 9.8 
a = (6.5)*(math.pow(10,-3)) 
Bm = 4*math.pow(10,-5) #B2/m,unit:m^(-1)
T0 = 300 
vw = -20 #velocity of wind, unit:m/s
va = 1000 #initial_velocity,unit:m/s
sv = [va]
sa = [0]
s = xx
for i in range(21):
    v = va 
    v0 = 0
    angle = 25 + i*0.001 #initial_angle=25°,add 2° each time
    for j in range(20):
        x = [0] #initial_x,unit:m
        y = [0] # initial_y,unit:m
        dt = 0.1 #time_step,unit:s
        vx = [v*math.cos(math.pi*angle/180)]
        vy = [v*math.sin(math.pi*angle/180)]
        while (x[-1]<=xx): 
            if y[-1] >100000000:
                c = 0
            else:
                c = math.pow((1-(a*y[-1]/T0)),2.5)
            Fx = -Bm*math.sqrt((vx[-1]-vw)*(vx[-1]-vw)+vy[-1]*vy[-1])*(vx[-1]-vw)*c
            Fy = -Bm*math.sqrt((vx[-1]-vw)*(vx[-1]-vw)+vy[-1]*vy[-1])*vy[-1]*c
            vx.append(vx[-1]+Fx*dt)
            vy.append(vy[-1]+(-g+Fy)*dt)  
            x.append(x[-1]+vx[-2]*dt)
            y.append(y[-1]+vy[-2]*dt)
        r = (xx-x[-2])/(x[-1]-xx)
        y[-1] = (y[-2]+r*y[-1])/(r+1)
        x[-1] = xx
        if y[-1]>yy:
            vt = v
            v = v0+(vt-v0)/2
        if y[-1]<yy:
            v0 = v
            v = v0+(vt-v0)/2
    sv.append(v)
    sa.append(angle)
vmin = min(sv)
l = sv.index(vmin)
amin = sa[l]
print('The x position of the target',xx)
print('The y position of the target',yy)
print('velocity of wind',vw)
print ('The minimum initial velocity:'+str(vmin)+'m/s')
print('angle:'+str(amin)+'°')
```
