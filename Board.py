"""
Brennon
"""

import pygame
pygame.init()


class Board:
    levels = {
        "level_1":4,
        "level_2":8,
        "level_3":16,

    }

    def Board():

        screen = pygame.display.set_mode([600,600])
        run = True 
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
            pygame.display.update()



        

