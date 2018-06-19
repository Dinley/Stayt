#!/usr/local/bin/python3.5m

import pygame

pygame.init()

def create_window () :
    # Screen dimensions
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    
    done = False

    while done == False :
        pygame.init()
        
        #screen details
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Stayt")
        
        #closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            #closing game through escape key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('You hit escape')
                    print('That quits the game')
                    done = True
        
    return
