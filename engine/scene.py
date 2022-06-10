class Scene:

    def __init__(self):
        self.actors = []

    def load(self):
        for actor in self.actors:
            actor.load()

    def render(self, surface):
        for actor in self.actors:
            actor.render(surface)

    # TO FIX: timing
    def update(self):
        for actor in self.actors:
            actor.update()

