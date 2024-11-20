import stockquotes

class CompanyInfo:
    def __init__(self, companyName, fileName, tickerSymbol):
        self.name = companyName
        self.info = fileName # in reality, this will be reading from a text file and be inputting the information in a standardized format
        companyStock = stockquotes.Stock(tickerSymbol)
        self.stockPrice = companyStock.current_price