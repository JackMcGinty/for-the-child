import pygame
from Board import Board
from Test import Test

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode([WIDTH, HEIGHT])

def main():
    Test()

    The_Board = Board()
    The_Board.Board()




if __name__ == "__main__":
    main()