import pygame

class Controller:
  
#   def __init__(self):
    #setup pygame data
    
  def mainloop(self):
    while(True): #this can also be a variable instead of just True
      #1. Handle events
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()
  
  ### below are some sample loop states ###

#   def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
#   def gameloop(self):
      #event loop

      #update data

      #redraw
    
#   def gameoverloop(self):
      #event loop

      #update data

      #redraw
