import pygame
from src.cityNode import CityNode
from src.stateInfo import StateInfo
from src.companyInfo import CompanyInfo

class Controller:
      def __init__(self):
            """
            is the controller for the whole thing to run
            """
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
            
            self.regularFont = 'assets/Montserrat-VariableFont_wght.ttf'
            # preset font sizes for simplicity
            self.fontsize1 = 65
            self.fontsize2 = 50
            self.fontsize3 = 40
            self.fontsize4 = 35
            self.fontsize5 = 30
            self.fontsize6 = 24
            self.fontsize7 = 18
            self.fontsize8 = 10
            
            # here im caching values, otherwise is runs REALLY slowly
            # i had to watch a whole tutorial for this
            self.statePopulationCache = {}
            self.stateGDPCache = {}
            
            # a bunch of initialization
            self.currentPopulation = None
            self.stateInfo = None
            self.currentGDP = None
            
            self.showCompanies = False
            
            self.selectedState = None
            self.selectedCompanies = []
            
            self.currentCompanyIndex = 0
            
      def mainloop(self):
            """
            is the mainloop for the program to run and redraw
            """
            def displayText(text, coordinates, fontSize):
                  """
                  makes it easier to displayText on screen by compacting it in one function
                  Args:
                      text (string): the text to be shown on screen
                      coordinates (tuple): contains the x and y coordinates for the text to be placed
                      fontSize (integer): desired size of the text to be displayed
                  """
                  font = pygame.font.Font(self.regularFont, fontSize)
                  font.set_bold(True)
                  toRender = font.render(text, True, (255, 255, 255))
                  self.display.blit(toRender, coordinates)
                  
            state = None
            while self.running:  # Main game loop
                  self.display.blit(self.background, (0, 0))
                  
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              self.running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                              mousePos = pygame.mouse.get_pos()
                              nodeClicked = False
                              print(mousePos)
                              for node in self.nodes:
                                    if node.nodeClicked(mousePos):
                                          print(f"Clicked on {node.state}")
                                          self.selectedState = node.state
                                          self.selectedCompanies = node.tickersByState(node.state)
                                          self.showCompanies = True
                                          self.currentCompanyIndex = 0
                                          nodeClicked = True
                                          break
                                    
                                    if not nodeClicked:
                                          self.showCompanies = False
                                          self.selectedState = None
                                          self.selectedCompanies = []
                        elif event.type == pygame.KEYDOWN:
                              if self.showCompanies:
                                    if event.key == pygame.K_RIGHT:  # Go to next company
                                          self.currentCompanyIndex = (self.currentCompanyIndex + 1) % len(self.selectedCompanies)
                                    elif event.key == pygame.K_LEFT:  # Go to previous company
                                          self.currentCompanyIndex = (self.currentCompanyIndex - 1) % len(self.selectedCompanies)
                  
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
                        else:
                             state = None
                             
                  for node in self.nodes:
                        node.createNode(self.display)
                  
                  if state is not None:
                        displayText(state, (15, 552), self.fontsize2)
                        displayText(str(self.currentPopulation), (15, 615), self.fontsize4)
                        displayText(str(self.currentGDP), (15, 655), self.fontsize4)
                  else:
                        displayText("The United States of America", (15, 565), self.fontsize1)
                  
                  if self.showCompanies:
                        displayText("Companies in", (972, 9), self.fontsize5)
                        displayText(f"{self.selectedState}", (970, 37), self.fontsize3)
                        displayText("Use left and right arrow keys", (992, 678), self.fontsize7)
                        displayText("New York, California, and Massachusetts specifically", (989, 700), self.fontsize8)
                        
                        if self.selectedCompanies:
                              shownCompanyTicker = self.selectedCompanies[self.currentCompanyIndex]
                              company = CompanyInfo(shownCompanyTicker)
                              displayText(company.name(), (970, 90), self.fontsize6)
                              displayText("CEO: " + company.CEO(), (968, 200), self.fontsize6)
                              displayText(shownCompanyTicker, (968, 120), self.fontsize3)
                              displayText("Headquarters: " + company.headquarters(), (968, 230), self.fontsize8)
                              displayText("Founded " + company.founded(), (968, 240), self.fontsize7)
                              displayText("Revenue: " + company.revenue(), (968, 260), self.fontsize8)
                              displayText(company.stockPrice(), (968, 160), self.fontsize4)
                              
                              logo = company.retrievePhoto()
                              logo = pygame.image.load(logo)
                              logo = pygame.transform.scale(logo, (275, 275))
                              self.display.blit(logo, (982, 300))
                              
                  pygame.display.flip()
                  self.clock.tick(60)
                  
            pygame.quit()