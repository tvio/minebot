#udelat cas na release prisery
#alpha obrazky
#udelat priseru a postunovat ji k mine
#kolize miny s priserou
#zasobnik min
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
        #self.image = pygame.Surface([width,height])
        #self.image.fill(color)
        #pygame.draw.ellipse(self.image, color, [250, 250, width, height])
        self.image = pygame.image.load("minebot4.png").convert();
        self.image.set_colorkey(white);
        self.rect = self.image.get_rect()
        #pygame.draw.rect(self.image, red, [0, 0, width, height], 1)
       

class Prisera(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.center = [(random.randint(0,width)), (random.randint(0,height)) ]
        pygame.draw.circle(self.image, color,self.rect.center,10)   
    def autoPohyb():

        
class Mina(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mina1.png").convert();
        self.image.set_colorkey(white);
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
       
player = Player(blue,20,20)
#global player x,y synonym 
prisera = Prisera(red,15,15)
#playerList = pygame.sprite.Group()
#playerList.add(player)
priseryList = pygame.sprite.Group()
priseryList.add(prisera)

minyList = pygame.sprite.Group()


allSpritesList = pygame.sprite.Group()
allSpritesList.add(player)
allSpritesList.add(prisera)
while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mina = Mina()
            minyList.add(mina)
            allSpritesList.add(mina)

        #game code
        
        player.rect.center = pos[0],pos[1]



        """
        stret = pygame.sprite.spritecollide(player,priseryList,True)
        
        if stret:
            prisera = Prisera(red,15,15)
            priseryList.add(prisera)
            allSpritesList.add(prisera)
        """
        screen.fill(white)
        allSpritesList.draw(screen)
        
        
        pygame.display.update()
        clock.tick(60)