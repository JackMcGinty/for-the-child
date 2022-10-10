"""
Brennon
"""

import pygame
#pygame.init()


class Board:
    levels = {
        "level_1":4,
        "level_2":8,
        "level_3":16,

    }

    def DisplayBoard(self):
        pygame.init()

        WIDTH = 1000
        HEIGHT = 700

        screen = pygame.display.set_mode([WIDTH, HEIGHT])

        #screen = pygame.display.set_mode()
        run = True 
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
            pygame.display.update()



        

