
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
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
NAME=''
EMAIL=''
font = pygame.font.Font('freesansbold.ttf', 32)
# create a text surface object,
# on which text is drawn on it.
img = font.render(NAME, True, green, blue)
img1 = font.render(EMAIL, True, green, blue)
# create a rectangular object for the


rect = img.get_rect()#defining bounding rectangle 
rect.topleft = (20, 20)#position of text
cursor = Rect(rect.topright, (3, rect.height))#cursor rectangle
rect1 = img1.get_rect()#defining bounding rectangle 
rect1.topleft = (20, 20)#position of text
cursor = Rect(rect1.topright, (3, rect1.height))#cursor rectangle
while True:
    display_surface.fill(white)
    # copying the text surface object
    # to the display surface object
    # at the  coordinate.
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(NAME)>0:
                    NAME = NAME[:-1]
            else:
                NAME += event.unicode
            img = font.render(NAME, True, RED)
            rect.size=img.get_size()
            cursor.topleft = rect.topright
            
            if event.key == K_BACKSPACE:
                if len(EMAIL)>0:
                    EMAIL = EMAIL[:-1]
            else:
                EMAIL += event.unicode
            img = font.render(EMAIL, True, RED)
            rect1.size=img.get_size()
            cursor.topleft = rect1.topright
    display_surface.fill((123,123,123))
    display_surface.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(display_surface, RED, cursor)
    pygame.display.update()
    if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()