from Cards import *

class Test_Deck:
    """Class that will test all the functionality of the Card class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("Deck:")
        self.test()
        
    def test(self):
        """Main Test Runner Function"""
        self.test_generate_deck()
    
    def test_generate_deck(self):
        """tests the generate deck function"""
        deck = generate_deck(4, (1000, 700))
        assert len(deck) == 4
        deck_matches = {}
        
        for card in deck:
            if card.color not in deck_matches:
                deck_matches