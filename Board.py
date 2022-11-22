"""
Brennon
"""

import time
import pygame
from Cards import Card, generate_deck
from Level import *
from Health import Health
from Sounds import sound
from Score import Score
if not pygame.get_init():
    pygame.init()

WIDTH = 1000
HEIGHT = 700
font = pygame.font.SysFont('Arial', 40)

class Board:
    def __init__(self):
        self.level = Level()
        self.health = Health()
        self.score = Score()
        self.health_txt = ""
        self.score_txt = ""
        self.round_txt = ""
        self.game_over = font.render("You Lose!", True, (255,0,0))

    def start_timer(self, timer):
        timer += 1
        return timer

    def update_stats(self):
        
        self.health_txt = font.render(f"Health: {self.health.get_health()}", True, (255,255,255))
        self.score_txt = font.render(f"Score: {self.score.get_score()}", True, (255,255,255))
        self.round_txt = font.render(f"Round: {self.level.get_level()}", True, (255,255,255))
    
    # def print_text(self, text, location):
    # """print text on the screen"""
    

    """ Bryan has messed around a bit in here """
    def DisplayBoard(self):
        print(self.score.high_score)
        while not self.health.no_health():
            pygame.display.set_caption("Memorize You Colors!")
            clock = pygame.time.Clock()

            screen = pygame.display.set_mode([WIDTH, HEIGHT])

            def show_main_menu():
                title_font = pygame.font.SysFont("comicsans", 50)
                run = True
                while run:
                    title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
                    screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            screen.fill((0,0,0))
                            play_game()

            def play_game():
                pygame.display.update()
                fx = sound()
                fx.shuffle()
                fx.play_back_ground_music()
                card_amount = self.level.get_next_level()
                list_of_cards = generate_deck(card_amount, (WIDTH, HEIGHT))

                cards_revealed = []
                cards_mismatched = []
                first_card = ""
                clicked_cntr = 0
                timer = 0
                timer_on = False
                combo = 0

                #screen = pygame.display.set_mode()
                run = True
                start = True
                level = self.level.get_level()
                while run:
                    self.update_stats()
                    if start:
                        for card in list_of_cards:
                            pygame.draw.rect(screen, card.color, card.rect, 0, 15)
                            pygame.display.update()
                        time.sleep(level)
                        fx.next_level()
                    clock.tick(60)
                    start = False

                    # score = self.font.render(str(self.score.get_score()), True, (255,255,255))
                    # health_num = self.font.render(str(self.health.get_health()), True, (255,255,255))
                    # round_num = self.font.render(str(level), True, (255,255,255))

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
                                                        combo += 1
                                                        clicked_cntr = 0
                                                        self.score.add_score(combo)
                                                    elif card.color == (0,0,0):
                                                        cards_revealed.append(card)
                                                        clicked_cntr = 1
                                                        fx.play_wildcard()

                                                    else:
                                                        fx.play_flip_back()
                                                        cards_mismatched.append(first_card)
                                                        cards_mismatched.append(card)
                                                        self.health.lose_a_life()
                                                        combo = 0
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
                                            screen.blit(self.game_over, (WIDTH/2 - 75, HEIGHT/2 - 50, 200, 200))
                                            self.score.update_high_score()
                                            pygame.display.update()
                                            time.sleep(3)
                                            
                                            # while True:
                                            #     choices = {"Y", "N"}
                                            #     choice = ""
                                            #     while choice not in choices:
                                            #         self.display_text("Would you like to play again? ")
                                            
                                            # TODO: User continues to the next level after losing.
                                            return
                                        
                                        if len(cards_revealed) == card_amount:
                                            timer_on = True
                                print(combo)
                    screen.fill((0,0,0))
                    # Draw cards
                    for card in list_of_cards:
                        if card == first_card or card in cards_revealed or card in cards_mismatched:
                            pygame.draw.rect(screen, card.color, card.rect, 0, 15)
                        else:
                            pygame.draw.rect(screen, (255,255,255), card.rect, 0, 15)

                    screen.blit(self.health_txt, (50, 655, 200, 200))
                    screen.blit(self.round_txt, (400, 655, 200, 200))
                    screen.blit(self.score_txt, (800, 655, 200, 200))

                    pygame.display.flip()

                    pygame.display.update()

                    if len(cards_revealed) == card_amount and not self.health.no_health():
                        start = True
                        self.health.add_health(level)
                        fx.shuffle()
                        time.sleep(1)
                        cards_revealed.clear()
                        card_amount = self.level.get_next_level()
                        clr_rect = pygame.draw.rect(screen, (255,255,255), (0, 0, 1000, 625), 0, 0)
                        screen.fill((0,0,0), clr_rect)
                        list_of_cards = generate_deck(card_amount, (WIDTH, HEIGHT))
                        level = self.level.get_level()
            
            
            show_main_menu()