from game.components.enemies.misiles.misil import Missile


class MissileHandler():
    def __init__(self):
        self.missiles = []

    def update(self, player):
        self.add_missile()
        for missile in self.missiles:
            missile.update(player)
            if missile.rect.colliderect(player.rect):
                player.is_alive = False
        if not missile.is_alive:
            self.missiles = [missile for missile in self.missiles if missile.is_alive]

    def draw(self, screen):
        for missile in self.missiles:
            missile.draw(screen)

    def add_missile(self):
        if len(self.missiles) < 1:
            self.missiles.append(Missile())

    def remove_missile(self, missile):
        self.missiles.remove(missile)

    def check_collision(self, rect):
        for missile in self.missiles:
            if missile.rect.colliderect(rect):
                return True
        return False
    
    def reset(self):
        self.missiles = []
