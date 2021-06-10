import pygame
import pygame_menu
import os
import sys
import random
import menu
from pygame.locals import *

GAME_SCREEN_HEIGHT = 600
GAME_SCREEN_WIDTH = 400
GAME_SPEED = 5

GAME_FPS = 60
Game_FramePerSec = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        #path = os.path.abspath("enemy.png") 
        self.image = pygame.image.load("./img/enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, GAME_SCREEN_WIDTH-40), 0))     
 
      def move(self):
        self.rect.move_ip(0,GAME_SPEED)
            
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #path2 = os.path.abspath('./img/download.png') 
        self.image = pygame.image.load("./img/download.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center = (150, 500))
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-(GAME_SPEED), 0)
        if self.rect.right < GAME_SCREEN_WIDTH :        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(GAME_SPEED, 0)

def start_game(DISPLAYSURF, FPS, FramePerSec, SCREEN_HEIGHT, SCREEN_WIDTH):

    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    random_spawn_time = 1000

    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")

    P1 = Player()

    enemies = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)

    #INC_SPEED = pygame.USEREVENT + 1
    #pygame.time.set_timer(INC_SPEED, 1000)

    SPAWN_ENEMY = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_ENEMY, random_spawn_time)


    while True:     
        for event in pygame.event.get():
            if event.type == SPAWN_ENEMY:
                random_spawn_time = random.randint(400,1200)  #Possibly increase difficulty, increase speed or increase amount spawning
                #num_of_enemies = random.randint(1,3)
                num_of_enemies = 1
                enemy_list = [None] * num_of_enemies #Add variable difficulty? Either menu option or increase over time? Both?
                for new_enemy in enemy_list:
                    new_enemy = Enemy()
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)

            elif event.type == QUIT: #Add scoring (score based on how many cars passed)
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill(WHITE)

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
            check = 0
            list_of_enemies = enemies.sprites()
            for sprite in list_of_enemies:
                if (entity == sprite):
                    check = 1
                else:
                    check = 0

            if (entity.rect.bottom > SCREEN_HEIGHT):
                if (check == 1):
                    enemies.remove(entity)

                all_sprites.remove(entity)
                entity.kill()

    
        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            menu.last_menu(DISPLAYSURF, FPS, FramePerSec, SCREEN_HEIGHT, SCREEN_WIDTH)

        pygame.display.update()
        FramePerSec.tick(FPS)



