import random
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


def seed(): #activates the RNG 
   random.seed
   return


def genlvl(size): #creates an array of numbers that represents a level of a defined number of platforms
   counter = 0
   level = []
   while counter < size:
      platform = genplatform(counter) #creates a platform to be put into the level
      level.append(platform)
      counter += 1
   print(level) #flag for testing
   
   return level
   
def buildlvl(level, screen): #converts the array from genlvl into actual platforms
   for x in range(len(level)):
      for y in range(len(level[x])): 
         platbuild(level[x][y][0], level[x][y][1], level[x][y][2], screen)
   
 
   return
 
    

def gentutorial():
    
   return


def genplatform(platformnum): #creates individual platforms
   platform = []
   if platformnum == 0:
    xcord = 50
    ycord = 400
    state = 11
    platform.append([xcord, ycord, state])  
   else:
      xcord = random.randrange(100, 5000, 10)
      ycord = random.randrange(120, 700, 10)
      state = random.randrange(1, 10, 1)
      platform.append([xcord, ycord, state])  
   return platform



def xedgebuild(screen):
   pygame.draw.rect(screen, red, (0, 0, 5, 800), 0) 

   
   return

def floorbuild(screen):
   pygame.draw.rect(screen, red, (0, 795, 1000, 5), 0) 

   
   return

def topbuild(screen):
   pygame.draw.rect(screen, red, (0, 0, 1000, 5), 0) 





def platbuild(xcord, ycord, state, screen):
   platwidth = 120 
   platheight = 50
   if state <= 5:
      pygame.draw.rect(screen, green, (xcord, ycord, platwidth, platheight), 0)
   elif 5 < state <= 10:
      pygame.draw.rect(screen, blue, (xcord, ycord, platwidth, platheight), 0)
   else:
      pygame.draw.rect(screen, black, (xcord, ycord, platwidth, platheight), 0)
   return
 
