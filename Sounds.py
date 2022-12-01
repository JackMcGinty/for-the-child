'''
Brennon Laney
'''

from pygame import mixer


class sound:
    def __init__(self) -> None:

        mixer.init()
        self.FLIP = mixer.Sound("assets/flip.ogg")
        self.FLIPBACK = mixer.Sound("assets/flipback.ogg")
        self.BELL_ONE = mixer.Sound("assets/bell1.ogg")
        self.BELL_TWO = mixer.Sound("assets/bell2.ogg")
        self.SHUFFLE = mixer.Sound("assets/shuffle.ogg")
        self.NEXTLEVEL = mixer.Sound("assets/untitled.ogg")
        self.FAIL = mixer.Sound("assets/fail.ogg")
        # CHEER = mixer.Sound("assets/Cheer.wav")
        # CRYING = mixer.Sound("assets/crying")

    def play_back_ground_music(self):
        '''
        Input: self
        Functionality: Plays the background music using mixer
        Returns: Void
        '''
        mixer.music.load("assets/background.ogg")
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)

    def play_bell_when_first_card_clicked(self):
        '''
        This function plays the sound of cards shuffling 
        '''
        self.FLIP.play()
    
    def play_wildcard(self):
        '''
        This plays the sound of the first bell
        '''
        self.BELL_ONE.play()

    def next_level(self):
        '''
        This plays a sound when the next level happens
        '''
        self.NEXTLEVEL.play()

    def play_fail(self):
        '''
        This plays the sound of FAIL when the user makes a mistake
        '''
        self.FAIL.play()

    def play_flip_back(self):
        '''
        This plays the sound FLIPBACK when the cards flip 
        '''
        self.FLIPBACK.play()

    def play_bell_when_second_card_clicked(self):
        '''
        This plays the second bell
        '''
        self.BELL_TWO.play()

    def shuffle(self):
        '''
        This plays the SHUFFLE sound when the cards are being shuffled 
        '''
        self.SHUFFLE.play()