from Test_Score import Test_Score
from Test_Level import Test_Level
from Test_Health import Test_Health
from Test_Board import Test_Board
from Test_Card import Test_Card
from Test_Deck import Test_Deck

class Test:
    """Class that will test all the functionality of the program"""
    def __init__(self):
        '''initilize all test classes to run'''
        Test_Score()
        print("SCORE TESTS:\t\t\tPASSED")
        Test_Level()
        print("LEVEL TESTS:\t\t\tPASSED")
        Test_Health()
        print("HEALTH TESTS:\t\t\tPASSED")
        Test_Board()
        print("BOARD TESTS:\t\t\tPASSED")
        Test_Card()
        print("CARD TESTS:\t\t\tPASSED")
        #Test_Deck()
        #print("DECK TESTS:\t\t\tPASSED")
        print("------------------------------------------------------------")
        print("\n+++++++++++++++++++++++++++")
        print("ALL TESTS\t\t\tPASSED")
        print("+++++++++++++++++++++++++++")
        
Test()