import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

TENKIU = pygame.image.load(os.path.join(IMG_DIR, 'Other/laser.png'))

LOGO = pygame.image.load(os.path.join(IMG_DIR, 'Other/Logo.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
LASER = pygame.image.load(os.path.join(IMG_DIR, "Bullet/laser.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
MISSILE = pygame.image.load(os.path.join(IMG_DIR, "Enemy/missile.png"))
UFO_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ufo_boss.png"))
METEOR = pygame.image.load(os.path.join(IMG_DIR, "Enemy/meteor.png"))

FONT_STYLE = 'freesansbold.ttf'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_SPACESHIP_TYPE = 'ship'
BULLET_BOSS_TYPE = 'ufo_boss'

LEFT = 'left'
RIGHT = 'right'

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
PURPLE_COLOR = (128, 0, 128)
GREEN_COLOR = (0, 255, 0)
