#!/usr/local/bin/python3.5m

import pygame
import Genmod
import random

FPS = 60 #frames per second setting

fpsClock = pygame.time.Clock()

pygame.init()


"""colors"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

"""screen dimensions"""
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

HALF_SCREEN_WIDTH = int(SCREEN_WIDTH / 2)
HALF_SCREEN_HEIGHT = int(SCREEN_HEIGHT / 2)


"""screen details"""
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stayt")


"""sprites and locations"""
gas_sprite = pygame.image.load('gas_sprite.png')
solid_sprite = pygame.image.load('solid_sprite.png')
liquid_sprite = pygame.image.load('liquid_sprite.png')
solidred = pygame.image.load('Solidred.png')

#location of sprite (middle of screen as of now)
playerx = HALF_SCREEN_WIDTH
playery = HALF_SCREEN_HEIGHT

#current_state = solid_sprite

player = solid_sprite

player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right

global level
level = Genmod.genlvl(3)



"""render objects"""
def render_objects(X, Y) : #,state)
    screen.blit(player, (playerx, playery))
    Genmod.buildlvl(level, screen, solidred)
    
    
    
    
    """movement options"""
pressed_right = False
pressed_left = False
pressed_down = False
pressed_up = False

def go_right() :
    #moves player right
    global playerx
    playerx += 25

def go_left() :
    #moves player left
    global playerx
    playerx -= 25 #speed at which the player moves

def go_up() :
    #moves player up
    global playery
    playery -= 25 #speed at which the player moves

def go_down() :
    #moves player up
    global playery
    playery += 25 #speed at which the player moves


"""key presses"""
def pressed_keys(pygame) :
    #which global variables the function is referencing
    global player
    global playerx
    global playery
    global current_state
    global player_faceleft
    global player_faceright
    
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
            #moving down (will turn into fastfall)
            if event.key == pygame.K_DOWN:
                print('you hit down')
                pressed_down = True
                #go_down()
            #changing state to solid
            if event.key == pygame.K_a:
                print('You changed to Solid')
                player = solid_sprite
                player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
                player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right
            #changing state to gas
            if event.key == pygame.K_s:
                print('You changed to Gas')
                player = gas_sprite
                player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
                player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right
            #changing state liquid
            if event.key == pygame.K_d:
                print('You changed to Liquid')
                player = liquid_sprite
                player_faceleft = pygame.transform.flip(player, True, False) #flips the sprite to face left
                player_faceright = pygame.transform.flip(player_faceleft, True, False) #flips the sprite to face right
            
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
            if event.key == pygame.K_DOWN:
                pressed_down = False


"""main loop"""
def main () :
    #which global variables the function is referencing
    global pressed_right
    global pressed_left
    global ressed_down
    global pressed_up
    
    global player
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
        if pressed_down:
            go_down()
        
        
        """main loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = True
            
            #closing game through escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('You hit escape')
                    print('That quits the game')
                    game_running = True
        
        
        #fill screen background
        screen.fill(WHITE)
        
        #render objects
        render_objects(pygame, screen)
        
        #update screen
        pygame.display.flip()
        
        #update screen rate
        fpsClock.tick(FPS)
        
main()
