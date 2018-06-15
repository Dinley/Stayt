#!/usr/local/bin/python3.5m

import pygame

pygame.init()

done = False


def pressed_keys() :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('you hit left')
            if event.key == pygame.K_RIGHT:
                print ('you hit right')
            if event.key == pygame.K_UP:
                print('you hit up')
            if event.key == pygame.K_DOWN:
                print('you hit down')
                
while done == False :
    pressed_keys()