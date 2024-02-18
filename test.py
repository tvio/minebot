#automove, aspon by se to melo hejbat nejakym smerem po nejaky cas
#alpha obrazky
#udelat priseru a postunovat ji k mine
#kolize miny s priserou
#zasobnik min
#central xy?
# predelat na image
# udelat miny a kolize na miny
#https://stackoverflow.com/questions/74070512/how-to-make-sprite-move-to-point-along-a-curve-in-pygame
# http://programarcadegames.com/index.php?chapter=introduction_to_sprites

import random
import pygame
import pygame.gfxdraw


black = (  0,   0,   0)
blue = (0,0,255)
white = (255, 255, 255)
red   = (255,   0,   0)
width = 800
height = 600
timeRespown = 10000

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
#kazdych  3sekund event
timeInterval =  3000
timerEvent =pygame.USEREVENT+1
pygame.time.set_timer(timerEvent,timeInterval)

ATOM_IMG = pygame.Surface((30, 30), pygame.SRCALPHA)
# draw.circle is not anti-aliased and looks rather ugly.
# pygame.draw.circle(ATOM_IMG, (0, 255, 0), (15, 15), 15)
# gfxdraw.aacircle looks a bit better.
pygame.gfxdraw.aacircle(ATOM_IMG, 15, 15, 14, (0, 255, 0))
pygame.gfxdraw.filled_circle(ATOM_IMG, 15, 15, 14, (0, 255, 0))

def bezier(p0, p1, p2, t):
    px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
    py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2   
    return px, py

class Atom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ATOM_IMG
        self.rect = self.image.get_rect(center=[(random.randint(0,width)), (random.randint(0,height)) ])
    def autoMove(self):
        self.rect.move_ip(random.randint(0, 999), random.randint(0, 999))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface([width,height])
        #self.image.fill(color)
        #pygame.draw.ellipse(self.image, color, [250, 250, width, height])
        self.image = pygame.image.load("minebot4.png").convert();
        self.image.set_colorkey(white);
        self.rect = self.image.get_rect()
        #pygame.draw.rect(self.image, red, [0, 0, width, height], 1)
       

class Prisera(pygame.sprite.Sprite):
    def __init__(self, color,radius):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.rect.center = [(random.randint(0,width)), (random.randint(0,height)) ]
        pygame.draw.circle(self.image, color,self.rect.center,radius)   
   

        
class Mina(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mina1.png").convert();
        self.image.set_colorkey(white);
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
       
player = Player()
prisera = Atom()
#global player x,y synonym 
playerList = pygame.sprite.Group()
playerList.add(player)
priseryList = pygame.sprite.Group()
minyList = pygame.sprite.Group()
allSpritesList = pygame.sprite.Group()
allSpritesList.add(player)
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
        if event.type == timerEvent:
            #prisera = Prisera (blue,10)
            prisera = Atom()
            priseryList.add(prisera)
            allSpritesList.add(prisera)
            

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
        prisera.autoMove()        
        pygame.display.update()
        clock.tick(60)