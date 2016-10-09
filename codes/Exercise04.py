import pylab as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Program to accompany 'Computational Physics' by Cai Hao
    """
    def __init__(self, number_of_nuclei_A = 0, number_of_nuclei_B= 100,\
    time_constant_A = 2, time_constant_B= 1, time_of_duration = 10,\
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
        plot1, = pl.plot(self.t, self.n1_uranium)
        plot2, = pl.plot(self.t, self.n2_uranium)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        first_legend=pl.legend([plot1, plot2],['A', 'B'], loc='best')
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
