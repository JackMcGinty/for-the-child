'''
Brennon Laney
'''

from pygame import mixer


class sound:

    mixer.init()
    BACKGROUND_MUSIC = mixer.music.load("assets/background.wav")
    BELL_ONE = mixer.Sound("assets/bell1.wav")
    BELL_TWO = mixer.Sound("assets/bell2.wav")
    CHEER = mixer.Sound("assets/Cheer.wav")
    CRYING = mixer.Sound("assets/crying")

    def play_back_ground_music(self):
        '''
        Input: self
        Functionality: Plays the background music using mixer
        Returns: Void
        '''
        self.BACKGROUND_MUSIC.play()

    def play_bell_when_first_card_clicked(self):
        self.BELL_ONE.play()

    def play_bell_when_second_card_clicked(self):
        self.BELL_TWO.play()

    def play_cheering(self):
        self.CHEER.play()

    def play_crying(self):
        self.CRYING.play()