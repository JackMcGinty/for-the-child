import json
import HighScore_Cloud
class Score:
    """Holds the current score and high score"""
    def __init__(self):
        """Initializes the score variables"""
        self.score = 0
        self.high_score = self.get_high_score()
        # Bryan Edit: cloud database
        self.connection = HighScore_Cloud.DatabaseConnection()
    
    def add_score(self, number):
        """Adds points to total score"""
        self.score += 2 ** number

    def get_score(self):
        """Returns the current score"""
        return self.score

    def update_high_score(self, file="high_score.json"):
        """Updates the high_score value in the json file"""
        if self.score > self.high_score:
            with open(file, "w") as file:
                high = { "high_score": self.score }
                json.dump(high, file)
        # Bryan Edit: pushes high score to cloud database
        if self.score > self.connection.pull_highscore():
            self.connection.push_highscore(self.score)

    def get_high_score(self, file="high_score.json"):
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
