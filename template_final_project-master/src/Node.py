import CompanyInfo

class Node:
    def __init__(self, x, y, companyName, companyLogo):
        self.x = x
        self.y = y
        self.name = companyName
        self.clickable = True
        self.logo = companyLogo # file string
        self.size = 5 # arbitrary number