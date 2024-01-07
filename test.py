#central xy?
# predelat na image
# udelat miny a kolize na miny

# http://programarcadegames.com/index.php?chapter=introduction_to_sprites

import random
import pygame
from sys import exit


black = (  0,   0,   0)
blue = (0,0,255)
white = (255, 255, 255)
red   = (255,   0,   0)
width = 800
height = 600 

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, color, [250, 250, width, height])


class Prisera(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, color,[0,0,width,height])   
        self.rect.x = (random.randint(0,800))
        self.rect.y = (random.randint(0,600)) 
    
    

player = Player(blue,20,20)
prisera = Prisera(red,15,15)
#playerList = pygame.sprite.Group()
#playerList.add(player)
priseryList = pygame.sprite.Group()
priseryList.add(prisera)

allSpritesList = pygame.sprite.Group()
allSpritesList.add(player)
allSpritesList.add(prisera)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
        pos = pygame.mouse.get_pos()
        player.rect.x = pos[0]
        player.rect.y = pos[1]
        stret = pygame.sprite.spritecollide(player,priseryList,True)
        if stret:
            prisera = Prisera(red,15,15)
            priseryList.add(prisera)
            allSpritesList.add(prisera)

        screen.fill(white)
        allSpritesList.draw(screen)
        pygame.display.update()
        clock.tick(60)