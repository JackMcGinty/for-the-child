import json

from Score import Score

class Test_Score:
    """Class that will test all the functionality of the Score class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("SCORE:")
        self.score = Score()
        print("SCORE INIT SETUP\t\tPASSED")
        self.test()
        
    def test(self):
        """Main Test Runner Function"""
        self.test_default()
        self.test_get_score()
        self.test_add_score()
    
    def test_default(self):
        """Tests default values of Score class"""
        assert self.score.score == 0
        assert self.score.high_score == self.score.get_high_score_file()
        print("\ttest_default\t\tPASSED")

    def test_get_score(self):
        """Tests get_score(): score == 0"""
        assert self.score.get_score() == 0 == self.score.score
        print("\ttest_get_score\t\tPASSED")

    def test_add_score(self):
        """Tests add_score(): score += 2"""
        self.score.add_score(1)
        assert self.score.score == 2
        # Reset score to 0
        self.score.score = 0
        print("\ttest_add_score\t\tPASSED")
