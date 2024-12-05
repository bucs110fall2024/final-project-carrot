import yfinance as yf
import json

class CompanyInfo:
    def __init__(self, companyName, tickerSymbol):
        """
        Provides info for the company coming from a premade text file
        Args:
            companyName (str): company name
            fileName (str): name of file for the company
            tickerSymbol (str): ticker symbol for the company
        """
        self.name = companyName
        self.ticker = yf.Ticker(tickerSymbol)
        self.fileTicker = tickerSymbol
        with open("assets/companyFolders.json", "r") as file:
            self.companyFolders = json.load(file)
        
    def stockPrice(self):
        todays_data = self.ticker.history(period='1d')
        return todays_data['Close'].iloc[0]
    
    def retrieveInformation(self, ticker):
        folderPath = self.companyFolders.get(ticker)
        filePath = f"{folderPath}/info.txt"
        print(filePath)
    
CompanyInfo('Goldman Sachs', 'GS').retrieveInformation('GS')