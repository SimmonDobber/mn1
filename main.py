import plotMaker
import csvLoader
import dataParser
import investor

data = csvLoader.CsvLoader.csvLoad()
dataParser = dataParser.DataParser(data)
_MACD = dataParser.getMACD()
_SIGNAL = dataParser.getSIGNAL()
plotMaker = plotMaker.PlotMaker(data, _MACD, _SIGNAL)
investor = investor.Investor(data, _MACD, _SIGNAL)

plotMaker.makePlots()
investor.makeInvestment()






