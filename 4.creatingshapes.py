import pygame
from pygame.locals import *
pygame.init()
WIDTH ,HEIGHT=900,500

screen=pygame.display.set_mode((WIDTH,HEIGHT)) #game window
pygame.display.set_caption("DRAWING SHAPES") #name of window
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
white=(255,255,255)
#defining a point to draw with mouse
start = (0, 0)
size = (0, 0)
drawing = False
run=True
while run:#main loop for running of game until pressed close
        
    for event in pygame.event.get():#for taking all the input inside of game
        if event.type==pygame.QUIT:
            run=False
        screen.fill(GREEN)
        pygame.draw.rect(screen, RED, (50, 100, 150, 200))#(surface,colour,(x-cordinate,y-cordinate,length,height),width)
        pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)#drawing rectangle
        pygame.draw.ellipse(screen, RED, (550, 20, 160, 100))#drawing ellipsce solid
        pygame.draw.ellipse(screen, RED, (725, 20, 160, 100),1)#drawing ellipsce outline
        pygame.draw.circle(screen,white, (80,80), 40, 0)#(Surface, color, center, radius, width)
        if event.type == MOUSEBUTTONDOWN:#drawing shape with mouse started
            start = event.pos
            size = 0, 0
            drawing = True
        elif event.type == MOUSEBUTTONUP:#mouse released
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
        elif event.type == MOUSEMOTION and drawing:#checking if we are in drawing mode while mouse is moving
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
        pygame.draw.rect(screen, RED, (start, size), 2)#after calculating size finally drawing only let us draw once
        pygame.display.update()

pygame.quit()
#we can also draw multiple shapes