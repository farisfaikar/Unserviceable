import pygame
import sys
from data.src import Config
import ast

pygame.init()

class Component:
    def __init__(self) -> None:
        self.shown = False
    
    def render(self, pygame_window: pygame.SurfaceType):
        '''Function used when rendering the Component, runs every frame'''
        pass

    def handle_event(self, event: pygame.event.Event):
        '''Function used when an event occurs in pygame window'''
        pass


class BackpackComponent(Component):
    def __init__(self, backpack_type: str, font: pygame.font.FontType, font_color = "White") -> None:
        super().__init__()
        self.backpack_type = backpack_type
        
        self.font = font
        self.small_font = font
        self.font_color = font_color
        
        self.size = (100, 100)
        self.color = Config.item_config.get(backpack_type, "BackpackColor", fallback="#404d32")

        self.pos = (50, 20)
    
    def render(self, pygame_window: pygame.SurfaceType):

        window_width = pygame_window.get_width()
        window_height = pygame_window.get_height()
        self.size = ((window_width-100)/6, (window_height-40)/2+20)
        
        self.rect = pygame.Rect(*self.pos, *self.size)
        pygame.draw.rect(pygame_window, self.color, self.rect)

        backpack_title = TextComponent(self.backpack_type, self.font, self.font_color)
        backpack_title.pos = (self.pos[0]+(self.size[0]/2-backpack_title.get_width()/2), self.pos[1]+10)
        backpack_title.render(pygame_window)

        control_text = TextComponent("Tab - Open/Close backpack", self.small_font, self.font_color)
        control_text.pos = (self.pos[0]+(self.size[0]/2-control_text.get_width()/2), self.pos[1]+self.size[1]-10-control_text.get_height())
        control_text.render(pygame_window)

        usable_height = self.rect.height - 20 - backpack_title.get_height() - 20 - control_text.get_height()
        usable_width = self.rect.width - 20

        pygame.draw.rect(pygame_window, "Black", pygame.Rect(self.pos[0]+10, self.pos[1]+backpack_title.get_height()+20, usable_width, usable_height))

        row_x = self.pos[0]+20
        for row in range(int(Config.item_config.getint(self.backpack_type, "AmmoPouchCount", fallback=5)/5)):
            row_y = (self.pos[1]+backpack_title.get_height()+20) * (row+1)
            row_y += 10

            row_width = (usable_width-40)/5

            for column in range(0, 5):
                color = Config.item_config.get(self.backpack_type, "PouchColor", fallback="Black")
                rect = pygame.Rect(row_x+(row_width)*column+5*column, row_y, row_width, row_width)
                pygame.draw.rect(pygame_window, color, rect)


class TextComponent(Component):
    def __init__(self, text: str, font: pygame.font.FontType, color = "Black", pos: tuple = (0, 0)) -> None:
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos

    def get_width(self):
        return self.font.size(self.text)[0]

    def get_height(self):
        return self.font.size(self.text)[1]

    def render(self, pygame_window: pygame.surface.SurfaceType):
        text_render = self.font.render(self.text, True, self.color)
        pygame_window.blit(text_render, self.pos)


class Window:
    def __init__(self, window_size: list) -> None:
        self.flags = 0
        self.window_size = window_size

        self.background_image = None
        self.background_color = (0, 0, 0)

        self.fps = 60

        self.components = []
        self.keybinds = []
    
    def make_fullscreen(self):
        self.flags = pygame.FULLSCREEN
        self.window_size = (0, 0)

    def make_windowed(self):
        self.flags = 0
    
    def make_borderless(self, fullscreen: bool):
        if fullscreen:
            self.flags = pygame.NOFRAME | pygame.FULLSCREEN
            self.window_size = (0, 0)

        else:
            self.flags = pygame.NOFRAME

    def add_component(self, component: Component):
        self.components.append(component)

    def add_keybind(self, key, fun: callable):
        self.keybinds.append([key, fun])

    def render(self):
        self.window = pygame.display.set_mode(self.window_size, self.flags)

        clock = pygame.time.Clock()
        
        while True:

            # Background
            if self.background_image == None:
                self.window.fill(self.background_color)
            else:
                self.window.blit(self.background_image, (0, 0))
            
            for component in self.components:
                if component.shown == True:
                    component.render(self.window)

            clock.tick(self.fps)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                else:
                    for keybind in self.keybinds:
                        if event.type == pygame.KEYUP:
                            if event.key == keybind[0]:
                                keybind[1]()

                    for component in self.components:
                        if component.shown == True:
                            component.handle_event(event)

