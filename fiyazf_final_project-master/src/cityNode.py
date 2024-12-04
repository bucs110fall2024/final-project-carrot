import pygame

class CityNode:
    def __init__(self, x, y, state):
        """
        Creates a node at (x, y)
        Args:
            x (int): x coord
            y (int): y coord
        Returns: none
        """

        self.rect = pygame.Rect(x-48, y-96, 96, 96)
        self.imageNormal = pygame.image.load('assets/city_node_unhighlighted.png')
        self.imageHovered = pygame.image.load('assets/city_node_highlighted.png')
        self.imageCurrent = self.imageNormal
        self.state = state

    def createNode(self, screen):
        screen.blit(self.imageCurrent, self.rect.topleft)
        
    def nodeClicked(self, mousePos):
        return self.rect.collidepoint(mousePos)