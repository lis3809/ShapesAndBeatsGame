# Класс ящик
import pygame as pg
import random
import math

import game_config


def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (50, 50))
    return img


class Enemy(pg.sprite.Sprite):
    def __init__(self, screen, player_x, player_y):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img("picture/enemy.png")
        self.rect = self.image.get_rect()

        self.respawn(player_x, player_y)

    def respawn(self, player_x, player_y):

        self.direction = random.choice(["left_up", "left_down", "right_up", "right_down"])
        if (self.direction == "left_up"):
            self.rect.centerx = game_config.WINDOW_SIZE[0]
            self.rect.centery = game_config.WINDOW_SIZE[1]

        elif (self.direction == "left_down"):
            self.rect.centerx = game_config.WINDOW_SIZE[0]
            self.rect.centery = 0

        elif (self.direction == "right_up"):
            self.rect.centerx = 0
            self.rect.centery = game_config.WINDOW_SIZE[0]

        else:
            # "right_down"
            self.rect.centerx = 0
            self.rect.centery = 0

        self.angle = math.atan2(player_y - self.rect.centery, player_x - self.rect.centerx)
        self.dx = game_config.speed * math.cos(self.angle)
        self.dy = game_config.speed * math.sin(self.angle)

    def move(self, player_x, player_y):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left > game_config.WINDOW_SIZE[0]:
            self.respawn(player_x, player_y)
        if self.rect.right < 0:
            self.respawn(player_x, player_y)

        if self.rect.top > game_config.WINDOW_SIZE[1]:
            self.respawn(player_x, player_y)
        if self.rect.bottom < 0:
            self.respawn(player_x, player_y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
