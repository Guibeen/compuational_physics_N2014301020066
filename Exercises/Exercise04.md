# 第四次作业

###姚贵斌 2014301020066 

---
##作业内容

###problem1.5

Consider again a decay problem with two types of nuclei $A$ and $B$, but now suppose that nuclei of type $A$ decay into ones of type $B$, while nuclei of type $B$ decay into ones of type $A$. Strictly speaking, this is not a "decay" process, since it is possible for the type $B$ nuclei to turn back into type $A$ nuclei.  $A$ better analogy would better be a resonance in which a system can tunnel or move back and forth between two states $A$ and $B$ which have equal energies. The corresponding rate equations are
$$\frac{dN_A}{dt}=\frac{N_B}{\tau}-\frac{N_A}{\tau}$$
$$\frac{dN_B}{dt}=\frac{N_A}{\tau}-\frac{N_B}{\tau}$$
Where for simplicity we have assumed that the two types of decay are characterized by the same time constant, $\tau$. Solve this system of equations fo the numbers of nuclei, $N_A$ and $N_B$, as functions of time. Consider different initial conditions, such as $N_A=100,N_B=0,$,etc.,and take $\tau$=1s. Show that your numeral results are consistant with the idea that the system reaches a steady state in which $N_A$ and$N_B$ are costant. In such a steady state, the time derivatives $dN_A/dt$ and $dN_B/dt$ should vanish.  
##思路
仿照第一章课件中的方法。只是将原来的单种核变成两种核。
##代码

``` 
import pylab as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Program to accompany 'Computational Physics' by Cai Hao
    """
    def __init__(self, number_of_nuclei_A = 80, number_of_nuclei_B=20,\
    time_constant_A = 1, time_constant_B=1, time_of_duration = 4,\
    time_step = 0.05):
        # unit of time is second
        self.n1_uranium = [number_of_nuclei_A]
        self.n2_uranium = [number_of_nuclei_B]
        self.t = [0]
        self.tau1 = time_constant_A
        self.tau2 = time_constant_B
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant A ->", time_constant_A)
        print("Time constant B ->", time_constant_B)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
           tmp1 = self.n1_uranium[i] - self.n1_uranium[i] /self.\
           tau1 * self.dt+self.n2_uranium[i] / self.tau2 * self.dt
           tmp2 = self.n2_uranium[i] - self.n2_uranium[i] /self.\
           tau2 *self.dt+self.n1_uranium[i] / self.tau1 * self.dt
           self.n1_uranium.append(tmp1)
           self.n2_uranium.append(tmp2)
           self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n1_uranium)
        pl.plot(self.t, self.n2_uranium)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n1_uranium[i], file = myfile)
            print(self.t[i], self.n2_uranium[i], file = myfile)
        myfile.close()
a = uranium_decay()
a.calculate()
a.show_results()
a.store_results()
```
##结果
$1，N_A=100，N_B=0$
![结果图1]()

