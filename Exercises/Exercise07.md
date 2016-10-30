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
