import pygame
from pygame.locals import *
pygame.init()
WIDTH ,HEIGHT=900,500
purple=(123,34,213)#rgb values
RED=(255,0,0)
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #game window
pygame.display.set_caption("Name of window") #name of window
img = pygame.image.load('E:\learn\pygame\yellow.jpg')#loading image
img.convert_alpha()
img=pygame.transform.scale(img,(WIDTH,HEIGHT))
rect = img.get_rect() #returns surface object from imagefile
run=True
moving=False
while run:#main loop for running of game until pressed close
        
    for event in pygame.event.get():#for taking all the input inside of game
        if event.type==pygame.QUIT:
            run=False
        if event.type == MOUSEBUTTONDOWN:#for moving image with mouse
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
        screen.fill((RED))
        
        screen.blit(img, rect)
        pygame.draw.rect(img, (0,255,0), rect, 1)
        pygame.display.update()
pygame.quit()