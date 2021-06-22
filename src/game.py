import pygame
import pygame_menu
import sys
import random
import high_score
import menu
import pygame.freetype
from pygame.locals import *
from pygame_menu.locals import *

GAME_SCREEN_HEIGHT = 600
GAME_SCREEN_WIDTH = 400
GAME_SPEED = 5

GAME_FPS = 60
Game_FramePerSec = pygame.time.Clock()

TotalScore = 0
first_time_check = 0

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, GAME_SCREEN_WIDTH-40), 0))     
 
      def move(self):
        self.rect.move_ip(0,GAME_SPEED)
            
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/download.png")
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

def score_draw(dispsurf, current_score):
    pygame.freetype.init()
    myfont = pygame.freetype.Font("./assets/Premier2019-rPv9.ttf", 24.0)
    textsurface = myfont.render("Score: "+str(current_score), (0, 0, 0))
    dispsurf.blit(textsurface[0], (0,0))
    pygame.display.flip()

def start_game(DISPLAYSURF, FPS, FramePerSec, SCREEN_HEIGHT, SCREEN_WIDTH, running_score):

    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    random_spawn_time = 1000

    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")

    running_score = 0

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

            elif event.type == QUIT: 
                pygame.quit() #Look at making executable standalone (py2exe)
                sys.exit()

        DISPLAYSURF.fill(WHITE)
        score_draw(DISPLAYSURF, running_score)

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()           
            if (entity.rect.bottom > SCREEN_HEIGHT):
                running_score+=1
                all_sprites.remove(entity)
                entity.kill()

    
        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            if (high_score.check_scores(running_score) == True):
                menu.high_score_menu(DISPLAYSURF, FPS, FramePerSec, SCREEN_HEIGHT, SCREEN_WIDTH, running_score, 0)
            else:
                menu.last_menu(DISPLAYSURF, FPS, FramePerSec, SCREEN_HEIGHT, SCREEN_WIDTH)

        pygame.display.update()
        FramePerSec.tick(FPS)



