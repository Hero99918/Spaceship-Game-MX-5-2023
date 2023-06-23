import pygame, random
from game.utils.constants import METEOR, SCREEN_WIDTH, SCREEN_HEIGHT


class Meteorite():
    WIDTH = 30
    HEIGHT = 50
    Y_POS = 0
    SPEED = 8

    def __init__(self):
        self.image = METEOR
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        super().__init__()
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.rect.y = self.Y_POS
        self.is_alive = True

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        if self.rect.colliderect(player.rect):
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)