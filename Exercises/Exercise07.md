##第七次作业
####*姚贵斌 2014301020066*
------
##摘要

当步长很小时，欧勒法可以很好地模拟一些简单的模型。但对于单摆，传统的欧勒法将违反能量守很定律而导致发散。而与之类似的欧勒-克罗默方法(Euler-Cromer method)可以很好地解决这一问题。本文即用此方法研究了单摆的一些运动。

##背景介绍

对理想单摆的小角度情况，由牛顿第二定律

![](http://latex.codecogs.com/png.latex?%5Cddot%7B%5Ctheta%20%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta)

可以写成：

![](http://latex.codecogs.com/png.latex?%5Cdot%7B%5Comega%20%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta%2C%5Comega%3D%5Cdot%7B%5Ctheta%7D)

欧勒-克罗默方法：

![](http://latex.codecogs.com/png.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i-%28g/l%29%5Ctheta_i%5CDelta%20t)

![](http://latex.codecogs.com/png.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)
![](http://latex.codecogs.com/png.latex?t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t)

为不失一般性，去掉小角近似，并引入空气阻尼![](http://latex.codecogs.com/png.latex?-q%5Cdot%5Ctheta),以及外加驱动力
![](http://latex.codecogs.com/png.latex?F_Dsin%28%5COmega_Dt%29)，
则运动方程变为

![](http://latex.codecogs.com/png.latex?%5Cddot%7B%5Ctheta%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Cdot%7B%5Ctheta%7D&plus;F_Dsin%28%5COmega_Dt%29)

欧勒-克罗默方法具体形式也变为：

![](http://latex.codecogs.com/png.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;%5B-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta_i-q%5Comega_i&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t)

![](http://latex.codecogs.com/png.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)

![](http://latex.codecogs.com/png.latex?t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t).

当![](http://latex.codecogs.com/png.latex?%5Ctheta_%7Bi&plus;1%7D%5Cnotin%5B-%5Cpi%2C%5Cpi%5D)时，增加或减去2![](http://latex.codecogs.com/png.latex?%5Cpi)即可。

##正文
####习题3.12：课本图3.9只描出了驱动力相位为2nπ的时刻的点，在此描出动力相位为一些另外的值（如2nπ-π/4，2nπ+π/2）时的点。（n为整数）

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/07/3.12.py)

当![](http://latex.codecogs.com/png.latex?%5COmega_Dt%3D2n%5Cpi&plus;%5Cpi/2)时：

![二分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E4%BA%8C%E5%88%86%E4%B9%8B%E6%B4%BE.png)

当![](http://latex.codecogs.com/png.latex?%5COmega_Dt%3D2n%5Cpi-%5Cpi/2)时：

![负二分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E8%B4%9F%E4%BA%8C%E5%88%86%E4%B9%8B%E6%B4%BE.png)

当![](http://latex.codecogs.com/png.latex?%5COmega_Dt%3D2n%5Cpi&plus;%5Cpi/4)时：

![四分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E5%9B%9B%E5%88%86%E4%B9%8B%E6%B4%BE.png)

当![](http://latex.codecogs.com/png.latex?%5COmega_Dt%3D2n%5Cpi-%5Cpi/4)时：

![负四分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E8%B4%9F%E5%9B%9B%E5%88%86%E4%B9%8B%E6%B4%BE.png)

####习题3.13：两个完全一样的摆，但有一个很小的初始角度差（设为0.001弧度）。

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/07/3.13.py)

####习题3.14：两个除了摩擦因数有细微差别之外，其他完全相同的摆。

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/07/3.14.py)







