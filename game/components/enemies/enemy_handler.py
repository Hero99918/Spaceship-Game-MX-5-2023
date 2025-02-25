import pygame
from game.components.enemies.ship import ship
from game.components.enemies.spider_ship import Enemy2

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.number_enemies_destroyed = 0

    def update(self, bullet_handler):
        self.add_enemy()
        self.add_enemy2()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destroyed:
                if isinstance(enemy, Enemy2):
                    self.number_enemies_destroyed += 3
                else:
                    self.number_enemies_destroyed += 1
            if not enemy.is_alive: #is_alive significa que esta visible
                self.remove_enemy(enemy)

    def add_enemy2(self):
        if len(self.enemies) < 2:
            new_enemy2 = Enemy2()
            overlapping = False
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(new_enemy2, enemy):
                    overlapping = True
                    break
            if not overlapping:
                self.enemies.append(new_enemy2)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 4:
            new_enemy = ship()
            overlapping = False
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(new_enemy, enemy):
                    overlapping = True
                    break
            
            if not overlapping:
                self.enemies.append(new_enemy)

            new_enemy2 = Enemy2()
            overlapping = False

            for enemy in self.enemies:
                if pygame.sprite.collide_rect(new_enemy2, enemy):
                    overlapping = True
                    break
            
            if not overlapping:
                self.enemies.append(new_enemy2)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    @staticmethod
    def check_collision(rect1, rect2):
        return rect1.colliderect(rect2)
    
    def reset(self):
        self.enemies =  []
        self.number_enemies_destroyed = 0
