import pygame
from pygame.locals import *
import time
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
RED=(255,0,0)
X = 800
Y = 400
color=(230,230,0)
# def make_button():
#     text = pygame.font.Font('freesansbold.ttf', 25).render('Next', True, (0,0,255),(255,165,0))
#     textRect = text.get_rect()
#     textRect.center = (500,200)
#     display_surface.blit(text, textRect)
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if textRect.collidepoint(event.pos):
#             pass
    
display_surface = pygame.display.set_mode((X, Y))
text = pygame.font.Font('freesansbold.ttf', 25).render('Next', True, (0,0,255),(255,165,0))
textRect = text.get_rect()
textRect.center = (500,200)
run=True
while run:#main loop for running of game until pressed close
        
    for event in pygame.event.get():#for taking all the input inside of game
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if textRect.collidepoint(event.pos):
                    color=(230,230,230)
        display_surface.fill(color)
    display_surface.blit(text, textRect)
    pygame.display.update()
pygame.quit()
