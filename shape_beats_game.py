import pygame as pg

import game_config
import game_config as config
from game_dialog import GameDialog
from game_objects.enemy import Enemy
from game_objects.shape import Cube


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, config.WINDOW_SIZE)
    return img


class ShapeBeatsGame():
    """Базовый класс для запуска игры"""

    def __init__(self):
        # Фон игры
        self.background = load_img("picture/background.png")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pg.time.Clock()

        # Создаем объект класса GameDialog
        self.__game_dialog = GameDialog()

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Создаем объект основного окна
        self.screen = pg.display.set_mode(game_config.WINDOW_SIZE)
        pg.display.set_caption("Shapes & Beats")

        # Список всех спрайтов (графических объектов)
        self.all_sprites = pg.sprite.Group()

        # Объект игрока
        self.playerCube = Cube(self.screen)
        self.all_sprites.add(self.playerCube)

        self.enemy_list = pg.sprite.Group()
        self.count_enemy = 2

        for i in range(self.count_enemy):
            # Объект противника
            enemy = Enemy(self.screen, self.playerCube.rect.centerx, self.playerCube.rect.centery)
            self.enemy_list.add(enemy)
            self.all_sprites.add(enemy)

    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        # Обновляем экран
        pg.display.update()
        pg.display.flip()
        self.__clock.tick(self.__FPS)

    def run_game(self, game_is_run):
        # Основной цикл игры
        while game_is_run:
            # Обрабатываем событие закрытия окна
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            # Отрисовываем всё
            self.__draw_scene()
