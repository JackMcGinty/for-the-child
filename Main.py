import pygame
from Test import Test

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])

def main():
    Test()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pygame.display.update()

main()