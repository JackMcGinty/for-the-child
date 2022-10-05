import json

from Score import Score


"""Class that will test all the functionality of the Score class"""
class Test_Score:
    def __init__(self):
        print("\nSCORE INIT SETUP: ")
        self.score = Score()
        print("SCORE INIT SETUP PASSED")
        self.test()
        
    
    def test(self):
        """Main Test Runner Function"""
        print("\nSCORE TESTS: ")
        self.test_default()
        self.test_get_score()
        self.test_add_score()
        self.test_update_high_score()
        print("ALL SCORE TESTS PASSED")
    
    def test_default(self):
        """Tests default values of Score class"""
        assert self.score.score == 0
        assert self.score.high_score == 0
        print("test_default passed")

    def test_get_score(self):
        """Tests get_score(): score == 0"""
        assert self.score.get_score() == 0 == self.score.score
        print("test_get_score passed")

    def test_add_score(self):
        """Tests add_score(): score += 50"""
        self.score.add_score(50)
        assert self.score.score == 50
        # Reset score to 0
        self.score.score = 0
        print("test_add_score passed")

    def test_update_high_score(self):
        """Tests update_high_score(): high_score == 100 in json file"""
        self.score.add_score(100)
        file = "high_score_test.json"
        self.score.update_high_score(file)
        with open(file, 'r') as read:
            self.score.high_score = json.load(read)["high_score"]
        assert self.score.high_score == 100
        print("test_update_high_score passed")
