"""
Brennon
"""

import time
import pygame
from Cards import Card, generate_deck
from Level import *
if not pygame.get_init():
    pygame.init()

WIDTH = 1000
HEIGHT = 700

class Board:
    def __init__(self):
        self.levels = {
            "level_1":4,
            "level_2":8,
            "level_3":16,

        }
        self.level = Level()

    def start_timer(self, timer):
        timer += 1
        return timer

    """ Bryan has messed around a bit in here """
    def DisplayBoard(self):
        while self.level.get_level() < 4:
                
            pygame.init()
            clock = pygame.time.Clock()


            card_amount = self.level.get_next_level()

            screen = pygame.display.set_mode([WIDTH, HEIGHT])


            list_of_cards = generate_deck(card_amount, (WIDTH, HEIGHT))

            cards_revealed = []
            cards_mismatched = []
            first_card = ""
            clicked_cntr = 0
            timer = 0
            timer_on = False
            win = False

            #screen = pygame.display.set_mode()
            run = True 
            click_counter = 0 # for debug
            while run:
                clock.tick(60)
                if timer_on == True:
                    if timer < 60:
                        timer = self.start_timer(timer)
                    else:
                        timer = 0
                        cards_mismatched.clear()
                        first_card = ""
                        clicked_cntr = 0
                        timer_on = False
                        if win == True:
                            print("you win")
                            return
                
                else:
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            return

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for card in list_of_cards:
                                    if card.rect.collidepoint(event.pos):
                                        if card not in cards_revealed:
                                            clicked_cntr += 1
                                            if clicked_cntr >= 2:
                                                if first_card == card:
                                                    pass
                                                elif first_card.is_match(card):
                                                    cards_revealed.append(first_card)
                                                    cards_revealed.append(card)
                                                    clicked_cntr = 0
                                                else:
                                                    cards_mismatched.append(first_card)
                                                    cards_mismatched.append(card)
                                                    if first_card.color == (0,0,0):
                                                        cards_revealed.append(first_card)
                                                    if card.color == (0,0,0):
                                                        cards_revealed.append(card)

                                                    timer_on = True

                                            else:
                                                first_card = card
                                    print(len(cards_revealed), card_amount)
                                    if len(cards_revealed) == card_amount:
                                        timer_on = True
                                        if self.level.get_level() > 3:
                                            win = True
                # Draw cards
                for card in list_of_cards:
                    if card == first_card or card in cards_revealed or card in cards_mismatched:
                        pygame.draw.rect(screen, card.color, card.rect)
                    else:
                        screen.blit(card.surf, card.rect)

                pygame.display.flip()

                pygame.display.update()

                if len(cards_revealed) == card_amount:
                    time.sleep(1)
                    cards_revealed.clear()
                    card_amount = self.level.get_next_level()
                    screen.fill((0,0,0))
                    list_of_cards = generate_deck(card_amount, (WIDTH, HEIGHT))



            

