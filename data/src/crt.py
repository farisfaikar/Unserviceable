""" CRT class file """
import pygame
from random import randint


class CRT:
    """ CRT class """

    def __init__(self, tv_width, tv_height, screen):
        self.display_screen = screen
        self.tv_width = tv_width
        self.tv_height = tv_height
        self.tv = pygame.image.load('data/img/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (self.tv_width, self.tv_height))

    def create_crt_lines(self):
        """ Create CRT lines based on window dimensions """
        line_height = 4
        line_amount = int(self.tv_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (self.tv_width, y_pos))

    def draw(self):
        """ Draw CRT onto screen """
        self.tv.set_alpha(randint(60, 90))
        self.create_crt_lines()
        self.display_screen.blit(self.tv, (0, 0))
