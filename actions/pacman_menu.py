from actions.base import BaseActions


class PacmanMenuActions(BaseActions):
    def update(self, events):
        if self.app.main_menu.is_enabled():
            self.app.main_menu.update(events)

    def draw(self):
        self.app.surface.fill(self.app.COLOR_BACKGROUND)
        self.app.all_sprites.draw(self.app.surface)
        self.app.coins_sprites.draw(self.app.surface)
        if self.app.main_menu.is_enabled():
            self.app.main_menu.draw(self.app.surface)