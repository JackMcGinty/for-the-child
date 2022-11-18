'''
Brennon Laney
'''

from pygame import mixer


class sound:

    mixer.init()
    BACKGROUND_MUSIC = mixer.music.load("assets/background.ogg")
    FLIP = mixer.Sound("assets/flip.ogg")
    FLIPBACK = mixer.Sound("assets/flipback.ogg")
    BELL_ONE = mixer.Sound("assets/bell1.ogg")
    BELL_TWO = mixer.Sound("assets/bell2.ogg")
    SHUFFLE = mixer.Sound("assets/shuffle.ogg")
    NEXTLEVEL = mixer.Sound("assets/untitled.ogg")
    FAIL = mixer.Sound("assets/fail.ogg")
    # CHEER = mixer.Sound("assets/Cheer.wav")
    # CRYING = mixer.Sound("assets/crying")

    def play_back_ground_music(self):
        '''
        Input: self
        Functionality: Plays the background music using mixer
        Returns: Void
        '''
        self.BACKGROUND_MUSIC.play()

    def play_bell_when_first_card_clicked(self):
        self.FLIP.play()
    
    def play_wildcard(self):
        self.BELL_ONE.play()

    def next_level(self):
        self.NEXTLEVEL.play()

    def play_fail(self):
        self.FAIL.play()

    def play_flip_back(self):
        self.FLIPBACK.play()

    def play_bell_when_second_card_clicked(self):
        self.BELL_TWO.play()

    def shuffle(self):
        self.SHUFFLE.play()

    def play_cheering(self):
        self.CHEER.play()

    def play_crying(self):
        self.CRYING.play()