class Component:
    """This class acts as an interface"""

    def __init__(self):
        self.components = []

    def load(self):
        pass

    def render(self):
        pass

    # TO FIX: timing
    def update(self):
        pass
