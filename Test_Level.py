from Level import Level

class Test_Level:
    """Class that will test all the functionality of the Level class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("LEVEL:")
        self.level = Level()
        print("LEVEL INIT SETUP\t\tPASSED")
        self.test()
        
    def test(self):
        """Main Test Runner Function"""
        self.test_default()
        self.test_get_level()
        self.test_add_level()
    
    def test_default(self):
        """Tests default values of Level class"""
        assert self.level.current_level == 0
        print("\ttest_default\t\tPASSED")

    def test_get_level(self):
        """Tests get_level(): level == 0"""
        assert self.level.get_level() == 0 == self.level.current_level
        print("\ttest_get_level\t\tPASSED")

    def test_add_level(self):
        """Tests next_level(): level += 1"""
        self.level.add_level()
        assert self.level.current_level == 1
        # Reset level to 0
        self.level.level = 0
        print("\ttest_next_level\t\tPASSED")
