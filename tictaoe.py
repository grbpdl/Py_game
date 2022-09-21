#game plan
'''
bg music
build setup package
create a intro scene with bg image where it shows game developed by and about game and on clicking button
how to play shows instruction
create a second scene where it asks user its name and also allows to select multiplayer or
against computer and also fav bg colour to pick
third scene is main game scene to play tic tac toe
sound effect for wrong move and winning
fourth scene for result and play again or quit option
'''

import sys
import pygame
from pygame.locals import *

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
                    
            App.screen.fill((0,0,255))
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
            App.screen = pygame.display.set_mode((640, 240), flags)
            App.running = True
    def run(self):#main loop
        gs=gamestate()
        while App.running:
            gs.scene_manager()
            
        pygame.quit()
    
if __name__ == '__main__':
        App().run()