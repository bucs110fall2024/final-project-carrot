from companyInfo import CompanyInfo

class Node:
    def __init__(self, x, y, companyName, companyLogo):
        """
        Creates a node at (x, y) with the company logo
        Args:
            x (int): x coord
            y (int): y coord
            companyName (string): name of company
            companyLogo (string): logo file name
        Returns: none
        """
        
        self.x = x
        self.y = y
        self.name = companyName
        self.clickable = True
        self.logo = companyLogo # file string
        self.size = 5 # arbitrary number
        
    def openWindowOnClick(self):
        """
        Opens a window upon the user clicking on the window,
        will not open more than one window per node at a time
        args: none
        returns: none
        """