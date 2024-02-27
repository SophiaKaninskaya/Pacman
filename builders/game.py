import pygame.sprite

from pacman import N_rows, N_cols, gamezone_schemes, Teleport, LevelTeleport, Coin, Tile


class GameBuilder:
    @staticmethod
    def build(level=1):
        list_centers = [[] for _ in range(N_rows)]
        Teleport.teleports_on_level = []
        gamezone_scheme = gamezone_schemes[level-1]
        all_sprites = pygame.sprite.Group()
        coins_sprites = pygame.sprite.Group()
        level_sprites = pygame.sprite.Group()
        teleport_sprites = pygame.sprite.Group()
        columns_sprites = pygame.sprite.Group()
        for i in range(N_rows):
            for j in range(N_cols):
                if gamezone_scheme[N_rows - i - 1][j] == '_':
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/floor.png'))
                    list_centers[N_rows - i - 1].append([Tile.W * 1/2 * (N_rows - i + 1/4),
                                                         Tile.W * 1/2 * (j + 3 - 3/5) - Tile.W * 1/2 * j / 2,
                                                         "floor", False])
                    coins_sprites.add(Coin(Tile.W * 1/2 * (N_rows - i + 1/4),
                                           Tile.W * 1/2 * (j + 3 - 3/5) - Tile.W * 1/2 * j / 2))
                elif gamezone_scheme[N_rows - i - 1][j] == '/':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/left.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == 'e':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/left-eyes.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == '~':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2,
                                                         "floor", False])
                    coins_sprites.add(Coin(Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                           Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2))
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/floor-water.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == 'l':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/top.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == 't':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/top-tent.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == '<':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3/5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    all_sprites.add(Tile(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2, 'images/elements/left-top.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == '.':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2,
                                                         "telep", False])
                    teleport = Teleport(Tile.W * 1/2 * (N_rows - i - 3/4), Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2)
                    Teleport.teleports_on_level.append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                        Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2,
                                                        j, N_rows - i - 1])
                    teleport_sprites.add(teleport)
                elif gamezone_scheme[N_rows - i - 1][j] == '*':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2,
                                                         "telep", False])
                    teleport = LevelTeleport(Tile.W * 1/2 * (N_rows - i - 3/4),
                                             Tile.W * 1/2 * (j + 3) - Tile.W * 1/2 * j / 2)
                    level_sprites.add(teleport)
                elif gamezone_scheme[N_rows - i - 1][j] == 'c':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    columns_sprites.add(
                        Tile(Tile.W * 1 / 2 * (N_rows - i - 3 / 4), Tile.W * 1 / 2 * (j + 3) - Tile.W * 1 / 2 * j / 2,
                             'images/elements/columns.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == 'r':
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2,
                                                         "wall", False])
                    columns_sprites.add(
                        Tile(Tile.W * 1 / 2 * (N_rows - i - 3 / 4), Tile.W * 1 / 2 * (j + 3) - Tile.W * 1 / 2 * j / 2,
                             'images/elements/trash.png'))
                elif gamezone_scheme[N_rows - i - 1][j] == '!':
                    all_sprites.add(
                        Tile(Tile.W * 1 / 2 * (N_rows - i - 3 / 4), Tile.W * 1 / 2 * (j + 3) - Tile.W * 1 / 2 * j / 2,
                             'images/elements/floor.png'))
                    list_centers[N_rows - i - 1].append([Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                                         Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2,
                                                         "floor", True])
                    coins_sprites.add(Coin(Tile.W * 1 / 2 * (N_rows - i + 1 / 4),
                                           Tile.W * 1 / 2 * (j + 3 - 3 / 5) - Tile.W * 1 / 2 * j / 2))
                else:
                    list_centers[N_rows - i - 1].append([0, 0, "empty", False])
        return all_sprites, coins_sprites, level_sprites, teleport_sprites, columns_sprites, list_centers
