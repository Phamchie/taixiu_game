import pygame
import random

pygame.init()

screen = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Sunwin 20')
background = pygame.image.load('sun_bg.png').convert_alpha()
tx = pygame.image.load('sum68.png').convert_alpha()

def draw_background():
    bg_casino = pygame.transform.scale(background, (750, 500))
    screen.blit(bg_casino, (0, 0))
def draw_bg():
    bg_tx = pygame.transform.scale(tx, (750, 500))
    screen.blit(bg_tx, (0, 0))

font = pygame.font.Font(None, 30)
text1 = font.render("", True, (0, 0, 0))
tk_rect = pygame.Rect(0,0,0,0)

clock = pygame.time.Clock()

selected_tai = False
selected_xiu = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font(None, 28)

session = True
while session:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            session = False
    draw_background()
    draw_bg()
    pos_1 = (10, 10, 10, 10)
    pygame.draw.rect(screen, (255, 255, 255), tk_rect)
    screen.blit(text1, pos_1)
    pygame.display.update()
    clock.tick(60)
