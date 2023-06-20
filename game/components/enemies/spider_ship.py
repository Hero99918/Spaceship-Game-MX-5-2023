import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT

class Enemy2(Enemy):
    WIDTH = 40
    HEIGHT = 60
    X_POS_LIST = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    Y_POS = -3
    SPEED_X = 10
    SPEED_Y = 3
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 70
    SHOOTING_TIME = 15

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.move_x = random.choice(self.MOV_X)
        self.index = 0
        self.shooting_time = random.randint(0, self.SHOOTING_TIME)

    def update(self, bullet_handler):
        super().update(bullet_handler)
        self.index += 1
        if self.index >= self.INTERVAL:
            self.index = 0
            self.move_x = random.choice(self.MOV_X)
        
        if self.move_x == LEFT:
            self.rect.x -= self.speed_x
            if self.rect.x <= 0:
                self.move_x = RIGHT
        elif self.move_x == RIGHT:
            self.rect.x += self.speed_x
            if self.rect.x + self.WIDTH > SCREEN_WIDTH:
                self.rect.x = SCREEN_WIDTH - self.WIDTH
                self.move_x = LEFT

        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT:
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
