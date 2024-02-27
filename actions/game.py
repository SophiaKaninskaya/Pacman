import random

import pygame.sprite

from actions.base import BaseActions
from pacman import Pacman


def get_another_teleport(all_teleports: list, curr_teleport: list) -> tuple:
    index = -1
    for i in range(len(all_teleports)):
        if int(all_teleports[i][0]) == int(curr_teleport[0]) and \
                int(all_teleports[i][1]) == int(curr_teleport[1]):
            index = i
    if index == -1:
        exit(-1)
    other_teleports = all_teleports[:index] + all_teleports[index+1:]
    rand_num = random.randint(0, len(other_teleports)-1)
    new_teleport = other_teleports[rand_num]
    print("NEW_TELEPORT:", new_teleport)
    return tuple(new_teleport)


IS_TELEPORTED = False
new_teleport = (0, 0)


class GameActions(BaseActions):
    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.app.current_menu.get_title() == 'Main Menu':
                    self.app.main_menu.toggle()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Pacman.moveLeft = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Pacman.moveRight = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    Pacman.moveUp = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    Pacman.moveDown = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Pacman.moveLeft = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Pacman.moveRight = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    Pacman.moveUp = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    Pacman.moveDown = False

    def logic(self, level):
        collided_coins = pygame.sprite.spritecollide(self.app.pacman, self.app.coins_sprites, True, False)
        global POINTS
        self.app.POINTS += len(collided_coins)
        if self.app.POINTS >= 170:
            return level, 1
        collided_cultists = pygame.sprite.spritecollide(self.app.pacman, self.app.cultist_sprites, True, False)
        if len(collided_cultists):
            self.app.POINTS += 15
        collided_level_gates = pygame.sprite.spritecollide(self.app.pacman, self.app.level_sprites, False, False)
        if len(collided_level_gates):
            if level == 1 and self.app.POINTS == 75:
                level += 1
            elif self.app.POINTS >= 120:
                level += 1
        global IS_TELEPORTED
        global new_teleport

        # if self.app.pacman.rect.center != new_teleport[:2]:
        #     IS_TELEPORTED = False
        if (new_teleport[0] > self.app.pacman.rect.centerx or self.app.pacman.rect.centerx > new_teleport[0]
            or new_teleport[1] > self.app.pacman.rect.centery or
            self.app.pacman.rect.centery > new_teleport[1]) and not self.app.pacman.on_move:
            IS_TELEPORTED = False
        if not IS_TELEPORTED:
            collided_teleports = pygame.sprite.spritecollide(self.app.pacman, self.app.teleport_sprites, False, False)
            if len(collided_teleports):
                print("ALL:", collided_teleports[0].teleports_on_level)
                print("MY_POSITION:", collided_teleports[0].cent)
                IS_TELEPORTED = True
                new_teleport = get_another_teleport(collided_teleports[0].teleports_on_level,
                                                    collided_teleports[0].cent)
                self.app.pacman.rect.center = new_teleport[:2]
                Pacman.on_move_target = new_teleport[:2]
                self.app.pacman.cell_pos = {'x': new_teleport[2], 'y': new_teleport[3]}

        self.app.all_sprites.update()
        self.app.coins_sprites.update()
        self.app.pacman_sprites.update()
        self.app.cultist_sprites.update()
        return level, 0

    def draw(self):
        self.app.surface.fill(self.app.COLOR_BACKGROUND)
        self.app.all_sprites.draw(self.app.surface)
        self.app.coins_sprites.draw(self.app.surface)
        self.app.columns_sprites.draw(self.app.surface)
        self.app.teleport_sprites.draw(self.app.surface)
        self.app.level_sprites.draw(self.app.surface)
        self.app.cultist_sprites.draw(self.app.surface)
        self.app.pacman_sprites.draw(self.app.surface)
