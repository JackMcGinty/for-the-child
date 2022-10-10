class Health:
    def __init__(self):
        self.health = 1

    def get_health(self):
        '''gets the current health'''
        return self.health

    def add_health(self):
        '''adds one health point to the player'''
        self.health += 1
        return self.health

    def subtract_health(self):
        '''removes a health point from the player'''
        self.health -= 1
        return self.health

    def no_health(self):
        '''Gives True value if there is no more health remaining and player is dead.'''
        if self.health <= 0:
            return True