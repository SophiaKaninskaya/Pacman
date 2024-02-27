from actions.base import BaseActions


class PauseMenuActions(BaseActions):
    def update(self, events):
        self.app.main_menu.update(events)

    def draw(self):
        self.app.surface.fill((40, 0, 40))
        if self.app.main_menu.is_enabled():
            self.app.main_menu.draw(self.app.surface)