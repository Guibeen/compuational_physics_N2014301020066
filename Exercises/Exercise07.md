##第七次作业
####*姚贵斌 2014301020066*
------
##摘要

当步长很小时，欧勒法可以很好地模拟一些简单的模型。但对于单摆，传统的欧勒法将违反能量守很定律而导致发散。而与之类似的欧勒-克罗默方法(Euler-Cromer method)可以很好地解决这一问题。本文即用此方法研究了单摆的一些运动。

##背景介绍

![背景介绍图](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/%E7%AC%AC%E4%B8%89%E7%AB%A0-%E8%83%8C%E6%99%AF.png)

##正文
####习题3.12：课本图3.9只描出了驱动力相位为2nπ的时刻的点，在此描出动力相位为一些另外的值（如2nπ-π/4，2nπ+π/2）时的点。（n为整数）

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/07/3.12.py)

当相位为π/2时：

![二分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E4%BA%8C%E5%88%86%E4%B9%8B%E6%B4%BE.png)

当相位为-π/2时：

![负二分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E8%B4%9F%E4%BA%8C%E5%88%86%E4%B9%8B%E6%B4%BE.png)

当相位为π/4时：

![四分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E5%9B%9B%E5%88%86%E4%B9%8B%E6%B4%BE.png)

当相位为-π/4时：

![负四分之派](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3.12-%E8%B4%9F%E5%9B%9B%E5%88%86%E4%B9%8B%E6%B4%BE.png)

####习题3.13：两个完全一样的摆，但有一个很小的初始角度差（设为0.001弧度）。

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/07/3.13.py)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-FD0.5.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-0.5-1.png)
![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-0.5-2.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-FD1.2.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-1.2-1.png)
![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-1.2-2.png)

####习题3.14：两个除了摩擦因数有细微差别之外，其他完全相同的摆。

[代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/07/3.14.py)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-FD0.5.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-14-FD0.5.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-13-FD1.2.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-14-FD1.2-1.png)

![](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/07/3-14-FD1.2-2.png)

##结论

3.12--驱动力相位为±π/2的时刻，两图像基本是中心对称的关系。而±π/4的两图像则无对称关系.

3.13--驱动力幅度较小(0.5)时，Δθ开始时随时间数递减且呈一定的周期性，当减小到一定程度时，递减的速度开始下降；驱动力幅度较大(1.2)时，Δθ总体随时间递增，但过程没有规律，最后递增的速度也有减缓。

3.14--驱动力幅度较小(0.5)时，Δθ的变化呈现一定的周期性，虽然变动幅度很大，但极值一致稳定在初始值；驱动力幅度较大(1.2)时，Δθ先是迅速的增加，有经过一段叫缓慢的总体增长，最后其最大值也基本稳定，整个过程都无规律。

##参考

[rfhongyi](https://github.com/rfhongyi)的代码支援





