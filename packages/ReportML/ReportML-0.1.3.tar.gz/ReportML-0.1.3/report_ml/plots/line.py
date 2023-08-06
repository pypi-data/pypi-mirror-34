import matplotlib.pyplot as plt
from report_ml.plots.plot_instance import PlotInstance

class LinePlot(PlotInstance):
    def __init__(self,*args):
        super(LinePlot, self).__init__(*args)

    def start(self):
        for i in range(0,len(self.data)):
            plt.plot(self.data[i])
