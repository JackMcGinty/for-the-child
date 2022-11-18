"""
Brennon
"""

import time
import pygame
from Cards import Card, generate_deck
from Level import *
from Health import Health
from Sounds import sound
if not pygame.get_init():
    pygame.init()

WIDTH = 1000
HEIGHT = 700

class Board:
    font = pygame.font.SysFont('Arial', 40)
    health_txt = font.render("Health: ", True, (255,255,255))
    round_txt = font.render("Round:", True, (255,255,255))

    def __init__(self):
        self.level = Level()
        self.health = Health()

    def start_timer(self, timer):
        timer += 1
        return timer
    
    # def print_text(self, text, location):
    # """print text on the screen"""
    

    """ Bryan has messed around a bit in here """
    def DisplayBoard(self):
        while not self.health.no_health():
            
            pygame.init()
            pygame.display.set_caption("Memorize You Colors!")
            clock = pygame.time.Clock()
            fx = sound()
            fx.shuffle()

            card_amount = self.level.get_next_level()

            screen = pygame.display.set_mode([WIDTH, HEIGHT])


            list_of_cards = generate_deck(card_amount, (WIDTH, HEIGHT))

            cards_revealed = []
            cards_mismatched = []
            first_card = ""
            clicked_cntr = 0
            timer = 0
            timer_on = False

            #screen = pygame.display.set_mode()
            run = True
            start = True
            while run:
                if start:
                    for card in list_of_cards:
                        pygame.draw.rect(screen, card.color, card.rect, 0, 15)
                        pygame.display.update()
                    time.sleep(self.level.get_level())
                    fx.next_level()
                clock.tick(60)
                start = False

                health_num = self.font.render(str(self.health.get_health()), True, (255,255,255))
                round_num = self.font.render(str(self.level.get_level()), True, (255,255,255))

                if timer_on == True:
                    if timer < 60:
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
                                                    fx.play_bell_when_second_card_clicked()
                                                    cards_revealed.append(first_card)
                                                    cards_revealed.append(card)
                                                    self.health.add_health(1)
                                                    clicked_cntr = 0
                                                elif card.color == (0,0,0):
                                                    cards_revealed.append(card)
                                                    clicked_cntr = 1
                                                    fx.play_wildcard()

                                                else:
                                                    fx.play_flip_back()
                                                    cards_mismatched.append(first_card)
                                                    cards_mismatched.append(card)
                                                    self.health.lose_a_life()

                                                    timer_on = True

                                            else:
                                                if card.color == (0,0,0):
                                                    cards_revealed.append(card)
                                                    clicked_cntr = 0
                                                    fx.play_wildcard()
                                                else:
                                                    fx.play_bell_when_first_card_clicked()                                                    
                                                first_card = card
                                    if self.health.no_health():
                                        fx.play_fail()
                                        print("You lose")
                                        screen.fill((0,0,0))
                                        game_over = self.font.render("You Lose!", True, (255,0,0))
                                        screen.blit(game_over, (WIDTH/2 - 75, HEIGHT/2 - 50, 200, 200))
                                        pygame.display.update()
                                        time.sleep(3)
                                        
                                        # while True:
                                        #     choices = {"Y", "N"}
                                        #     choice = ""
                                        #     while choice not in choices:
                                        #         self.display_text("Would you like to play again? ")
                                        
                                        return
                                    
                                    if len(cards_revealed) == card_amount:
                                        timer_on = True

                screen.fill((0,0,0))
                # Draw cards
                for card in list_of_cards:
                    if card == first_card or card in cards_revealed or card in cards_mismatched:
                        pygame.draw.rect(screen, card.color, card.rect, 0, 15)
                    else:
                        pygame.draw.rect(screen, (255,255,255), card.rect, 0, 15)

                screen.blit(self.health_txt, (50, 655, 200, 200))
                screen.blit(self.round_txt, (600, 655, 200, 200))
                screen.blit(health_num, (200, 655, 200, 200))
                screen.blit(round_num, (800, 655, 200, 200))

                pygame.display.flip()

                pygame.display.update()

                if len(cards_revealed) == card_amount and not self.health.no_health():
                    start = True
                    self.health.add_health(self.level.get_level())
                    fx.shuffle()
                    time.sleep(1)
                    cards_revealed.clear()
                    card_amount = self.level.get_next_level()
                    screen.fill((0,0,0))
                    list_of_cards = generate_deck(card_amount, (WIDTH, HEIGHT))
                    