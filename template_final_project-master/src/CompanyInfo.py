import stockquotes

class CompanyInfo:
    def __init__(self, companyName, fileName, tickerSymbol):
        """
        Provides info for the company coming from a premade text file
        Args:
            companyName (str): company name
            fileName (str): name of file for the company
            tickerSymbol (str): ticker symbol for the company
        """
        
        self.name = companyName
        self.info = fileName # in reality, this will be reading from a text file and be inputting the information in a standardized format
        companyStock = stockquotes.Stock(tickerSymbol)
        self.stockPrice = companyStock.current_price