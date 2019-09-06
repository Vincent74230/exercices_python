import pygame
from pathlib import Path

pygame.init()
SCREEN_SIZE = (500,1000)
screen = pygame.display.set_mode(SCREEN_SIZE)

SPRITE_SIZE = 100
BASE_DIR = Path(__file__).resolve().parent
cube = str(BASE_DIR / 'cube.png')
imgcube = pygame.image.load(cube).convert_alpha()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    screen.blit(imgcube, (0, 0))
    pygame.display.update()

pygame.quit()