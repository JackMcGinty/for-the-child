import pygame

class User_Interface():
    def get_mouse_coord(self):
        (x, y) = pygame.mouse.get_pos()
        return x, y

    def get_click(self, rectangle):
        if pygame.mouse.get_pressed()[0] and rectangle.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False