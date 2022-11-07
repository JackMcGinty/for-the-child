import pygame
import random
import math
if not pygame.get_init():
    pygame.init()


# TODO 
#   Write card positioning code (use Board.py code as base)



"""
Bryan
"""

class Card:
    def __init__(self, color: tuple, card_size: tuple = (50, 100)):
        self.color = color
        self.rect = pygame.Rect(0, 0, card_size[0], card_size[1])
        self.surf = pygame.Surface(card_size)

    def is_match(self, other_card) -> bool:
        """ Check if we have a match. 
        Returns True if the argued card's value matches self's value,
        and returns False if it doesn't. """
        if self.color == other_card.color:
            return True
        else:
            return False
    
    def update_surf(self):
        """ Update our surface to reflect the size of our rect """
        self.surf = pygame.Surface((self.rect.width, self.rect.height))
        self.surf.fill((0xff, 0xff, 0xff)) # hex color codes

def generate_deck(size: int, screensize: tuple[2]) -> list:
    """ Generate a list of cards (i.e. a deck)
    of the argued size. if you argue an odd number,
    it rounds up to the next largest even number.
    Randomizes the deck with scramble_deck(), and
    then positions the deck wth position_deck(),
    which is what we need the screensize for. """
    if size <= 0:
        return list()
    new_deck = []
    for i in range(size // 2):
        new_card_color = generate_color()
        new_card_1 = Card(new_card_color)
        new_card_2 = Card(new_card_color)
        new_deck.append(new_card_1)
        new_deck.append(new_card_2)
    if size % 2 != 0:
        new_deck.append(Card((0, 0, 0)))
    suffled_deck = shuffle_deck(new_deck)
    placed_deck = position_deck(suffled_deck, screensize)
    return placed_deck

def shuffle_deck(deck: list) -> list:
    """ Shuffles a deck (i.e. mixes up the elements of a list)
    argued in the deck variable. """
    return_deck = []
    deck_length = len(deck)
    for number_of_cards in range(deck_length):
        chosen_card = random.choice(deck)
        deck.remove(chosen_card)
        return_deck.append(chosen_card)
    return return_deck
        
# Position (and resize) the cards on screen.

# [TODO] Cards on second and onward rows are offset more than the first.
#   Find out why.
#   Also screensize is not used but is hardcoded @ (1000, 700)
def position_deck(deck: list[Card], screensize: tuple[2]) -> list[Card]:

    # let's find the ideal card size
    ideal_cols = 0
    ideal_rows = 0
    ideal_cols = round(len(deck) ** (1/2))
    ideal_rows = ideal_cols
    x_padding = 10
    y_padding = 10
    card_width = (screensize[0] - (x_padding*(ideal_rows+1))) / ideal_rows
    card_height = (screensize[1] - (x_padding*(ideal_cols+1))) / ideal_cols
    i_x = 0
    i_y = 0
    column = 0
    for card in deck:
        card.rect.width = card_width
        card.rect.height = card_height
        card.rect.left = i_x + x_padding
        card.rect.top = i_y + y_padding
        i_x += (card.rect.width + x_padding)
        column += 1
        if column >= ideal_cols:
            i_x = 0
            i_y += (card.rect.height + y_padding)
            column = 0
        card.update_surf()
    return deck

def generate_color():
    """ Generates a random color in (rgb) format.
    Although it is technically possible for the 
    exact same color to be picked twice, the odds
    against this are extremely small and the 
    level would still be completable anyway, 
    since color is the means by which a match 
    is determined."""
    # to make sure we don't get black
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    return (r, g, b)