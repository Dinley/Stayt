#!/usr/local/bin/python3.5m

import pygame
import key_presses
#import hi_there

pygame.init()

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
        
        #modules go here
        key_presses.pressed_keys(pygame)
        #hi_there.hell_yeah()
        
        
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
