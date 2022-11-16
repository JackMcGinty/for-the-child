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
        self.test_card_is_match()

    def test_default(self):
        """Tests default values of Card class"""
        assert self.card.color
        assert self.card.rect
        assert self.card.surf
        print("\ttest_default\t\tPASSED")
        
    def test_card_is_match(self):
        """tests the is match function"""
        black = (0,0,0)
        assert self.card.is_match(black, black)
    