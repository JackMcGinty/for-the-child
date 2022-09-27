"""
Bradley
"""
class Level:
    """Holds the attributes for the Level class including: current level..."""
    def __init__(self):
        """Initializes variables for the Level class"""
        self.level = 0
        # self.levels = {0:2, 1:4, 2:9, 3:16, 4:25}

    def get_level(self):
        """Returns the current level"""
        return self.level

    def next_level(self):
        """Progress to next level"""
        self.level += 1