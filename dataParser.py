

class DataParser:

    def __init__(self, csvData):
        self.data = csvData
        self._MACD = self.initMACD(self.data)
        self._SIGNAL = self.initSIGNAL(self._MACD)

    def initMACD(self, data):
        _MACD = [0 for _ in range(1000)]
        for day in range(26, 1000):
            _MACD[day] = self.getEMA(data, day, 12) - self.getEMA(data, day, 26)
        return _MACD

    def initSIGNAL(self, _MACD):
        _SIGNAL = [0 for _ in range(1000)]
        for day in range(35, 1000):
            _SIGNAL[day] = self.getEMA(_MACD, day, 9)
        return _SIGNAL

    def getEMA(self, data, currentDay, n):
        oneMinusAlpha = (n - 1) / (n + 1)
        nominator = self.getEMANominator(data, currentDay, n, oneMinusAlpha)
        denominator = self.getEMADenominator(n, oneMinusAlpha)
        return nominator / denominator

    def getEMANominator(self, data, currentDay, n, oneMinusAlpha):
        nominator = 0
        for i in range(0, n + 1):
            nominator += data[currentDay - i] * pow(oneMinusAlpha, i)
        return nominator

    def getEMADenominator(self, n, oneMinusAlpha):
        denominator = 0
        for i in range(0, n + 1):
            denominator += pow(oneMinusAlpha, i)
        return denominator

    def getMACD(self):
        return self._MACD

    def getSIGNAL(self):
        return self._SIGNAL