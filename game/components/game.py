import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, PURPLE_COLOR, LOGO, GREEN_COLOR
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.components.enemies.meteorite_handler import MeteoriteHandler
from game.components.enemies.misiles.misil_handler import MissileHandler
from game.utils import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.power_up_handler = PowerUpHandler()
        self.meteorite_handler = MeteoriteHandler()
        self.missile_handler = MissileHandler()
        self.number_death = 0
        self.score = 0
        self.max_score = 0
        self.num_attempts = 0
        self.menu_selection = 0
        self.game_over = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                if self.playing:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                else:
                    if event.key == pygame.K_UP:
                        self.menu_selection -= 1
                        if self.menu_selection < 0:
                            self.menu_selection = 2
                    elif event.key == pygame.K_DOWN:
                        self.menu_selection += 1
                        if self.menu_selection > 2:
                            self.menu_selection = 0
                    elif event.key == pygame.K_RETURN:
                        if self.menu_selection == 0:
                            self.playing = True
                            self.reset()
                        elif self.menu_selection == 1:
                            self.show_max_score()
                            pygame.time.delay(2000)
                        elif self.menu_selection == 2:
                            self.running = False

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            if self.player.is_alive:
                self.player.update(user_input, self.bullet_handler, self.meteorite_handler, self.missile_handler)
                if self.meteorite_handler.check_collision(self.player):
                    self.player.is_alive = False
                elif self.missile_handler.check_collision(self.player):
                    self.player.is_alive = False
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.power_up_handler.update(self.player)
            self.meteorite_handler.update(self.player)
            self.missile_handler.update(self.player)
            self.score = self.enemy_handler.number_enemies_destroyed
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_death += 1
                self.game_over = True
                self.max_score = max(self.max_score, self.score)
                self.num_attempts += 1

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.meteorite_handler.draw(self.screen)
            self.missile_handler.draw(self.screen)
            self.draw_score()
            self.draw_tip()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed


    WIDTH = 340
    HEIGHT = 300

    def draw_menu(self):
        options_menu = ['START', 'Max Score', 'Exit']
        color_menu = [WHITE_COLOR] * 3
        color_menu[self.menu_selection] = PURPLE_COLOR
        menu_image = LOGO
        menu_image = pygame.transform.scale(menu_image, (self.WIDTH, self.HEIGHT))
        menu_rect = menu_image.get_rect()
        menu_rect.center = (560, 160)
        self.screen.blit(menu_image, menu_rect)

        for index, option in enumerate(options_menu):
            text, text_rect = text_utils.get_message(option, 30, color_menu[index], height=SCREEN_HEIGHT//1.3 - 100 + index * 40)
            self.screen.blit(text, text_rect)
        if self.game_over:
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, PURPLE_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 200)
            self.screen.blit(score, score_rect)
            attempts, attempts_rect = text_utils.get_message(f'Attempts: {self.num_attempts}', 20, PURPLE_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 170)
            self.screen.blit(attempts, attempts_rect)

    def show_max_score(self):
        max_score_text = f"Max Score: {self.max_score}"
        text_surface, text_rect = text_utils.get_message(max_score_text, 30, GREEN_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_attempts(self):
        attempts, attempts_rect = text_utils.get_message(f'Attempts. {self.num_attempts}', 20, PURPLE_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.screen.blit(attempts, attempts_rect)

    def draw_tip(self):
        tip, tip_rect = text_utils.get_message(f'Kill as many as you can', 15, PURPLE_COLOR, 90, 40)
        self.screen.blit(tip, tip_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.meteorite_handler.reset()
        self.missile_handler.reset()








