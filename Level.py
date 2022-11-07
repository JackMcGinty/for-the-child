class Level:
    """Holds the attributes for the Level class including: current level..."""

    levels = {
        1:4,
        2:9,
        3:16,
    }

    current_level = 1

    def __init__(self):
        self.current_level = 0

    def get_level(self):
        """Returns the current level"""
        return self.current_level

    def add_level(self):
        """adds a level"""
        self.current_level += 1

    def get_next_level(self) -> int:
        """
        Inputs: None
        Progress to next level
        Outputs: 
        """
        self.add_level()
        num_cards = self.levels[self.current_level]
        return num_cards