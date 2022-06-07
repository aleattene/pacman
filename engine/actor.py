class Actor:

    def __init__(self):
        self.components = []

    def load(self):
        for component in self.components:
            component.load()

    def render(self):
        for component in self.components:
            component.render()

    # TO FIX: timing
    def update(self):
        for component in self.components:
            component.update()

