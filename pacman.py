import random

import pygame
import pygame.gfxdraw

# ============= Screen ===============
size = width, height = 1250, 620

# ============= Colors ===============
black = 0, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
red = 255, 0, 0
white = 255, 255, 255
brown = 77, 34, 14
green_army = 75, 83, 32

border_color = red
wall_color = brown
grass_color = green

N_cols = 20
N_rows = 19

gamezone_schemes = [
    ["         ^          ",
     "        / |         ",
     "       / _ |        ",
     "      / _ _ |       ",
     "     / _ _ ~ |      ",
     "    e _ _ . _ |     ",
     "   e ~ _ _ _ _ |    ",
     "  / _ _ _ _ _ _ |   ",
     " / _ _ _ _ _ _ _ |  ",
     "< _ _ _ _ _ ~ _ _ > ",
     " l _ _ _ _ _ * _ J  ",
     "  l _ _ _ _ _ _ J   ",
     "   t _ _ _ ! _ J    ",
     "    l _ ~ _ _ J     ",
     "     l _ _ _ J      ",
     "      l . _ J       ",
     "       t _ J        ",
     "        l J         ",
     "         V          "
     ],
    ["         ^          ",
     "        / |         ",
     "       e r |        ",
     "      / r _ |       ",
     "     e ! _ ~ |      ",
     "    e r _ ~ r |     ",
     "   e ~ _ c _ _ |    ",
     "  / _ c _ _ . r |   ",
     " e _ ~ * _ _ _ r |  ",
     "< _ _ _ _ _ ~ _ _ > ",
     " t _ c _ _ _ _ _ J  ",
     "  l _ _ . _ _ c J   ",
     "   l _ _ _ _ _ J    ",
     "    l _ ~ _ _ J     ",
     "     t _ _ c J      ",
     "      l _ _ J       ",
     "       t c J        ",
     "        l J         ",
     "         V          "
     ],
    ["         ^          ",
     "        e |         ",
     "       e c |        ",
     "      e c r |       ",
     "     e ~ ~ ~ |      ",
     "    e ~ r c r |     ",
     "   e ~ _ _ _ _ |    ",
     "  e r _ _ _ _ _ |   ",
     " / r ~ _ _ _ _ . |  ",
     "< _ ~ _ ~ ~ ~ _ _ > ",
     " t _ ~ _ r r ! _ J  ",
     "  t _ . _ _ _ _ J   ",
     "   t _ ~ ~ ~ _ J    ",
     "    l _ ~ _ _ J     ",
     "     l _ _ _ J      ",
     "      t c _ J       ",
     "       t r J        ",
     "        l J         ",
     "         V          "
     ]
]


class Pacman(pygame.sprite.Sprite):
    Pacman_size = ball_width, ball_height = 45, 45
    moveRight = False
    moveLeft = False
    moveUp = False
    moveDown = False
    path = 'images/heroSizeBase/glav-ger_N.png'
    on_move = False
    dest = ""
    on_move_target = []

    def __init__(self, list_centers):
        self.list_centers = list_centers
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, Pacman.Pacman_size)
        self.rect = self.image.get_rect()
        for i in range(N_rows):
            for j in range(N_cols):
                if list_centers[N_rows - i - 1][j][2] == 'floor':
                    self.rect.center = self.list_centers[N_rows - i - 1][j][0], self.list_centers[N_rows - i - 1][j][1]
                    self.cell_pos = {'x': j, 'y': N_rows - i - 1}
                    break

    def update(self):
        self.step(Pacman.moveLeft, Pacman.moveRight, Pacman.moveUp, Pacman.moveDown)

    def step(self, left, right, up, down):
        if self.on_move:
            if self.dest == "right":
                self.path = 'images/heroSizeBase/glav-ger_N.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Pacman.Pacman_size)
                if self.rect.center[0] < Pacman.on_move_target[0]:
                    self.rect.centerx += 8
                    self.rect.centery += 4
                else:
                    self.on_move = False
            elif self.dest == "left":
                self.path = 'images/heroSizeBase/glav-ger_S.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Pacman.Pacman_size)
                if self.rect.center[0] > Pacman.on_move_target[0]:
                    self.rect.centerx -= 8
                    self.rect.centery -= 4
                else:
                    self.on_move = False
            elif self.dest == "up":
                self.path = 'images/heroSizeBase/glav-ger_W.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Pacman.Pacman_size)
                if self.rect.center[1] > Pacman.on_move_target[1]:
                    self.rect.centery -= 4
                    self.rect.centerx += 8
                else:
                    self.on_move = False
            elif self.dest == "down":
                self.path = 'images/heroSizeBase/glav-ger_E.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Pacman.Pacman_size)
                if self.rect.center[1] + 4 < Pacman.on_move_target[1]:
                    self.rect.centery += 4
                    self.rect.centerx -= 8
                else:
                    self.on_move = False
        if left:
            if not self.on_move and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][2] != 'empty':
                self.on_move = True
                self.dest = "left"
                Pacman.on_move_target = [self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][0],
                                         self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][1]]
                self.cell_pos['x'] -= 1
                self.cell_pos['y'] -= 1
        elif right:
            if not self.on_move and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][2] != 'empty':
                self.on_move = True
                self.dest = "right"
                Pacman.on_move_target = [self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][0],
                                         self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][1]]
                self.cell_pos['x'] += 1
                self.cell_pos['y'] += 1
        elif up:
            if not self.on_move and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][2] != 'empty':
                self.on_move = True
                self.dest = "up"
                Pacman.on_move_target = [self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][0],
                                         self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][1]]

                self.cell_pos['y'] += 1
                self.cell_pos['x'] -= 1
        elif down:
            if not self.on_move and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][2] != 'empty':
                self.on_move = True
                self.dest = "down"
                Pacman.on_move_target = [self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][0],
                                         self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][1]]
                self.cell_pos['y'] -= 1
                self.cell_pos['x'] += 1


