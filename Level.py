class Level:
    """Holds the attributes for the Level class including: current level..."""
    def __init__(self):
        self.level = 0

    def get_level(self):
        """Returns the current level"""
        return self.level

    def next_level(self):
        """Progress to next level"""
        self.level += 1