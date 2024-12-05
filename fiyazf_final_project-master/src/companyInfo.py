import yfinance as yf
import json

class CompanyInfo:
    def __init__(self, tickerSymbol):
        """
        Provides info for the company coming from a premade text file and stock tracker
        Also allows access to photos
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
        """
        Provides the price of the company's stock, changing day to day
        Returns:
            string: a representation of the price of the stock
        """
        todays_data = self.ticker.history(period='1d')
        if todays_data.empty:
            return "Data not available"
        price = todays_data['Close'].iloc[0]
        return f"NYSE: {price:.2f} USD"
    
    def retrieveInformation(self):
        """
        Retrieves the company's information from the company's own folder in the assets folder
        Returns:
            string: the lines of the .txt file where company info is stored
        """
        folderPath = self.companyFolders.get(self.fileTicker)
        filePath = f"{folderPath}/info.txt"
        with open(filePath, "r") as file:
            lines = [line.strip() for line in file]
        return lines
    
    def retrievePhoto(self):
        """
        Retrieves the company's logo from the company's own folder in the assets folder
        Returns:
            string: the string of the filepath for the image to be used in the controller
        """
        folderPath = self.companyFolders.get(self.fileTicker)
        filePath = f"{folderPath}/logo.png"
        return filePath
    
    def CEO(self):
        """
        Filters the retrieved information to get the CEO
        Returns:
            string: name of company CEO
        """
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("CEO:"):
                return line.replace("CEO:", "").strip()
        return None
    
    def headquarters(self):
        """
        Filters the retrieved information to get the address of headquarters
        Returns:
            string: address of company headquarters
        """
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Headquarters:"):
                return line.replace("Headquarters:", "").strip()
        return None
    
    def founded(self):
        """
        Filters the retrieved information to get the founding date
        Returns:
            string: date of founding
        """
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Founded:"):
                return line.replace("Founded:", "").strip()
        return None
    
    def revenue(self):
        """
        Filters the retrieved information to get the revenue as of September 2024 for a full year
        Returns:
            string: the company revenue for a year up to September 2024
        """
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Revenue:"):
                return line.replace("Revenue:", "").strip()
        return None
    
    def name(self):
        """
        Filters the retrieved information to get the company name
        Returns:
            string: company name
        """
        lines = self.retrieveInformation()
        for line in lines:
            if line.startswith("Company:"):
                return line.replace("Company:", "").strip()
        return None