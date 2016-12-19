import pylab as pl
import math
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq
dx = 0.01
dt = 0.0001/3
r = 1.0
c = r*dx/dt
L = 1.0                # the length of the string
t = 0.5                  # the total time
ls = int(L/dx)         # length scope=33
ts = int(t/dt)         # time scope
k = 1000
y = [[0 for i in range(ls)]for j in range(ts)]
x = []
yo = []
for i in range(ls):
    y[0][i] = math.exp(-k*(i*dx-0.5-0.05)**2)
    y[1][i] = math.exp(-k*(i*dx-0.5-0.05)**2)
for n in range(1,ts-1):
    y[n][0] = 0
    y[n][-1] = 0
    for i in range(1,ls-1):
        y[n+1][i] = -1*y[n-1][i]+r**2*(y[n][i+1]+y[n][i-1])
for k in range(ts):
    x.append(k*dt)
    yo.append(y[k][50])
def signal():
    #pl.figure(figsize=(6,5))
    pl.plot(x,yo)
    pl.title('exited at 0.50, observed at 0.50')
    pl.xlim(0.,0.035)
    pl.ylim(-.6,.6)
    pl.xlabel('time/s')
    pl.ylabel('signal(arbitary units)')
    pl.show()
def frequency():
    #t_plot = np.arange(0,t,dt)
    amplitude_record = []
    for i in range(ts):
        amplitude_record.append(y[i][20])
    freq = fftfreq(len(amplitude_record), d=dt)
    freq = np.array(abs(freq))
    f_signal = rfft(amplitude_record)
    f_signal = np.array(f_signal**2)
       #plt.subplot(122)
    pl.title('Power spectra')
    pl.ylabel('Power (arbitrary units)')
    pl.xlabel('Frequency (Hz)')
    pl.xlim(0,4000)
    
    pl.plot(freq,f_signal,label = 'epsilon = ')#+str(self.e))
    pl.legend(['xo=0.50'])
signal()
frequency()
