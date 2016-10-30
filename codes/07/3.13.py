import pylab as pl
import math
class oscillatory:
    def __init__(self,g=9.8,l=9.8,q=0.5,F_D=0.5,O_D=2/3,time_step=0.04,\
   total_time=80,initial_theta=0.2,initial_omega=0,initial_omega1=0,\
    initial_theta1=0.201,q1=0.5):
        self.g=g
        self.l=l
        self.q=q
        self.q1=q1
        self.F=F_D
        self.O=O_D
        self.t=[0]
        self.initial_theta=initial_theta
        self.initial_theta1=initial_theta1
        self.initial_omega=initial_omega
        self.dt=time_step
        self.time= total_time
        self.omega= [initial_omega]
        self.omega1=[initial_omega1]
        self.theta= [initial_theta]
        self.theta1= [initial_theta1]
        self.nsteps=int(total_time//time_step+1)
        self.D=[0]
        self.e=[0]
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
            tmpo1=self.omega1[i]+(-1*(self.g/self.l)*math.sin(self.theta1[i])-\
            self.q1*self.omega1[i]+self.F*math.sin(self.O*self.t[i]))*self.dt
            tmpt1=self.theta1[i]+tmpo1*self.dt
            while(tmpt1<(-1*math.pi) or tmpt1>math.pi):
                if tmpt1<(-1*math.pi):
                   tmpt1+=2*math.pi
                if tmpt1>math.pi:
                   tmpt1-=2*math.pi
            self.omega1.append(tmpo1)
            self.theta1.append(tmpt1)
            self.t.append(self.t[i]+self.dt)
            tmpD=abs(tmpt-tmpt1)
            self.D.append(tmpD)
            self.e.append(0.001*math.exp(-0.247*self.t[i]))
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,}
        pl.semilogy(self.t,self.D)
        pl.semilogy(self.t,self.e,'--')
        pl.title(r'$\Delta\theta$ versus time', fontdict = font)
        pl.xlabel('time(s)')
        pl.ylabel(r'$\Delta\theta$(radians)')
        pl.legend((['$F_D$=0.5']))
        pl.show()
a = oscillatory()
a.run()
a.show_results()
