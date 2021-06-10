from menu import first_menu
from game import *

pygame.init()
GAMEDISPLAYSURF = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))

first_menu(GAMEDISPLAYSURF, GAME_FPS, Game_FramePerSec, GAME_SCREEN_HEIGHT, GAME_SCREEN_WIDTH)


