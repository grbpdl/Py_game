import pygame
from pygame.locals import *
import random

pygame.init()
WIDTH ,HEIGHT=900,500
purple=(123,34,213)#rgb values
RED=(255,0,0)
GREEN=(0,255,0)
bg=(0,0,0)
blue=(0,0,255)
white=(255,255,255)


screen=pygame.display.set_mode((WIDTH,HEIGHT)) #game window
pygame.display.set_caption("keys and mouse") #name of window

run=True
while run:#main loop for running of game until pressed close
        
    for event in pygame.event.get():#for taking all the input inside of game
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:#detecting keys pressed
            if event.key == pygame.K_r:
                bg = RED
            elif event.key == pygame.K_g:
                bg = GREEN
            elif event.key == pygame.K_p:
                bg = purple
        if event.type == MOUSEBUTTONDOWN:#detecting mouse click
            bg=blue
        if event.type == MOUSEBUTTONUP:
            bg=white
        if event.type == MOUSEMOTION:#detecting mouse motion
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            bg=(r,g,b)
        screen.fill(bg)
        pygame.display.update()
pygame.quit()
