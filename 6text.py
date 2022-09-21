
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
EditAbleText='this text can be edited'
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
# create a text surface object,
# on which text is drawn on it.
text = font.render('Showing text', True, green, blue)
img = font.render(EditAbleText, True, green, blue)
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
textRect.center = (500,200)#position of text

rect = img.get_rect()#defining bounding rectangle 
rect.topleft = (20, 20)#position of text
cursor = Rect(rect.topright, (3, rect.height))#cursor rectangle
while True:
    display_surface.fill(white)
    # copying the text surface object
    # to the display surface object
    # at the  coordinate.
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(EditAbleText)>0:
                    EditAbleText = EditAbleText[:-1]
            else:
                EditAbleText += event.unicode
            img = font.render(EditAbleText, True, RED)
            rect.size=img.get_size()
            cursor.topleft = rect.topright
    display_surface.fill((123,123,123))
    display_surface.blit(text, textRect)
    display_surface.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(display_surface, RED, cursor)
    pygame.display.update()
    if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()