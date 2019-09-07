import pygame
import settings as se
import shapes

pygame.init()

screen = pygame.display.set_mode(se.SCREEN_SIZE)

shape = shapes.shapes()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        #if event.type == pygame.KEYDOWN:
            #if event.type == pygame.K_UP:

    shape.display_shape(screen)
    pygame.display.update()

pygame.quit()