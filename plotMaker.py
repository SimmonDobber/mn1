import matplotlib.pyplot as plt


class PlotMaker:

    def __init__(self, csvData, _MACD, _SIGNAL):
        self.data = csvData
        self._MACD = _MACD
        self._SIGNAL = _SIGNAL

    def makePlots(self):
        self.showMACDPlot()
        self.showDataPlot()
        self.showDataAndMACDPlot()

    def showMACDPlot(self):
        self.plotMACD()
        plt.show()

    def showDataPlot(self):
        self.plotData()
        plt.show()

    def plotMACD(self):
        plt.plot(self._SIGNAL, label='SIGNAL', color='blue', linewidth=1)
        plt.plot(self._MACD, label='MACD', color='red', linewidth=1)
        plt.xlabel('day')
        plt.ylabel('value')
        plt.legend(loc='center left')

    def plotData(self):
        plt.plot(self.data, label='data', color='green', linewidth=1)
        plt.xlabel('day')
        plt.ylabel('value')

    def showDataAndMACDPlot(self):
        self.plotData()
        self.plotMACD()
        plt.show()
