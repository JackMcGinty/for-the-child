import json

class Score:
    """Holds the current score and high score"""
    def __init__(self):
        """Initializes the score variables"""
        self.score = 0
        self.high_score = self.get_high_score_file()
    
    def add_score(self, level, combo = 0):
        """Adds points to total score"""
        if combo < 0:
            self.score += combo
        else:
            self.score += 2 * level + (combo * level)

    def get_score(self):
        """Returns the current score"""
        return self.score

    def update_high_score(self, file="high_score.json"):
        """Updates the high_score value in the json file"""
        if self.score > self.high_score:
            with open(file, "w") as file:
                high = { "high_score": self.score }
                json.dump(high, file)
        self.high_score = self.get_high_score_file()
                
    def get_high_score(self):
        """Returns the high score set at the beginning"""
        return self.high_score

    def reset_score(self):
        self.score = 0

    def get_high_score_file(self, file = "high_score.json"):
        """Returns the current high_score in the json file"""
        try:
            with open(file, 'r') as file:
                r = json.load(file)
                return r['high_score']
        except:
            with open(file, 'w') as file:
                high = { "high_score": 0 }
                json.dump(high, file)
                return 0
