import pandas as pd


class CsvLoader:

    @staticmethod
    def csvLoad():
        csvData = pd.read_csv("./wig20_d.csv")
        csvData = csvData[:1000]
        csvData = csvData[['Zamkniecie']]
        csvData = csvData.Zamkniecie
        return csvData
