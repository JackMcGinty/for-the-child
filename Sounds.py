'''
Brennon Laney
'''

from pygame import mixer
import random


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
        self.CHEER = mixer.Sound("assets/Cheer.ogg")
        self.CRYING = mixer.Sound("assets/crying.ogg")


        # These sounds are for the random sound list
        self.CONGRATULATIONS1 = mixer.Sound("assets/hurray1-converted.ogg")
        self.CONGRATULATIONS2 = mixer.Sound("assets/hurray2-converted.ogg")
        self.CONGRATULATIONS3 = mixer.Sound("assets/hurray3-converted.ogg")
        self.CONGRATULATIONS4 = mixer.Sound("assets/hurray4-converted.ogg")
        self.CONGRATULATIONS5 = mixer.Sound("assets/hurray5-converted.ogg")
        self.CONGRATULATIONS6 = mixer.Sound("assets/hurray6-converted.ogg")
        self.CONGRATULATIONS7 = mixer.Sound("assets/hurray7-converted.ogg")
        self.CONGRATULATIONS8 = mixer.Sound("assets/hurray8-converted.ogg")
        self.CONGRATULATIONS9 = mixer.Sound("assets/hurray9-converted.ogg")
        self.CONGRATULATIONS10 = mixer.Sound("assets/hurray10-converted.ogg")
        self.CONGRATULATIONS11 = mixer.Sound("assets/hurray11-converted.ogg")
        self.CONGRATULATIONS12 = mixer.Sound("assets/hurray12-converted.ogg")
        self.CONGRATULATIONS13 = mixer.Sound("assets/hurray13-converted.ogg")
        self.CONGRATULATIONS14 = mixer.Sound("assets/hurray14-converted.ogg")
        self.CONGRATULATIONS15 = mixer.Sound("assets/hurray15-converted.ogg")
        self.CONGRATULATIONS16 = mixer.Sound("assets/hurray16-converted.ogg")
        self.CONGRATULATIONS17 = mixer.Sound("assets/hurray17-converted.ogg")
        self.CONGRATULATIONS18 = mixer.Sound("assets/hurray18-converted.ogg")
        self.CONGRATULATIONS19 = mixer.Sound("assets/hurray19-converted.ogg")
        self.CONGRATULATIONS20 = mixer.Sound("assets/hurray20-converted.ogg")

        # This list is for the function ... that will randomly select a sound in this list
        self.random_positive_sounds = [
            self.CONGRATULATIONS1,
            self.CONGRATULATIONS2,
            self.CONGRATULATIONS3,
            self.CONGRATULATIONS4,
            self.CONGRATULATIONS5,
            self.CONGRATULATIONS6,
            self.CONGRATULATIONS7,
            self.CONGRATULATIONS8,
            self.CONGRATULATIONS9,
            self.CONGRATULATIONS10,
            self.CONGRATULATIONS11,
            self.CONGRATULATIONS12,
            self.CONGRATULATIONS13,
            self.CONGRATULATIONS14,
            self.CONGRATULATIONS15,
            self.CONGRATULATIONS16,
            self.CONGRATULATIONS17,
            self.CONGRATULATIONS18,
            self.CONGRATULATIONS19,
            self.CONGRATULATIONS20,
        ]

        self.WRONG1 = mixer.Sound("assets/wrong-converted.ogg")
        self.WRONG2 = mixer.Sound("assets/wrong2-converted.ogg")
        self.WRONG3 = mixer.Sound("assets/wrong3-converted.ogg")
        self.WRONG4 = mixer.Sound("assets/wrong4-converted.ogg")
        self.WRONG5 = mixer.Sound("assets/wrong5-converted.ogg")
        self.WRONG6 = mixer.Sound("assets/wrong6-converted.ogg")
        self.WRONG7 = mixer.Sound("assets/wrong7-converted.ogg")

        self.random_negative_sounds = [
            self.WRONG1,
            self.WRONG2,
            self.WRONG3,
            self.WRONG4, 
            self.WRONG5,
            self.WRONG6,
            self.WRONG7
        ]

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

    def play_crying(self):
        '''
        This will play a crying noise
        '''
        self.CRYING.play()

    def play_cheer(self):
        '''
        This will play a cheering noise
        '''
        self.CHEER.play()

    def play_random_positive_sound(self):
        '''
        This will select a random sound from the random_positive_sounds list and play it
        '''
        new_sound = random.choice(self.random_positive_sounds)
        new_sound.play()
    
    def play_random_negative_sound(self):
        '''
        Select a random negative sound and play it.
        '''
        new_sound = random.choice(self.random_negative_sounds)
        new_sound.play()