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

                    # Initialing Color
            color = (255,0,0)
  
            Xfirst = 30
            Yfirst = 30
            Xsize = 60
            Ysize = 80
            # Drawing Rectangle
            for i in range(12):
                
                pygame.draw.rect(screen, color, pygame.Rect(Xfirst, Yfirst, Xsize, Ysize))

                Xfirst += 80      
            pygame.display.update()



        

