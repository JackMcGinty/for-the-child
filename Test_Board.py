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
        # self.test_default()
        pass

    
    # def test_default(self):
    #     """Tests default values of Board class"""
    #     assert self.board.level.levels[1] == 4
    #     assert self.board.level.levels[2] == 8
    #     assert self.board.level.levels[3] == 16
    #     assert self.board.level.levels[4] == 25
    #     print("\ttest_default\t\tPASSED")
    