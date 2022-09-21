import sys
import pygame
from pygame.locals import *
WIDTH ,HEIGHT=1250,650
BG_COLOR=(255, 53, 184)

class gamestate:
    def __init__(self):
        self.screenid= 0
    
    def intro(self):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.screenid= 1
            App.screen.fill((255,0,0))
            pygame.display.update()
            
    def game(self):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            App.screen.fill(BG_COLOR)
            pygame.display.update()
    def scene_manager(self):
        if self.screenid == 0:
            self.intro()
        if self.screenid == 1:
            self.game()
class App:
    def __init__(self):#inialize pygame
            pygame.init()
            flags = RESIZABLE
            App.screen = pygame.display.set_mode((WIDTH,HEIGHT), flags)
            App.running = True
    def run(self):#main loop
        gs=gamestate()
        while App.running:
            gs.scene_manager()
            
        pygame.quit()
    
if __name__ == '__main__':
        App().run()