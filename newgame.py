import pygame
from pygame.locals import *
pygame.init()
HEIGHT ,WIDTH=500,500
screen = pygame.display.set_mode((HEIGHT, WIDTH))
running = True

def main():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.update()
