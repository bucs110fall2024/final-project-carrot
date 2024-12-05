import pygame

class CityNode:
    def __init__(self, x, y, state):
        """
        initializes the values and actions for a node at (x, y) and assigns it a state
        Args:
            x (int): x coord
            y (int): y coord
            state (string): the state which the node is for
        Returns: none
        """

        self.rect = pygame.Rect(x-48, y-96, 96, 96)
        self.imageNormal = pygame.image.load('assets/city_node_unhighlighted.png')
        self.imageHovered = pygame.image.load('assets/city_node_highlighted.png')
        self.imageCurrent = self.imageNormal
        self.state = state
        self.stateCompaniesDict = {
            "New York": ["GS", "JPM", "C", "BLK", "MS", "BK", "SNEX"],
            "Massachusetts": ["STT", "FNF"],
            "California": ["CGHC", "PHK", "BEN"],
            "Pennsylvania": ["VTI"],
            "Missouri": ["JNSXX"],
            "Georgia": ["IVZ"],
            "North Carolina": ["BAC"],
            "Iowa": ["TSTRX"],
            "South Dakota": ["WFC"],
        }

    def createNode(self, screen):
        """
        creates the node on the display
        Args:
            screen (pygame.Surface): the display on which the node is created
        """
        screen.blit(self.imageCurrent, self.rect.topleft)
        
    def nodeClicked(self, mousePos):
        """
        checks whether or not the node has been clicked
        Args:
            mousePos (tuple): is the coordinates of the mouse cursor
        Returns:
            boole: True if mouse hovers over node, false if not
        """
        return self.rect.collidepoint(mousePos)
    
    def tickersByState(self, state):
        """
        returns the list of ticker values of companies within a state using the dictionary in the initialization
        Args:
            state (string): the state from which the ticker values will be taken

        Returns:
            list: the list of ticker values of the companies within the state
        """
        return self.stateCompaniesDict.get(state, [])