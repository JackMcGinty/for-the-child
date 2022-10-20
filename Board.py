"""
Brennon
"""

import pygame
from Cards import Card, generate_deck
from Level import *
#pygame.init()

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



    def DisplayBoard(self):
        pygame.init()


        screen = pygame.display.set_mode([WIDTH, HEIGHT])


        list_of_cards = generate_deck(4)

        #screen = pygame.display.set_mode()
        run = True 
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in list_of_cards:
                            if i.rect.collidepoint(event.pos):
                                print("true")
                    
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



        

