#第三次作业
###姚贵斌 2014301020066
---
##作业内容
 - 课程主页上复习这两次课程的内容，初步掌握python和matplotlib的语法规则（正在学习中）
 
 - L1：在第二次作业的基础上，让英文名在屏幕上移动起来
 - L2：在80-80点阵上用字符拼出一些内容，并让其旋转起来

---
##L1

####思路
在输出名字的基础上加入一个循环，使得：每进行一次循环，便让输出名字的点阵总体向后移动一格（在其前面多输出一个空格）,并加入清屏函数与演示函数，使其呈现移动的效果。
####代码
![L1-代码](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/%E4%BD%9C%E4%B8%9A%E4%B8%89-L1-%E4%BB%A3%E7%A0%81.png)

[链接](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/codes/Exercise03-L1)
####运行结果
![L1-结果](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/%E4%BD%9C%E4%B8%9A%E4%B8%89-L1-%E7%BB%93%E6%9E%9C.gif)

---
##L2
####代码
```python
import os
import time
a=['                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    ' 
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'      ####                ####      '
  ,'    #       ##        ##       #    '
  ,'  #            ##  ##            #  '
  ,' #               ##               # '
  ,'#                                  #'
  ,' #                                # '
  ,'   #                            #   '
  ,'     #                        #     '
  ,'       #                    #       '
  ,'         #                #         '
  ,'           #            #           '
  ,'             #        #             '
  ,'               #    #               '
  ,'                 ##                 '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '
  ,'                                    '] 
for i in range(len(a)):
    print (a[i])
time.sleep(1)
os.system('cls')
for j in range(36):
    con2=''
    for i in range(len(a)):
        con2=con2+a[i][j]
    print (con2)   
time.sleep(1) 
os.system('cls')   
for i in range(len(a)):
    print (a[i])  
time.sleep(1) 
os.system('cls')    
for j in range(36):
    con2=''
    for i in range(len(a)):
        con2=con2+a[i][j]
    print (con2)   
time.sleep(1) 
os.system('cls') 
for i in range(len(a)):
    print (a[i])
time.sleep(1)
os.system('cls')
for j in range(36):
    con2=''
    for i in range(len(a)):
        con2=con2+a[i][j]
    print (con2)   
time.sleep(1) 
os.system('cls')   
for i in range(len(a)):
    print (a[i])  
time.sleep(1) 
os.system('cls')    
for j in range(36):
    con2=''
    for i in range(len(a)):
        con2=con2+a[i][j]
    print (con2)   
time.sleep(1) 
os.system('cls')
```
####运行结果
![结果](https://github.com/Guibeen/compuational_physics_N2014301020066/blob/master/images/%E4%BD%9C%E4%B8%9A%E4%B8%89-L2-%E7%BB%93%E6%9E%9C.gif)
####感谢
rfhongyi提供的算法
####讨论
此程序中有以下不足(以后将改进)：1,旋转后横纵改变，使得心形图案在垂直对称轴方向严重拉伸变形；2,只能旋转90度，不能转满一周。
