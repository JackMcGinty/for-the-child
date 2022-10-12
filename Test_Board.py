from Board import Board

class Test_Board:
    """Class that will test all the functionality of the Board class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("BOARD:")
        self.board = Board()
        print("BOARD INIT SETUP\t\tPASSED")
        self.test()
        
    def test(self):
        """Main Test Runner Function"""
        self.test_default()

    
    def test_default(self):
        """Tests default values of Board class"""
        assert len(self.board.levels) == 3
        assert self.board.levels["level_1"] == 4
        assert self.board.levels["level_2"] == 8
        assert self.board.levels["level_3"] == 16
        print("\ttest_default\t\tPASSED")
    