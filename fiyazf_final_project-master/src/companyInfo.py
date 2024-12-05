import yfinance as yf
import json

class CompanyInfo:
    def __init__(self, tickerSymbol):
        """
        Provides info for the company coming from a premade text file
        Args:
            companyName (str): company name
            fileName (str): name of file for the company
            tickerSymbol (str): ticker symbol for the company
        """
        self.ticker = yf.Ticker(tickerSymbol)
        self.fileTicker = tickerSymbol
        with open("assets/companyFolders.json", "r") as file:
            self.companyFolders = json.load(file)
        
    def stockPrice(self):
        todays_data = self.ticker.history(period='1d')
        if todays_data.empty:
            return "Data not available"
        price = todays_data['Close'].iloc[0]
        return f"NYSE: {price:.2f} USD"
    
    def retrieveInformation(self):
        folderPath = self.companyFolders.get(self.fileTicker)
        filePath = f"{folderPath}/info.txt"
        with open(filePath, "r") as file:
            lines = [line.strip() for line in file]
        return lines
    
    def retrievePhoto(self):
        folderPath = self.companyFolders.get(self.fileTicker)
        filePath = f"{folderPath}/logo.png"
        return filePath
    
    def CEO(self):
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("CEO:"):
                return line.replace("CEO:", "").strip()
        return None
    
    def headquarters(self):
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Headquarters:"):
                return line.replace("Headquarters:", "").strip()
        return None
    
    def founded(self):
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Founded:"):
                return line.replace("Founded:", "").strip()
        return None
    
    def revenue(self):
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Revenue:"):
                return line.replace("Revenue:", "").strip()
        return None
    
    def name(self):
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Company:"):
                return line.replace("Company:", "").strip()
        return None