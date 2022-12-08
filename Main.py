import pygame
from Board import Board
from Test import Test



def main():
    Test()

    The_Board = Board()
    The_Board.show_main_menu()
    pygame.quit()

if __name__ == "__main__":
    main()