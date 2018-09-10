#!/usr/local/bin/python3.5m

import pygame
import Genmod
import random

FPS = 60 #frames per second setting

fpsClock = pygame.time.Clock()

pygame.init()


"""colors"""
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)



"""screen dimensions"""
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

HALF_SCREEN_WIDTH = int(SCREEN_WIDTH / 2)
HALF_SCREEN_HEIGHT = int(SCREEN_HEIGHT / 2)



"""Starting stats"""
Xspeed = 25
Yspeed = 25
Gravity = 2
airtick = 0


"""player sprites and locations"""
gas_sprite = pygame.image.load('gas_sprite.png')
solid_sprite = pygame.image.load('solid_sprite.png')
liquid_sprite = pygame.image.load('liquid_sprite.png')


# default platform size
platwidth = int(100) 
platheight = int(50)


#location of sprite (middle of screen as of now)
playerx = HALF_SCREEN_WIDTH
playery = HALF_SCREEN_HEIGHT

#player details
player = solid_sprite
playersizex = 83
playersizey = 68

player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right


global level
global levelsize
levelsize = 3
level = Genmod.genlvl(levelsize)

    

"""screen details"""
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stayt")

cameralimit = 420
cameralimitleft = 360
cameralimitright = 700
cameralimitup = 300
cameralimitdown = 1000

camerax = 0
cameray = 0
print(camerax)
print(cameray)


"""render objects"""
def render_objects(X, Y) : #,state)
    screen.blit(player, (playerx, playery))
    Genmod.buildlvl(level, screen)
    Genmod.floorbuild(screen)
    Genmod.topbuild(screen)
    

"""Calculate gravity"""
def CalcGrav():
    global Gravity
    global playery
    global airtick
    playery += Gravity*airtick
    if airtick > 50:
     airtick = 50
 
 
"""Collision detections"""


"""Collision with the floor and celling"""
def BorderCol():
    global playerx
    global playery
    global airtick
    global playersizex
    global playersizey
    global SCREEN_HEIGHT
    global SCREEN_WIDTH
    
    
    if playery + playersizey > SCREEN_HEIGHT - 5:
     playery = SCREEN_HEIGHT - 5 - playersizey
     airtick = 0
    if playery + playersizey == SCREEN_HEIGHT - 5:
     airtick = 0
     
    if playery + playersizey < 0:
     playery = 0 + playersizey

     
     
     


"""Collision with Platform"""
def PLatCol():
    global playerx
    global playery
    global levelsize
    global airtick
    global playersizex
    global playersizey
    
    colision = False 
    for x in range(len(level)):
     for y in range(len(level[x])): 
        if playerx + playersizex < level[x][y][0]: #top
            sidecol = 'top'
        elif playerx > level[x][y][0] + platwidth: #bottom
            sidecol = 'bottom'
        elif playery + playersizey < level[x][y][1]: #left
            sidecol = 'left'
        elif playery > level[x][y][1] + platheight: #right
            sidecol = 'right'     
        else:
         colision = True
         
           # playery = level[x][y][1] - playersizey
    if colision == True:
        airtick = 0
          
    else:
       airtick += 1
        
        


"""moving the camera"""
def move_camera() :
    global playerx
    global playery 
    
    global cameralimit
    global cameralimitleft
    global cameralimitright
    global cameralimitup
    global cameralimitdown
    
    global camerax
    global cameray
    global HALF_SCREEN_HEIGHT
    global HALF_SCREEN_WIDTH
    
    playerCenterx = playerx + int(playerx / 2)
    playerCentery = playery + int(playery / 2)
    if (camerax + HALF_SCREEN_WIDTH) - playerCenterx > cameralimitleft:
        playerx += 25
        for x in range(len(level)):
             for y in range(len(level[x])): 
                 level[x][y][0] += 25
                 
    elif playerCenterx - (camerax + HALF_SCREEN_WIDTH) > cameralimitright:
        playerx -= 25
        for x in range(len(level)):
            for y in range(len(level[x])): 
                level[x][y][0] -= 25
                
