import pygame
from src.cityNode import CityNode
from src.stateInfo import StateInfo

class Controller:
      def __init__(self):
            pygame.init()
            self.display = pygame.display.set_mode((1280, 720))
            pygame.display.set_caption("United State Financial Services Company Map")
            self.clock = pygame.time.Clock()
            self.running = True
            self.background = pygame.image.load('assets/game_screen.png')
            self.nodes = [
                  CityNode(198, 232, 'California'),
                  CityNode(868, 172, 'Massachusetts'),
                  CityNode(806, 197, 'Pennsylvania'),
                  CityNode(592, 205, 'Iowa'),
                  CityNode(608, 255, 'Missouri'),
                  CityNode(757, 377, 'Georgia'),
                  CityNode(812, 303, 'North Carolina'),
                  CityNode(513, 161, 'South Dakota'),
                  CityNode(820, 176, 'New York')
            ]
            self.font1 = pygame.font.Font('assets/Montserrat-VariableFont_wght.ttf', 50)
            self.font1.set_bold(True)
            self.font2 = pygame.font.Font('assets/Montserrat-VariableFont_wght.ttf', 35)
            
            self.statePopulationCache = {}
            self.stateGDPCache = {}
            
            self.currentPopulation = None
            self.stateInfo = None
            self.currentGDP = None
            
      def mainloop(self):
            state = None
            population = None
            while self.running:  # Main game loop
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              self.running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                              mousePos = pygame.mouse.get_pos()
                              print(mousePos)
                              for node in self.nodes:
                                    if node.nodeClicked(mousePos):
                                          print(f"Clicked on {node.state}")
                                          break

                  self.display.blit(self.background, (0, 0))
                  
                  mousePos = pygame.mouse.get_pos()
                  
                  for node in self.nodes:
                        node.imageCurrent = node.imageNormal
                  for node in self.nodes:
                        if node.rect.collidepoint(mousePos):
                              node.imageCurrent = node.imageHovered
                              state = node.state
                              
                              if state not in self.statePopulationCache:
                                    self.statePopulationCache[state] = StateInfo(state).population()
                              self.currentPopulation = self.statePopulationCache[state]
                              
                              if state not in self.stateGDPCache:
                                    self.stateGDPCache[state] = StateInfo(state).gdp()
                              self.currentGDP = self.stateGDPCache[state]
                              
                              break
                  for node in self.nodes:
                        node.createNode(self.display)
                  
                  if state is not None:
                        stateNameDisplay = self.font1.render(state, True, (255, 255, 255))
                        self.display.blit(stateNameDisplay, (15, 552))
                        
                        statePopulationDisplay = self.font2.render(str(self.currentPopulation), True, (255, 255, 255))
                        self.display.blit(statePopulationDisplay, (15, 615))
                        
                        stateGDPDisplay = self.font2.render(str(self.currentGDP), True, (255, 255, 255))
                        self.display.blit(stateGDPDisplay, (15, 655))
                        
                  pygame.display.flip()
                  self.clock.tick(60)
                  
            pygame.quit()