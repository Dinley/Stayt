#!/usr/local/bin/python3.5m

import pygame
#import window_creation
import key_presses

#import pygame

pygame.init() 

#window_creation.create_window()
#key_presses.pressed_keys()


def main () :
    
    pygame.init()
    
    # Screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    
    done = False

    #screen details
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Stayt")

    while done == False :
        pygame.init()
        
        key_presses.pressed_keys(pygame)
        
        
        
        #main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            #closing game through escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('You hit escape')
                    print('That quits the game')
                    done = True
                      
        #key_presses.pressed_keys()
        
main()

"""
#Screen creation
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    
    #screen details
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Stayt")
    
    done = False
    
    while done == False :
        
        #closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            #closing game through escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('You hit escape')
                    print('That quits the game')
                    done = True"""
