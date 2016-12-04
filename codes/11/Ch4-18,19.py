import math
import matplotlib.pyplot as plt
GM=4*(math.pi**2)
class precession:
    def __init__(self,e=0.,time=9,dt=0.0001,vcoefficient=1,beta=2,alpha=0,intial_w=0,intial_sita=0):
        self.intial_sita=intial_sita
        self.alpha=alpha
        self.beta=beta
        self.vcoefficient=vcoefficient
        self.e=e
        self.a=1/(1+e)
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=self.vcoefficient*math.sqrt((GM*(1-e))/(self.a*(1+e)))
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.w=[intial_w]
        self.sita=[intial_sita]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.ThetaPrecession=[]
        self.TimePrecession=[]
    def calculate_reset(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+self.alpha/r**2)*self.X[-1]/r**(1+self.beta))*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+self.alpha/r**2)*self.Y[-1]/r**(1+self.beta))*self.dt
            newY=self.Y[-1]+newVy*self.dt
            newW=self.w[-1]-3*GM/(r**5)*(self.X[-1]*math.sin(self.sita[-1])-self.Y[-1]*math.cos(self.sita[-1]))*(self.X[-1]*math.cos(self.sita[-1])+self.Y[-1]*math.sin(self.sita[-1]))*self.dt
            newSita=self.dt*self.w[-1]+self.sita[-1]         
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.w.append(newW)
            self.sita.append(newSita)
            self.T.append(self.T[-1]+self.dt)            
            while self.sita[-1]>=1*math.pi:
                self.sita[-1]=self.sita[-1]-2*math.pi
            while  self.sita[-1]<=-1*math.pi:
                self.sita[-1]=self.sita[-1]+2*math.pi       
    def plot(self,slogan=''):
        plt.plot(self.T,self.w)
        plt.legend(loc='upper right',frameon=False,fontsize='small')
        plt.grid(True)
        plt.title('Hyperion(Elliptical orbit) $\\theta$ versus $\\omega$')
        plt.ylabel('$\\omega(radians/yr)$')        
        plt.xlabel('$\\theta(radians)$')
a=precession()
a.calculate_reset()
a.plot()
