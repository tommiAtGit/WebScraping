class StockValue:
    def __init__(self, stockPrefix, openValue,openDate,closeValue, closeDate,buyValue, sellValue, highValue, lowValue):
        self.stockPrefix = stockPrefix
        self.openValue = openValue
        self.openDate = openDate
        self.closeValue = closeValue
        self.closeDate =  closeDate
        self.buyValue =  buyValue
        self.sellValue = sellValue
        self.highValue =  highValue
        self.lowValue = lowValue

    def getstockPrefix(self):
            return self.stockPrefix
    def getOpenValue(self):
            return self.openValue
    def getOpenDate(self):
            return self.openDate
    def getCloseValue(self):
            return self.closeValue
    def getCloseDate(self):
            return self.closeDate
    def getBuyValue(self):
            return self.buyValue
    def getSellValue(self):
            return self.sellValue
    def getHighValue(self):
            return self.highValue
    def getLowValue(self):
            return self.lowValue
