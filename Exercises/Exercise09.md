#第九次作业

####*姚贵斌 2014301020066*
------
##摘要
研究了刚性小球在容器内不断碰撞容器壁并反射后的轨迹。将刚性小球视为质点，假设是在无摩擦的水平面上进行（重力对运动无影响），且假设其与容器的碰撞是完全弹性碰撞。
##背景
此即所谓“台球问题”。此问题可以分为两个部分。
第一：当在两次碰撞之间，质点的匀速直线运动。欧勒法可以完美地解决这一过程：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cfrac%7Bdx%7D%7Bdt%7D%3Dv_x)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cfrac%7Bdy%7D%7Bdt%7D%3Dv_y)

其中，在没有碰撞时，速度分量保持不变。

第二：碰撞过程。对这一过程，可以先计算碰撞点的位置，进而计算碰撞处的单位法向量
![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Chat%7Bn%7D),再将速度矢量按法向量方向与垂直法向量方向分解。碰撞前：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv_%7Bi%2C%5Cperp%20%7D%7D%3D%28%5Cvec%7Bv_i%7D%5Ccdot%20%5Chat%7Bn%7D%29%5Chat%7Bn%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv_%7Bi%2C%5Cparallel%20%7D%7D%3D%5Cvec%7Bv_i%7D-%5Cvec%7Bv_%7Bi%2C%5Cperp%20%7D%7D)

由于是完全弹性碰撞，入射教育反射角相等，因此碰撞后：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv_%7Bf%2C%5Cperp%20%7D%7D%3D-%5Cvec%7Bv_%7Bi%2C%5Cperp%20%7D%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv_%7Bf%2C%5Cparallel%20%7D%7D%3D%5Cvec%7Bv_%7Bi%2C%5Cparallel%20%7D%7D)

##正文
