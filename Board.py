"""
Brennon
"""

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
        pygame.init()
        clock = pygame.time.Clock()


        screen = pygame.display.set_mode([WIDTH, HEIGHT])


        list_of_cards = generate_deck(16, (WIDTH, HEIGHT))

        cards_revealed = []
        cards_mismatched = []
        first_card = ""
        clicked_cntr = 0
        timer = 0
        timer_on = False

        #screen = pygame.display.set_mode()
        run = True 
        click_counter = 0 # for debug
        while run:
            clock.tick(60)

            if timer_on == True:
                if timer < 40:
                    timer = self.start_timer(timer)
                else:
                    timer = 0
                    cards_mismatched.clear()
                    first_card = ""
                    clicked_cntr = 0
                    timer_on = False
            
            else:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        run = False

                    # The timer allows the user to see what mismatched color they selected for a breif moment
                    # This is inside the event forloop so that you can exit the game while it's looping but it doesn't look great

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for card in list_of_cards:
                                if card.rect.collidepoint(event.pos):
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

                                            timer_on = True

                                    else:
                                        first_card = card
         
            # Draw cards
            for card in list_of_cards:
                if card == first_card or card in cards_revealed or card in cards_mismatched:
                    pygame.draw.rect(screen, card.color, card.rect)
                else:
                    screen.blit(card.surf, card.rect)

            pygame.display.flip()
                    # Initialing Color
            # color = (255,0,0)

            # Xfirst = 30
            # Yfirst = 30
            # Xsize = 60
            # Ysize = 80
            # Drawing Rectangle

            #     pygame.draw.rect(screen, color, pygame.Rect(Xfirst, Yfirst, Xsize, Ysize))
                
            #     Xfirst += 80
            #     # if i == 11 or i == 21 or i == 31:
            #     #     Yfirst += 100
            #     #     Xfirst = 30

                # if Xfirst % 830 == 0:
                #     Yfirst += 100
                #     Xfirst = 30
            pygame.display.update()



            

