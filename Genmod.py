import random
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


dif = 1
disdif = 5*dif #distance between platforms modifier

def seed(): #activates the RNG 
   random.seed
   return


def genlvl(size): #creates an array of numbers that represents a level of a defined number of chunks
   #size = int(input("How large of a level do you want? ")) 
   counter = 0
   level = []
   dif = 1
   disdif = 5*dif #distance between platforms modifier
   while counter < size:
      chunk = genchunk(counter) #creates a chunk to be put into the level
      level.append(chunk)
      counter += 1
   print(level) #flag for testing
   
   return level
   
def buildlvl(level, screen): #converts the array from genlvl into actual platforms
   for x in range(len(level)):
      for y in range(len(level[x])): 
         platbuild(level[x][y][0], level[x][y][1], screen)
   
 
   return
 
    

def gentutorial():
    
   return


def genchunk(chunknum): #creates individual chunks
   chunk = []
   NoP = 1 #number of platforms per chunk
   counter = 0
   while counter < NoP:#this number is the number of platforms per chunk
      xcord = random.randrange(0, 1000, 1*disdif)
      ycord = random.randrange(0, 800, 1*disdif)
      chunk.append([xcord, ycord])
      counter += 1
     
   return chunk



def xedgebuild(screen):
   pygame.draw.rect(screen, red, (0, 0, 5, 800), 0) 

   
   return

def floorbuild(screen):
   pygame.draw.rect(screen, red, (0, 795, 1000, 5), 0) 

   
   return

def topbuild(screen):
   pygame.draw.rect(screen, red, (0, 0, 1000, 5), 0) 





def platbuild(xcord, ycord, screen):
   platwidth = int(100) 
   platheight = int(50)
   platform = pygame.draw.rect(screen, green, (xcord, ycord, platwidth, platheight), 0)
   return
 
