# """ Config file to store global variables """
# Ammo
# ammo = 5
# pouch_data = {  # This could be an object/class?
#     1: {
#         'slot_filled': False,
#         'ammo': 0,
#     }, 2: {
#         'slot_filled': True,
#         'ammo': 5,
#     }, 3: {
#         'slot_filled': True,
#         'ammo': 5,
#     }, 4: {
#         'slot_filled': True,
#         'ammo': 5,
#     }
# }
# bullet_chambered = True
# magazine_inserted = True
# magazine_in_hand = True
# firing_mode = ['safe', 'single', 'automatic']
# firing_index = 0

from configparser import ConfigParser

weapon_config = ConfigParser(allow_no_value=False)
weapon_config.read("data\\configs\\Weapons.config")

user_config = ConfigParser(allow_no_value=False)
user_config.read("data\\configs\\User.config")

item_config = ConfigParser(allow_no_value=False)
item_config.read("data\\configs\\Items.config")

