"""
Unserviceable: The Game
"""
# import pygame
# import sys
# import math

# import data.src.config as cfg
# import data.src.crt as c

# # Initialize pygame
# pygame.init()

# # Initiate screen
# screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))

# pygame.display.set_caption("Unserviceable!")

# class Program:
#     """ Program class """

#     def __init__(self):
#         # Initiate instances
#         self.player = pygame.image.load('data/img/player.png')

#         self.font = pygame.font.Font(cfg.chary_font, 18)
#         self.controls = {
#             "r": "Remove/Load the magazine",
#             "f": "Rack the gun",
#             "t": "Check bullets in the magazine",
#             "g": "Check bullet in the chamber",
#             "v": "Select firing mode"
#         }

#     def run(self):
#         """ Runs methods every frame """
#         mouse_x, mouse_y = pygame.mouse.get_pos()

#         # Player drawing and rotation
#         player_rect = self.player.get_rect()
#         player_center_x, player_center_y = player_rect.center
        
#         angle_rad = math.atan2(player_center_y - mouse_x, player_center_x - mouse_y)
#         angle_deg = -math.degrees(angle_rad)

#         player_copy = pygame.transform.rotate(self.player, angle_deg + 90)
        
#         pygame.draw.rect(screen, cfg.GREEN, player_rect)
#         screen.blit(player_copy, player_copy.get_rect())

#         # Controls
#         control_rect_height = self.font.get_height() + 10
#         control_rect = pygame.Rect(0, screen.get_height()-control_rect_height, screen.get_width(), control_rect_height)
#         pygame.draw.rect(screen, "MidnightBlue", control_rect)

#         previous_width = 5
#         for control in self.controls:
#             render = self.font.render(control+": "+self.controls.get(control), True, "Whitesmoke", "MidnightBlue")
#             screen.blit(render, (0+previous_width, control_rect.y+5))

#             previous_width += render.get_width() + 20

        

#     def process_fire(self):
#         if cfg.firing_mode[cfg.firing_index] == 'safe':
#             print('The trigger is stuck')
#         elif cfg.ammo > 0 and cfg.bullet_chambered:
#             cfg.ammo -= 1
#             print('Bang!')
#         else:
#             cfg.bullet_chambered = False
#             print('*Click*')

#     def process_mouse_input(self, mouse_pos):
#         """ Process mouse input """
#         self.process_fire()

#     def process_keyboard_input(self, keys):
#         """ Process keyboard input """
#         if keys[pygame.K_r]:
#             if cfg.magazine_in_hand:
#                 if cfg.magazine_inserted:
#                     print('Removing magazine')
#                 else:
#                     print('Loading magazine')

#                 cfg.magazine_inserted = not cfg.magazine_inserted
#             else:
#                 print('You are not holding a magazine')

#         if keys[pygame.K_f]:
#             print('Racking')
#             if cfg.bullet_chambered:
#                 cfg.ammo -= 1

#             if cfg.ammo > 0:
#                 cfg.bullet_chambered = True
#             else:
#                 cfg.bullet_chambered = False

#         if keys[pygame.K_t]:
#             if cfg.magazine_in_hand:
#                 if not cfg.magazine_inserted:
#                     print('Checking Magazine')
#                     if cfg.ammo >= 5:
#                         print('Magazine is full')
#                     elif 5 > cfg.ammo > 1:
#                         print('Magazine is half-full')
#                     elif cfg.ammo == 1:
#                         print('Magazine is almost empty')
#                     elif cfg.ammo == 0:
#                         print('Magazine is empty')
#                 else:
#                     print('Remove magazine first')
#             else:
#                 print('You must be holding the magazine')

#         if keys[pygame.K_g]:
#             print('Checking Chamber')
#             if cfg.bullet_chambered:
#                 print('A bullet is chambered')
#             else:
#                 print('No bullet is chambered')

#         if keys[pygame.K_v]:
#             cfg.firing_index = (cfg.firing_index + 1) % len(cfg.firing_mode)
#             print(cfg.firing_mode[cfg.firing_index])

#         slots = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]
#         for i, slot in enumerate(slots, 1):
#             if keys[slot]:
#                 if not cfg.magazine_inserted:

#                     if cfg.pouch_data[i]['slot_filled'] and cfg.magazine_in_hand:
#                         print(f'Slot {i} is filled with another magazine, pick another one')
#                     elif cfg.magazine_in_hand:
#                         print(f'Magazine inserted into slot {i}')
#                         cfg.pouch_data[i]['slot_filled'] = True
#                         cfg.pouch_data[i]['ammo'] = cfg.ammo
#                         cfg.magazine_in_hand = False
#                         cfg.ammo = 0
#                     else:
#                         print(f'Grabbed magazine from slot {i}')
#                         cfg.pouch_data[i]['slot_filled'] = False
#                         cfg.ammo = cfg.pouch_data[i]['ammo']
#                         cfg.magazine_in_hand = True
#                         cfg.pouch_data[i]['ammo'] = 0

#                     # print('ammo:', cfg.ammo, ' slot_filled:', cfg.pouch_data[i]['slot_filled'],
#                     #       f' slot {i} ammo:', cfg.pouch_data[i]['ammo'], ' magazine_in_hand:', cfg.magazine_in_hand)

#                 else:
#                     print('Remove magazine first')

#         # print('ammo:', cfg.ammo, 'chambered?:', cfg.bullet_chambered, 'magazine:', cfg.magazines)


# def main():
#     """ === DRIVER CODE === """
#     # Initiate instances
#     program = Program()
#     # crt = c.CRT(1280, 720, screen)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 program.process_mouse_input(mouse_pos)
#             if event.type == pygame.KEYDOWN:
#                 keys = pygame.key.get_pressed()
#                 program.process_keyboard_input(keys)

#         # Run program
#         program.run()
#         # crt.draw()

#         # Updates
#         pygame.display.flip()
#         screen.fill(cfg.BLACK)


# if __name__ == "__main__":
#     main()

import ast
import pygame

from data.src import GameLibrary
from data.src import Config

window = GameLibrary.Window(ast.literal_eval(Config.user_config.get("Window", "Size", fallback="(1920, 1080)")))
window.fps = int(Config.user_config.get("Window", "FPS", fallback=60))

if Config.user_config.get("Window", "WindowMode") == "Windowed":
    window.make_windowed()
elif Config.user_config.get("Window", "WindowMode") == "WindowedBorderless":
    window.make_borderless()
elif Config.user_config.get("Window", "WindowMode") == "Fullscreen":
    window.make_fullscreen()

default_font = Config.user_config.get("Window", "Font", fallback="data\\font\\charybdis.ttf")
default_font = pygame.font.Font(default_font, 30)

small_font = Config.user_config.get("Window", "Font", fallback="data\\font\\charybdis.ttf")
small_font = pygame.font.Font(small_font, 20)

backpack = GameLibrary.BackpackComponent(Config.user_config.get("Player", "Backpack", fallback="DefaultBackpack"), default_font, font_color="White")
backpack.small_font = small_font
def backpack_keybind():
    backpack.shown = not backpack.shown
window.add_keybind(pygame.K_TAB, backpack_keybind)
window.add_component(backpack)

window.render()
