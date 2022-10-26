



class Level:
    """Holds the attributes for the Level class including: current level..."""

    levels = {
        1:4,
        2:9,
        3:16,

    }

    current_level = 0

    def __init__(self):
        self.level = 0

    def get_level(self):
        """Returns the current level"""
        return self.level

    def get_next_level(self) -> int:
        """
        Inputs: None
        Progress to next level
        Outputs: 
        """
        self.current_level ++ 1
        num_cards = self.levels[self.current_level]
        return num_cards