""" if (cameray + HALF_SCREEN_HEIGHT) - playerCentery > cameralimitup:
        playery += 25
        for x in range(len(level)):
            for y in range(len(level[x])): 
                level[x][y][1] += 25 
        
    elif playerCentery - (cameray + HALF_SCREEN_HEIGHT) > cameralimitdown:
        playery -= 25
        for x in range(len(level)):
            for y in range(len(level[x])): 
                level[x][y][1] -= 25 
        """

    
"""movement options"""
pressed_right = False
pressed_left = False
pressed_down = False
pressed_up = False

def go_right() :
    #moves player right
    global playerx
    playerx += Xspeed

def go_left() :
    #moves player left
    global playerx
    playerx -= Xspeed #speed at which the player moves

def go_up() :
    #moves player up
    global playery
    playery -= Yspeed #speed at which the player moves

def go_down() :
    #moves player up
    global playery
    playery += Yspeed #speed at which the player moves


"""key presses"""
def pressed_keys(pygame) :
    #which global variables the function is referencing
    global Gravity
    global player
    global playerx
    global playery
    global current_state
    global player_faceleft
    global player_faceright
    global playersizex
    global playersizey
    
    global pressed_right
    global pressed_left
    global pressed_down
    global pressed_up
    
    for event in pygame.event.get():
        #when a button is pressed
        if event.type == pygame.KEYDOWN:
            
            #moving left
            if event.key == pygame.K_LEFT:
                print('you hit left')
                pressed_left = True
                player = player_faceleft
                #go_left()
                
            #moving right
            if event.key == pygame.K_RIGHT:
                print ('you hit right')
                pressed_right = True
                player = player_faceright
                #go_right()
                
            #moving up/jumping
            if event.key == pygame.K_UP:
                print('you hit up')
                pressed_up = True
                #go_up()
                
            #changing state to solid
            if event.key == pygame.K_a:
                print('You changed to Solid')
                player = solid_sprite
                player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
                player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right
                Xspeed = 25
                Yspeed = 25
                Gravity = 2
                playersizex = 83
                playersizey = 68        
                
            #changing state to gas
            if event.key == pygame.K_s:
                print('You changed to Gas')
                player = gas_sprite
                player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
                player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right
                Xspeed = 0
                Yspeed = 0
                Gravity = -1
                playersizex = 92
                playersizey = 62
                
            #changing state to liquid
            if event.key == pygame.K_d:
                print('You changed to Liquid')
                player = liquid_sprite
                player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
                player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right
                Xspeed = 50
                Yspeed = 25
                Gravity = 1
                playersizex = 78
                playersizey = 51
            
            #closing game
            if event.key == pygame.K_ESCAPE:
                    print('You hit escape')
                    print('That quits the game')
                    quit()
        
        #when a button isnt pressed            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_left = False
            if event.key == pygame.K_RIGHT:
                pressed_right = False
            if event.key == pygame.K_UP:
                pressed_up = False


"""main loop"""
def main () :
    #which global variables the function is referencing
    global pressed_right
    global pressed_left
    global ressed_down
    global pressed_up
    
    global player
    global playerx
    global playery
    global player_faceleft
    global player_faceright
    global current_state
    
    pygame.init()
    
    game_running = False

    while game_running == False :
        pygame.init()
        
        """run key press detection"""
        pressed_keys(pygame)
        
        if pressed_left:
            go_left()
            #player = player_faceleft
        if pressed_right:
            go_right()
            #player = player_faceright
        if pressed_up:
            go_up()
        
        
        """main loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = True
                pygame.quit()
                quit()
            
            #closing game through escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('You hit escape')
                    print('That quits the game')
                    game_running = True
        
        #fill screen background
        screen.fill(white)
        
        #render player
        render_objects(pygame, screen)
        
        #detect collision
        PLatCol()
        BorderCol()
        
        #Calculate Gravity
        CalcGrav()
        
        #move the camera
        move_camera()
        
        #update screen
        pygame.display.flip()
        
        #update screen rate
        fpsClock.tick(FPS)
        
main()
