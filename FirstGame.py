import pygame, sys, random, time
from pygame.locals import *
 
pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 400
SPEED = 5

FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-40), 0))     
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("download.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center = (150, 500))
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-(SPEED), 0)
        if self.rect.right < SCREEN_WIDTH :        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(SPEED, 0)   
 
         
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group() #Add multiple enemies with one spawn at a time at random times
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
while True:     
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2              
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()


    pygame.display.update()
    FramePerSec.tick(FPS)



