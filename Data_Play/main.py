import time
from pygame import font
import pygame
import sys
pygame.font.init()
timer = pygame.time.Clock()
SCREEN_WIDTH = int(input())
SCREEN_HEIGHT = int(input())
fonts = pygame.font.Font("resource/cheri.ttf", 30)
text = fonts.render("Так держать! Сейчас - спресуем в готовый продукт и готово!", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, 100)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
from classes import Litties, conteiner
player_sprites = pygame.sprite.Group()
manipulator = Litties()
cont = conteiner()
player_sprites.add(player_sprites)
pause = False
while True:
    block = pygame.transform.scale(pygame.image.load("resource/blocks.png"), (SCREEN_WIDTH, SCREEN_HEIGHT // 3 * 2))
    fon = pygame.transform.scale(pygame.image.load("resource/fon.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(fon, (0,0))
    screen.blit(block, (0,SCREEN_HEIGHT // 3 * 2.1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        manipulator.update_position(1)
    elif key[pygame.K_RIGHT]:
        manipulator.update_position(2)
    if key[pygame.K_UP]:
        manipulator.update_position(3)
    elif key[pygame.K_DOWN]:
        manipulator.update_position(4)
    if key[pygame.K_SPACE]:
        manipulator.findow = True
    if manipulator.findow:
        print("True")
        manipulator.anim_lit(cont)
    cont.draw(screen)
    manipulator.draw(screen)
    pygame.display.flip()
    if manipulator.findow:
        timer.tick(1)
    if cont.fl_activ or pause:
        print("Text")
        screen.blit(text, text_rect)
        pygame.display.flip()
        pause = True
    timer.tick(15)
