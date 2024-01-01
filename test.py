#central xy?
# hide curosr
# colision s jinym sprite
# http://programarcadegames.com/index.php?chapter=introduction_to_sprites

import pygame
from sys import exit


black = (  0,   0,   0)
blue = (0,0,255)
white = (255, 255, 255)
red   = (255,   0,   0)
width = 800
height = 600 

pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])



player = Player(blue,20,20)
sprites = pygame.sprite.Group()
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
        pos = pygame.mouse.get_pos()
        player.rect.x = pos[0]
        player.rect.y = pos[1]
        screen.fill(white)
        sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)