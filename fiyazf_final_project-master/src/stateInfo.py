import pygame
import censusdata

class StateInfo:
    def __init__(self, state):
        self.apiKey = 'cb9ca5d419e6459b5325c1b345707eb089a69540'
        
        self.state = state
        
        self.stateData = {
            'New York': {'fip': '36', 'gdp': '1,751,000 million USD'},
            'Massachusetts': {'fip': '25', 'gdp': '640,000 million USD'},
            'California': {'fip': '06', 'gdp': '3,000,000 million USD'},
            'Pennsylvania': {'fip': '42', 'gdp': '750,000 million USD'},
            'Missouri': {'fip': '29', 'gdp': '300,000 million USD'},
            'Georgia': {'fip': '13', 'gdp': '600,000 million USD'},
            'North Carolina': {'fip': '37', 'gdp': '600,000 million USD'},
            'Iowa': {'fip': '19', 'gdp': '200,000 million USD'},
            'South Dakota': {'fip': '46', 'gdp': '52,000 million USD'}
        }
        
    def population(self):
        stateData = self.stateData.get(self.state)
        stateFip = stateData['fip']
        
        data = censusdata.download('acs5', 2020,
                                       censusdata.censusgeo([('state', stateFip)]),
                                       ['B01003_001E'])
        self.population = data['B01003_001E'].iloc[0]
        return(f"Population (as of 2020): {self.population}")
    
    def gdp(self):
        stateData = self.stateData.get(self.state)
        self.gdp = stateData['gdp']
        return(f"Approximated GDP (2024): {self.gdp}")