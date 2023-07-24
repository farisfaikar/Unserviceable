""" Config file to store global variables """
import pygame

# Screen dimension
screen_width = 800
screen_height = 512

# Font
chary_font = 'data/font/charybdis.ttf'

# Default RBG colors
RED = pygame.Color("#ff0000")
GREEN = pygame.Color("#00ff00")
BLUE = pygame.Color("#0000ff")
BLACK = pygame.Color("#000000")
WHITE = pygame.Color("#ffffff")

# Ammo
ammo = 5
pouch_data = {  # This could be an object/class?
    1: {
        'slot_filled': False,
        'ammo': 0,
    }, 2: {
        'slot_filled': True,
        'ammo': 5,
    }, 3: {
        'slot_filled': True,
        'ammo': 5,
    }, 4: {
        'slot_filled': True,
        'ammo': 5,
    }
}
bullet_chambered = True
magazine_inserted = True
magazine_in_hand = True
firing_mode = ['safe', 'single', 'automatic']
firing_index = 0
