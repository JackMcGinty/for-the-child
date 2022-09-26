import json

from Score import Score


class Test_Score:
    """Class that will test all the functionality of the Score class"""
    def __init__(self):
        self.passed = True
        self.score = Score()
    
    def test(self):
        """Main Test Runner Function"""
        self.test_default()
        self.test_get_score()
        self.test_add_score()
        self.test_update_high_score()
    
    def test_default(self):
        """Tests default values of Score class"""
        assert self.score.score == 0
        assert self.score.high_score == 0

    def test_get_score(self):
        """Tests get_score(): score == 0"""
        assert self.score.get_score() == 0 == self.score.score

    def test_add_score(self):
        """Tests add_score(): score += 50"""
        self.score.add_score(50)
        assert self.score.score == 50
        # Reset score to 0
        self.score.score = 0

    def test_update_high_score(self):
        """Tests update_high_score(): high_score == 100 in json file"""
        self.score.add_score(100)
        file = "high_score_test.json"
        self.score.update_high_score(file)
        with open(file, 'r') as read:
            self.score.high_score = json.load(read)["high_score"]
        assert self.score.high_score == 100


score = Test_Score()

Test_Score.test(score)
