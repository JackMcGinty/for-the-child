from Test_Score import Test_Score

"""Class that will test all the functionality of the program"""
class Test:
    def __init__(self):
        '''initilize all test classes and run'''
        self.score = Test_Score()
        self.run()
        
    def run(self):
        '''Runs all the test classes for each class in the program'''
        self.score.test()
        print("All Tests passed")

test = Test()

test.run()