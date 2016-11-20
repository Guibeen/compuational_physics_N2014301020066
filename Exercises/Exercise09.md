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

第二：碰撞过程。

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E5%8F%8D%E5%B0%84%E7%A4%BA%E6%84%8F.png)

对这一过程，可以先计算碰撞点的位置，进而计算碰撞处的单位法向量
![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Chat%7Bn%7D),再将速度矢量按法向量方向与垂直法向量方向分解。碰撞前：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%7D%3D%28%5Cvec%7Bv%7D_i%5Ccdot%20%5Chat%7Bn%7D%29%5Chat%7Bn%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv%7D_%7Bi%2C%5Cparallel%20%7D%3D%5Cvec%7Bv%7D_i-%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%7D)

由于是完全弹性碰撞，入射角与反射角相等，因此碰撞后：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv%7D_%7Bf%2C%5Cperp%20%7D%3D-%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv%7D_%7Bf%2C%5Cparallel%20%7D%3D%5Cvec%7Bv%7D_%7Bi%2C%5Cparallel%20%7D)

##正文

在平面直角坐标系下，对碰前速度与碰后速度分解：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv%7D_i%3D%5Cvec%7Bv%7D_%7Bi%2Cx%7D%5Chat%7Bi%7D&plus;%5Cvec%7Bv%7D_%7Bi%2Cy%7D%5Chat%7Bj%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Cvec%7Bv%7D_f%3D%5Cvec%7Bv%7D_%7Bf%2Cx%7D%5Chat%7Bi%7D&plus;%5Cvec%7Bv%7D_%7Bf%2Cy%7D%5Chat%7Bj%7D)


并记![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20%5Chat%7Bn%7D%3Da%5Chat%7Bi%7D&plus;b%5Chat%7Bj%7D)

解出碰撞后的速度分量：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20v_%7Bf%2Cx%7D%3D%281-2a%5E2%29v_%7Bi%2Cx%7D-2abv_%7Bi%2Cy%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20v_%7Bf%2Cy%7D%3D%281-2b%5E2%29v_%7Bi%2Cy%7D-2abv_%7Bi%2Cx%7D)

###正方形边界
[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/09/3.31-square.py)

当y方向速度是x方向速度的整数倍时，系统呈现周期性，与四条边界的交点数是固定的有限个孤立点；倍数越大，交点越多：

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E6%A8%AA%E4%B8%80%E7%BA%B5%E5%9B%9B.png)
![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E6%A8%AA%E4%B8%80%E7%BA%B5%E5%8D%81%E5%85%AD.png)

当y方向的速度是x方向的无理数倍时，焦点不固定，不呈周期性：

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E6%A0%B9%E5%8F%B7%E4%BA%8C.png)

经历更长时间后，质点运动轨迹将覆盖整个区域(此图时间为上图时间的100倍)：

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E6%A0%B9%E5%8F%B7%E4%BA%8C%E5%8A%A0%E9%95%BF%E7%89%88.png)

###圆形边界

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/09/3.31-circular.py)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E5%9C%86%E5%BD%A2%E5%8C%BA%E5%9F%9F.png)

y=0处的相空间：
![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E5%9C%86%E5%BD%A2-%E7%9B%B8%E7%A9%BA%E9%97%B4.png)

###“田径场”型边界
圆形是作为田径场的特例(a=0)。而更一般的，当a不为零时：

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E4%BD%93%E8%82%B2%E5%9C%BA.png)

几个不同a值对应的在y=0处的相空间图像：

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/a%3D0.png)
![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/a%3D0.001.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/a%3D0.01.png)
![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/a%3D0.1.png)

可见：当a为零或较小(0.001左右)时，从相空间来看至少是有规律的；而当其大于0.01后，混沌效应越来越明显。

###带电粒子在环形匀强磁场区域

考虑较为简单的情况：粒子带单位正电荷，荷质比为1.6C/kg，匀强磁场方向垂直于运动平面射向观测者。

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/09/3.31-magnetic%20field.py)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E7%8E%AF%E5%BD%A2%E7%A3%81%E5%9C%BA.png)

###关于混合场中的运动

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E6%B7%B7%E5%90%88%E5%9C%BA.png)

这是高中物理竞赛是曾经碰到的问题。带电粒子以某一初速度入射匀强电场与匀强磁场的混合场中，，不计重力。匀强电场和匀强磁场的方向垂直(或至少有垂直的分量)，且入射带电粒子的方向与磁场方向垂直。求例子以后的运动。

当时所给的方法是将粒子的速度分解。由于电厂、磁场不变，所以一定能找一个速度，是的粒子以这个速度运动时，洛伦兹力刚好与电场力相抵消。此为一个分量。将此分量分解后，由于电场的作用被抵消，离子的另一个分量将只受磁场影响而做匀速圆周运动。粒子的运动就是这两个运动的合成，即螺旋运动。

现在用欧勒法来模拟这一过程。

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/09/3-31-mixed%20field.py)

过程中将问题做了一定简化：磁场与电场大小均为一个单位(电场沿+x方向，磁场向外)，粒子沿-y轴方向入射、速度大小正好为E/B的一半.

如此，按照前面所述的方法，粒子将沿着-y轴方向做螺线运动。

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E5%B1%8F%E5%B9%95%E6%8D%95%E8%8E%B7_2016_11_21_01_14_53_804.png)

越向下运动半径越大(说明速度在变大)，应该是和用欧勒法处理单摆的时候的一样的问题。。。

------
分析--由欧勒法：

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D&plus;%5B%28qv_%7By%2Ci%7DB&plus;qE%29/m%5D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Clarge%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%28qv_%7By%2Ci%7DB/m%29%5CDelta%20t)

若取
------
那就用欧勒-克罗默方法再来一次

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/09/3.31-mixed%20field-2.0.py)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/09/%E5%AE%8C%E7%BE%8E%EF%BC%81.png)

匀速圆周分运动的半径保持不变。











