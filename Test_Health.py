from Health import Health

class Test_Health:
    """Class that will test all the functionality of the Health class"""
    def __init__(self):
        print("------------------------------------------------------------")
        print("Health:")
        self.health = Health()
        print("Health INIT SETUP\t\tPASSED")
        self.test()
        
    def test(self):
        """Main Test Runner Function"""
        self.test_default()
        self.test_get_health()
        self.test_add_health()
        self.test_subtract_health()
        self.test_no_health()
    
    def test_default(self):
        """Tests default values of Health class"""
        assert self.health.health == 1
        print("\ttest_default\t\tPASSED")

    def test_get_health(self):
        """Tests get_health(): health == 1"""
        assert self.health.get_health() == 1 == self.health.health
        print("\ttest_get_health\t\tPASSED")

    def test_add_health(self):
        """Tests add_health(): health += 1"""
        self.health.add_health()
        assert self.health.health == 2
        # Reset health to default (1)
        self.health.health = 1
        print("\ttest_add_health\t\tPASSED")
        
    def test_subtract_health(self):
        """Tests subtract_health(): health == 0"""
        assert self.health.subtract_health() == 0 == self.health.health
        print("\ttest_subtract_health\tPASSED")

    def test_no_health(self):
        """Tests no_health(): health == 0 returns true"""
        # Set health to 0
        self.health.health = 0
        assert self.health.no_health() == True
        print("\ttest_no_health\t\tPASSED")
