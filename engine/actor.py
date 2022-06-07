class Actor:

    def __init__(self):
        self.components = []

    def load(self):
        for actor in self.components:
            actor.load()

    def render(self):
        for actor in self.components:
            actor.render()

    # TO FIX: timing
    def update(self):
        for actor in self.components:
            actor.update()