class Cultist(pygame.sprite.Sprite):
    Cultist_size = ball_width, ball_height = 45, 45
    path = 'images/cultistSizeBase/sectant_N.png'
    on_move = False
    dest = ""
    on_move_target = []
    last = [1, 4]

    def __init__(self, list_centers):
        self.list_centers = list_centers
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, Cultist.Cultist_size)
        self.rect = self.image.get_rect()
        for i in range(N_rows):
            for j in range(N_cols):
                if list_centers[N_rows - i - 1][j][3]:
                    self.rect.center = self.list_centers[N_rows - i - 1][j][0], self.list_centers[N_rows - i - 1][j][1]
                    self.cell_pos = {'x': j, 'y': N_rows - i - 1}

    def update(self):
        n = random.randint(1, 4)
        while n in self.last:
            n = random.randint(1, 4)
        if n == 1:
            self.last[0] = n
            self.step(True, False, False, False)
        elif n == 2:
            self.last[0] = n
            self.step(False, True, False, False)
        elif n == 3:
            self.last[1] = n
            self.step(False, False, True, False)
        else:
            self.last[1] = n
            self.step(False, False, False, True)

    def step(self, left, right, up, down):
        if Cultist.on_move:
            if Cultist.dest == "right":
                self.path = 'images/cultistSizeBase/sectant_N.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Cultist.Cultist_size)
                if self.rect.center[0] < Cultist.on_move_target[0]:
                    self.rect.centerx += 8
                    self.rect.centery += 4
                else:
                    Cultist.on_move = False
            elif Cultist.dest == "left":
                self.path = 'images/cultistSizeBase/sectant_S.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Cultist.Cultist_size)
                if self.rect.center[0] > Cultist.on_move_target[0]:
                    self.rect.centerx -= 8
                    self.rect.centery -= 4
                else:
                    Cultist.on_move = False
            elif Cultist.dest == "up":
                self.path = 'images/cultistSizeBase/sectant_W.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Cultist.Cultist_size)
                if self.rect.center[1] > Cultist.on_move_target[1]:
                    self.rect.centery -= 4
                    self.rect.centerx += 8
                else:
                    Cultist.on_move = False
            elif Cultist.dest == "down":
                self.path = 'images/cultistSizeBase/sectant_E.png'
                self.image = pygame.image.load(self.path)
                self.image = pygame.transform.scale(self.image, Cultist.Cultist_size)
                if self.rect.center[1] + 4 < Cultist.on_move_target[1]:
                    self.rect.centery += 4
                    self.rect.centerx -= 8
                else:
                    Cultist.on_move = False
        if left:
            if not Cultist.on_move and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][2] != 'empty':
                Cultist.on_move = True
                Cultist.dest = "left"
                Cultist.on_move_target = [self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][0],
                                          self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] - 1][1]]
                self.cell_pos['x'] -= 1
                self.cell_pos['y'] -= 1
        elif right:
            if not Cultist.on_move and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][2] != 'empty':
                Cultist.on_move = True
                Cultist.dest = "right"
                Cultist.on_move_target = [self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][0],
                                          self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] + 1][1]]
                self.cell_pos['x'] += 1
                self.cell_pos['y'] += 1
        elif up:
            if not Cultist.on_move and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][2] != 'empty':
                Cultist.on_move = True
                Cultist.dest = "up"
                Cultist.on_move_target = [self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][0],
                                          self.list_centers[self.cell_pos['y'] + 1][self.cell_pos['x'] - 1][1]]

                self.cell_pos['y'] += 1
                self.cell_pos['x'] -= 1
        elif down:
            if not Cultist.on_move and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][2] != 'wall' \
                    and self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][2] != 'empty':
                Cultist.on_move = True
                Cultist.dest = "down"
                Cultist.on_move_target = [self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][0],
                                          self.list_centers[self.cell_pos['y'] - 1][self.cell_pos['x'] + 1][1]]
                self.cell_pos['y'] -= 1
                self.cell_pos['x'] += 1


class Tile(pygame.sprite.Sprite):
    floor_size = W, H = 126, 156
    path = ''

    def __init__(self, x, y, path):
        pygame.sprite.Sprite.__init__(self)
        self.path = path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, Tile.floor_size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


class Coin(pygame.sprite.Sprite):
    coin_size = W, H = 25, 25
    path = 'images/elements/seed_N.png'

    def __init__(self, x, y):
        """
        :param color:
        :param status:;
        :param x: center
        :param y: center
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, Coin.coin_size)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.status = True


class LevelTeleport(pygame.sprite.Sprite):
    telep_size = W, H = 126, 156
    path = 'images/elements/portal.png'

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, Teleport.telep_size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


class Teleport(pygame.sprite.Sprite):
    telep_size = W, H = 126, 156
    path = 'images/elements/teleport.png'
    teleports_on_level = []
    cent = []

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, Teleport.telep_size)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.cent = [x + Tile.W / 2, y - Tile.W * 3 / 10]


def show(screen, data, font_size, color: tuple, pos_x, pos_y):
    font = pygame.font.SysFont("Comic Sans MS", font_size, True)
    ts = font.render(data, False, color)
    screen.blit(ts, (pos_x, pos_y))
