import pygame
from pygame.locals import *
pygame.init()
yellow=(123,123,123)
green=(123,123,123)
class Text:#defining text variables
        def __init__(self, text,pos):
                self.text = text
                self.pos = pos
                self.fontname = None
                self.fontsize = 72
                self.fontcolor = Color('black')
                self.set_font()
                self.render()

        def set_font(self):#Set the font from its name and size.
            self.font = pygame.font.Font(self.fontname, self.fontsize)


        def render(self):#Render the text into an image.
            self.img = self.font.render(self.text, True, self.fontcolor)
            self.rect = self.img.get_rect()
            self.rect.topleft = self.pos

        def draw(self):#Draw the text image to the screen.
            App.screen.blit(self.img, self.rect)
class App:
        def __init__(self):#inialize pygame
                pygame.init()
                flags = RESIZABLE
                App.screen = pygame.display.set_mode((640, 240), flags)
                App.t = Text('Pygame App',(20,20))
                App.running = True
        def run(self):#main loop
            while App.running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        App.running = False
                App.screen.fill((255,255,255))
                App.t.draw()
                pygame.display.update()
            pygame.quit()
if __name__ == '__main__':
        App().run()