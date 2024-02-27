import pygame_menu


class MainMenuBuilder:
    ABOUT = [
        f'pygame-menu {pygame_menu.__version__}',
        f'Author: Unified Cheese',
    ]
    HELP = [
        'Press ESC to enable/disable Menu',
        'Press ENTER to access a Sub-Menu or use an option',
        'Press UP/DOWN to move through Menu',
        'Press LEFT/RIGHT to move through Selectors'
    ]

    @staticmethod
    def build():
        pacman_menu = MainMenuBuilder.get_pacman_menu()
        help_menu = MainMenuBuilder.get_help_menu()
        about_menu = MainMenuBuilder.get_about_menu()
        main_menu = pygame_menu.Menu(
            enabled=False,
            height=400,
            theme=pygame_menu.themes.THEME_DARK,
            title='Main Menu',
            width=600
        )
        main_menu.add.button(pacman_menu.get_title(), pacman_menu)  # Add timer submenu
        main_menu.add.button(help_menu.get_title(), help_menu)  # Add help submenu
        main_menu.add.button(about_menu.get_title(), about_menu)  # Add about submenu
        main_menu.add.button('Exit', pygame_menu.events.EXIT)  # Add exit function
        return main_menu

    @staticmethod
    def get_about_menu():
        about_theme = pygame_menu.themes.THEME_DARK.copy()
        about_theme.widget_font = pygame_menu.font.FONT_NEVIS
        about_theme.title_font = pygame_menu.font.FONT_8BIT
        about_theme.title_offset = (5, -2)
        about_theme.widget_offset = (0, 0.14)
        about_menu = pygame_menu.Menu(
            center_content=False,
            height=400,
            mouse_visible=True,
            theme=about_theme,
            title='About',
            width=600
        )
        for m in MainMenuBuilder.ABOUT:
            about_menu.add.label(m, margin=(0, 0))
        about_menu.add.label('')
        about_menu.add.button('Return to Menu', pygame_menu.events.BACK)
        return about_menu

    @staticmethod
    def get_help_menu():
        help_theme = pygame_menu.Theme(
            background_color=(30, 50, 107, 190),  # 75% opacity
            title_background_color=(120, 45, 30, 190),
            title_font=pygame_menu.font.FONT_FRANCHISE,
            title_font_size=60,
            widget_font=pygame_menu.font.FONT_FRANCHISE,
            widget_font_color=(170, 170, 170),
            widget_font_shadow=True,
            widget_font_shadow_position=pygame_menu.locals.POSITION_SOUTHEAST,
            widget_font_size=45
        )
        help_menu = pygame_menu.Menu(
            height=600,  # Fullscreen
            theme=help_theme,
            title='Help',
            width=800
        )
        for m in MainMenuBuilder.HELP:
            help_menu.add.label(m, align=pygame_menu.locals.ALIGN_CENTER)
        help_menu.add.vertical_margin(25)
        help_menu.add.button('Return to Menu', pygame_menu.events.BACK)
        return help_menu

    @staticmethod
    def get_pacman_menu():
        pacman_theme = pygame_menu.themes.THEME_DARK.copy()  # Create a new copy
        pacman_theme.background_color = (0, 0, 0, 180)  # Enable transparency
        # Timer
        pacman_menu = pygame_menu.Menu(
            height=400,
            onclose=pygame_menu.events.RESET,
            theme=pacman_theme,
            title='Pacman Menu',
            width=600
        )

        # # Add widgets
        # pacman_menu.add.button('Reset timer', reset_timer)

        # Adds a selector (element that can handle functions)
        # pacman_menu.add.selector(
        #     title='Change color ',
        #     items=[
        #         ('Random', (-1, -1, -1)),  # Values of selector, call to change_color_bg
        #         ('Default', (128, 0, 128)),
        #         ('Black', (0, 0, 0)),
        #         ('Blue', (12, 12, 200))
        #     ],
        #     default=2,  # Optional parameter that sets default item of selector
        #     onchange=MainMenuBuilder.change_color_bg,  # Action when changing element with left/right
        #     onreturn=MainMenuBuilder.change_color_bg,  # Action when pressing return on an element
        #     All the following kwargs are passed to change_color_bg function
        # write_on_console=False
        # )

        pacman_menu.add.button('Return to Menu', pygame_menu.events.BACK)
        pacman_menu.add.button('Close Menu', pygame_menu.events.CLOSE)
        return pacman_menu

    # @staticmethod
    # def change_color_bg(value: Tuple, c: Optional[Tuple] = None, **kwargs) -> None:
    #     """
    #     Change background color.
    #
    #     :param value: Selected option (data, index)
    #     :param c: Color tuple
    #     :return: None
    #     """
    #     color, _ = value
    #     if c == (-1, -1, -1):  # If random color
    #         c = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    #     if kwargs['write_on_console']:
    #         print('New background color: {0} ({1},{2},{3})'.format(color[0], *c))
    #     COLOR_BACKGROUND[0] = c[0]
    #     COLOR_BACKGROUND[1] = c[1]
    #     COLOR_BACKGROUND[2] = c[2]
