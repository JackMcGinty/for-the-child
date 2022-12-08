from Cards import Card

class Test_Card:
    """Class that will test all the functionality of the Card class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("Card:")
        self.card = Card((0,0,0))
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
        assert self.card.is_match(Card((0,0,0)))
    