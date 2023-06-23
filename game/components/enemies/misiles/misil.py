import pygame, random
from game.utils.constants import MISSILE, SCREEN_WIDTH, SCREEN_HEIGHT


class Missile():
    WIDTH = 50
    HEIGHT = 30
    X_POS = 0
    Y_POS = SCREEN_HEIGHT - HEIGHT - 50
    SPEED = 10

    def __init__(self):
        self.image = MISSILE
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        super().__init__()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True

    def update(self, player):
        self.rect.x += self.SPEED
        if self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        if self.rect.colliderect(player.rect):
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)