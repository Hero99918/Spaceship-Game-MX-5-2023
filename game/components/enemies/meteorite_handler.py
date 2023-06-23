from game.components.enemies.meteorite import Meteorite


class MeteoriteHandler():
    def __init__(self):
        self.meteorites = []

    def update(self, player):
        self.add_meteorite()
        meteorite_to_remove = []

        for meteorite in self.meteorites:
            meteorite.update(player)
            if meteorite.rect.colliderect(player.rect):
                player.is_alive = False
                meteorite_to_remove.append(meteorite)
        for meteorite in meteorite_to_remove:
            self.remove_meteorite(meteorite)

        self.meteorites = [meteorite for meteorite in self.meteorites if meteorite.is_alive]

    def draw(self, screen):
        for meteorite in self.meteorites:
            meteorite.draw(screen)

    def add_meteorite(self):
        if len(self.meteorites) < 3:
            self.meteorites.append(Meteorite())

    def remove_meteorite(self, meteorite):
        self.meteorites.remove(meteorite)

    def check_collision(self, rect):
        for meteorite in self.meteorites:
            if meteorite.rect.colliderect(rect):
                return True
        return False

    def reset(self):
        self.meteorites = []
