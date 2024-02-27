class BaseActions:
    def __init__(self, app):
        self.app = app

    def update(self, events):
        pass

    def logic(self, level):
        return level, 0

    def draw(self):
        pass