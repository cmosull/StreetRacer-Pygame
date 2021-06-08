import sys
import pygame
from pygame.locals import *

pygame.init()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

