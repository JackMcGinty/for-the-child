from Cards import Card

class Test_Card:
    """Class that will test all the functionality of the Card class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("Card:")
        self.card = Card()
        print("CARD INIT SETUP\t\tPASSED")
        self.test()
        
    def test(self):
        """Main Test Runner Function"""
        self.test_default()

    def test_default(self):
        """Tests default values of Card class"""
        assert self.card.color
        print("\ttest_default\t\tPASSED")
    