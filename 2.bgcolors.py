import pygame
pygame.init()
WIDTH ,HEIGHT=900,500
colour=(123,34,213)#rgb values

screen=pygame.display.set_mode((WIDTH,HEIGHT)) #game window
pygame.display.set_caption("BACKGROUND COLORS") #name of window

run=True
while run:#main loop for running of game until pressed close
        
    for event in pygame.event.get():#for taking all the input inside of game
        if event.type==pygame.QUIT:
            run=False
        screen.fill(colour)
        pygame.display.update()
pygame.quit()
