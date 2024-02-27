from typing import Optional

import pygame.display
import pygame.event
import pygame.time
from pygame_menu.examples import create_example_window

from actions.game import GameActions
from actions.pacman_menu import PacmanMenuActions
from actions.pause_manu import PauseMenuActions
from builders.game import GameBuilder
from builders.main_menu import MainMenuBuilder
from pacman import Pacman, show, white, green, Cultist


def show_go_screen(screen):
    victory_sf = pygame.Surface((screen.get_rect().width, screen.get_rect().height))
    victory_sf.fill((0, 0, 0))   # fill in black
    show(victory_sf, "YOU WIN!", 80, green, screen.get_rect().centerx - 170, screen.get_rect().centery - 140)
    show(victory_sf, "Press 'R' to try again and 'E' to exit", 55, white, 150, screen.get_rect().centery - 60)
    screen.blit(victory_sf, (0, 0))
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    done = True
                if event.key == pygame.K_r:
                    return 1
    exit(1)


class Application:
    COLOR_BACKGROUND = [0, 0, 0]
    POINTS = -1
    FPS = 60
    H_SIZE = 850  # Height of window size
    W_SIZE = 1250  # Width of window size
    LEVEL = 1
    BASE_LEVEL = 1

    def __init__(self):
        self.surface: Optional['pygame.Surface'] = create_example_window('Pacman',
                                                                         (Application.W_SIZE, Application.H_SIZE))
        self.main_menu = MainMenuBuilder.build()
        self.all_sprites, \
            self.coins_sprites, \
            self.level_sprites,\
            self.teleport_sprites, \
            self.columns_sprites, \
            self.list_centers = GameBuilder.build(level=Application.LEVEL)
        self.pacman = Pacman(self.list_centers)
        self.pacman_sprites = pygame.sprite.Group()
        self.pacman_sprites.add(self.pacman)

        self.cultist = Cultist(self.list_centers)
        self.cultist_sprites = pygame.sprite.Group()
        self.cultist_sprites.add(self.cultist)

        self.states = [
            GameActions(self),
            PacmanMenuActions(self),
            PauseMenuActions(self)
        ]

    def get_index(self):
        if not self.main_menu.is_enabled():
            return 0
        elif self.current_menu.is_enabled() and self.current_menu.get_title() == 'Pacman Menu':
            return 1
        else:
            return 2

    def main_loop(self):
        while True:
            self.current_menu = self.main_menu.get_current()

            events = pygame.event.get()
            self.states[self.get_index()].update(events)
            Application.LEVEL, isWin = self.states[self.get_index()].logic(Application.LEVEL)
            if isWin:
                isRestart = show_go_screen(self.surface)
                if isRestart:
                    self = Application()
                    self.pacman.on_move = False
                    Application.LEVEL = 1
                    Application.BASE_LEVEL = Application.LEVEL
                    self.POINTS = 0
                    self.pacman_sprites.empty()
                    self.pacman = Pacman(self.list_centers)
                    self.pacman.on_move = False
                    self.all_sprites, self.coins_sprites, self.level_sprites, self.teleport_sprites, self.columns_sprites, \
                        self.pacman.list_centers = GameBuilder.build(level=1)
                    self.pacman_sprites.add(self.pacman)
                    self.cultist = Cultist(self.pacman.list_centers)
                    self.cultist_sprites = pygame.sprite.Group()
                    self.cultist_sprites.add(self.cultist)
            if Application.LEVEL is None:
                Application.LEVEL = Application.BASE_LEVEL
            if Application.LEVEL != Application.BASE_LEVEL:
                Application.BASE_LEVEL = Application.LEVEL
                self.all_sprites, self.coins_sprites, self.level_sprites, self.teleport_sprites, self.columns_sprites, \
                    self.pacman.list_centers = GameBuilder.build(level=Application.LEVEL)
                self.pacman_sprites.add(self.pacman)
                self.cultist = Cultist(self.pacman.list_centers)
                self.cultist_sprites = pygame.sprite.Group()
                self.cultist_sprites.add(self.cultist)
            self.surface.fill(self.COLOR_BACKGROUND)
            self.states[self.get_index()].draw()
            if Application.LEVEL == 1 and self.POINTS == 75:
                show(self.surface, "PORTAL ACTIVE", 40, white, 900, 660)
            elif Application.LEVEL == 2 and self.POINTS >= 120:
                show(self.surface, "PORTAL ACTIVE", 40, white, 900, 660)
            elif Application.LEVEL == 3:
                show(self.surface, "NO PORTAL", 40, white, 950, 660)
            else:
                show(self.surface, "PORTAL INACTIVE", 40, white, 850, 660)
            show(self.surface, "PORTAL", 40, white, 10, 10)
            show(self.surface, "ENERGY: " + str(self.POINTS), 40, white, 10, 60)
            pygame.display.flip()

            pygame.time.wait(50)
