import matplotlib.pyplot as plt
from plot_instance import PlotInstance

class ScatterPlot(PlotInstance):
    def __init__(self,*args):
        super(ScatterPlot, self).__init__(*args)

    def start(self):
        for i in range(0,len(self.data)):
            plt.scatter(range(len(self.data[i])), self.data[i])
