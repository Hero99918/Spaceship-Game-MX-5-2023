from game.components.enemies.ship import ship
from game.components.enemies.enemy2 import Enemy2

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy() and self.add_enemy2
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 4:
            self.enemies.append(ship())
            self.enemies.append(Enemy2())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def check_collision(rect1, rect2):
        return rect1.colliderect(rect2)
