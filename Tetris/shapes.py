import settings
import pygame

class shapes:
    def __init__(self):
        self.position_shape_sprites = settings.BAR
        self.position_shape_pixel = []
        self.square = pygame.image.load(settings.CUBE).convert_alpha()
        self.X = 0
        self.Y = 0

    def display_shape(self,screen):
        

        x=0
        y=0
        for element in self.position_shape_sprites[0]:
            
            x = element[0] * settings.SPRITE_SIZE
            y = element[1] * settings.SPRITE_SIZE
            screen.blit(self.square,(x,y))