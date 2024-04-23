import time
import pygame
from main import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import font

class Litties(pygame.sprite.Sprite):
    def __init__(self):
        self.images = [pygame.image.load(f"resource/anim{i}.png") for i in range(3)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -150
        self.findow = False
        self.count = 0
        self.fl_cont = False


    def update_position(self, n):
        print(self.image.get_height())
        print(self.rect.centery)
        if n == 1 and self.rect.x > 0:
            self.rect.x -= 5
        elif n == 2 and self.rect.centerx < SCREEN_WIDTH - 100:
            self.rect.x += 5
        if n == 3 and self.rect.centery > 0:
            self.fl_cont = False
            self.rect.y -= 5
        if n == 4 and self.rect.centery + 500 < self.image.get_height():
            self.rect.y += 5
        elif self.rect.centery + 500 >= self.image.get_height():
            self.fl_cont = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def anim_lit(self, cont):
        self.count += 1
        print("Попытка")
        if self.count <= 2 and (abs(self.rect.centerx - (SCREEN_WIDTH // 2)) < 100 and self.fl_cont):
            print("выполняю")
            self.image = self.images[self.count]
        elif self.count > 2:
            time.sleep(3)
            cont.image = pygame.transform.scale(cont.images[1], (600, 600))
            cont.fl_activ = True
            return 0
        else:
            self.fl_cont = False
            self.count = 0
            self.findow = 0

class conteiner(pygame.sprite.Sprite):
    def __init__(self):
        self.images = [pygame.image.load("resource/don_none.png"), pygame.image.load("resource/don_full.png")]
        self.image = pygame.transform.scale(self.images[0], (600, 600))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 3 * 2.05
        self.fl_activ = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
