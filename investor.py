import math


class Investor:

    def __init__(self, data, _MACD, _SIGNAL):
        self.data = data
        self._MACD = _MACD
        self._SIGNAL = _SIGNAL
        self.units = 0
        self.capital = 1000

    def makeInvestment(self):
        self.summarizeAtTheBeginning()
        for day in range(37, 1000):
            if self.isTimeForBuy(day):
                self.sell(day)
            if self.isTimeForBuy(day):
                self.buy(day)
        self.summarizeAtTheEnd()

    def sell(self, day):
        halfOfUnits = self.units / 2
        self.capital += halfOfUnits * self.data[day];
        self.units -= halfOfUnits

    def buy(self, day):
        halfOfCapital = self.capital / 2
        self.units += halfOfCapital / self.data[day]
        self.capital -= halfOfCapital

    def isTimeForSell(self, day):
        return self._MACD[day - 1] > self._SIGNAL[day - 1] and self._MACD[day] < self._SIGNAL[day]

    def isTimeForBuy(self, day):
        return self._MACD[day - 1] < self._SIGNAL[day - 1] and self._MACD[day] > self._SIGNAL[day]

    def summarizeAtTheBeginning(self):
        print('Capital on the first day: ' + str(self.getWholeCapital(37)))
        print('(' + str(self.getCapitalInUnits(37)) + ' in ' + str(round(self.units, 2)) + ' units)\n')

    def summarizeAtTheEnd(self):
        print('Capital on the last day: ' + str(self.getWholeCapital(999)))
        print('(' + str(self.getCapitalInUnits(999)) + ' in ' + str(round(self.units, 2)) + ' units)\n')

    def getCapitalInUnits(self, day):
        return round(self.units * self.data[day], 2)

    def getWholeCapital(self, day):
        return round(self.getCapitalInUnits(day) + self.capital, 2)





