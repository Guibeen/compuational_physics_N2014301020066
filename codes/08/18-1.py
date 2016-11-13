import pylab as pl
import math
class oscillatory:
    def __init__(self,g=9.8,l=9.8,q=0.5,F_D=1.465,O_D=2/3,time_step=3*math.pi/100,\
    total_time=100,initial_theta=0.2,initial_omega=0):
        self.g=g
        self.l=l
        self.q=q
        self.F=F_D
        self.O=O_D
        self.t=[0]
        self.initial_theta=initial_theta
        self.initial_omega=initial_omega
        self.dt=time_step
        self.time= total_time
        self.omega= [initial_omega]
        self.theta= [initial_theta]
        self.nsteps=int(total_time//time_step+1)
        self.tmpo=[0]
        self.tmpt=[0]
    def run(self):
        for i in range(self.nsteps):
            tmpo=self.omega[i]+(-1*(self.g/self.l)*math.sin(self.theta[i])-\
            self.q*self.omega[i]+self.F*math.sin(self.O*self.t[i]))*self.dt
            tmpt=self.theta[i]+tmpo*self.dt
            while(tmpt<(-1*math.pi) or tmpt>math.pi):
                if tmpt<(-1*math.pi):
                   tmpt+=2*math.pi
                if tmpt>math.pi:
                   tmpt-=2*math.pi
            self.omega.append(tmpo)
            self.theta.append(tmpt)
            self.t.append(self.t[i]+self.dt)
        for i in range(len(self.t)):
            if self.t[i]//(3*math.pi)>300:
                if ((2/3*self.t[i])%(2*math.pi))<=(2/3*self.dt*0.5)\
                or (2*math.pi-((2/3*self.t[i])%(2*math.pi)))<=(2/3*self.dt*0.5):
                    self.tmpo.append(self.omega[i])
                    self.tmpt.append(self.theta[i])   
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,}
        pl.plot(self.t,self.theta)
        #pl.scatter(self.tmpt, self.tmpo)
        pl.title(r'$\theta$ versus t', fontdict = font)
        pl.xlabel(r't(s)')
        pl.ylabel(r'$\theta$(radian)')
        pl.xlim(0,100)
        pl.ylim(-4,4)
        pl.legend((['$F_D$=1.465']))
        pl.show()
a = oscillatory()
a.run()
a.show_results()
