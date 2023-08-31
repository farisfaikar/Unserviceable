import pygame
import sys
from data.src import Config

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

        window_width = 1920
        window_height = 1080
        self.size = ((window_width-100)/6, (window_height-40)/2+20)
        self.rect = pygame.Rect(*self.pos, *self.size)
        self.backpack_title = TextComponent(self.backpack_type, self.font, self.font_color)
        self.backpack_title.pos = (self.pos[0]+(self.size[0]/2-self.backpack_title.get_width()/2), self.pos[1]+10)
        self.control_text = TextComponent("Tab - Open/Close backpack", self.small_font, self.font_color)
        self.usable_height = self.rect.height - 20 - self.backpack_title.get_height() - 20 - self.control_text.get_height()
        self.usable_width = self.rect.width - 20        
    
    def render(self, pygame_window: pygame.SurfaceType):

        window_width = pygame_window.get_width()
        window_height = pygame_window.get_height()
        self.size = ((window_width-100)/6, (window_height-40)/2+20)
        
        self.rect = pygame.Rect(*self.pos, *self.size)
        pygame.draw.rect(pygame_window, self.color, self.rect)

        self.backpack_title = TextComponent(self.backpack_type, self.font, self.font_color)
        self.backpack_title.pos = (self.pos[0]+(self.size[0]/2-self.backpack_title.get_width()/2), self.pos[1]+10)
        self.backpack_title.render(pygame_window)

        self.control_text = TextComponent("Tab - Open/Close backpack", self.small_font, self.font_color)
        self.control_text.pos = (self.pos[0]+(self.size[0]/2-self.control_text.get_width()/2), self.pos[1]+self.size[1]-10-self.control_text.get_height())
        self.control_text.render(pygame_window)

        self.usable_height = self.rect.height - 20 - self.backpack_title.get_height() - 20 - self.control_text.get_height()
        self.usable_width = self.rect.width - 20

        pygame.draw.rect(pygame_window, "Black", pygame.Rect(self.pos[0]+10, self.pos[1]+self.backpack_title.get_height()+20, self.usable_width, self.usable_height))

    def handle_event(self, event: pygame.event.Event):
        if self.shown == True:
            pass


class Gun(Component):
    def __init__(self) -> None:
        self.shown = True

        self.mag = 6
        self.chamber = 0
        self.modes = ["Safe", "Single", "Burst"]

        self.mag_loaded = False
        self.current_mode = 0

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                self.mag_loaded = not self.mag_loaded
                print("Realoded")

            elif event.key == pygame.K_f:
                self.mag -= 1
                self.chamber = 1
                print("Chambered")
            
            elif event.key == pygame.K_t:
                if self.mag == 6:
                    print("Full")
                elif self.mag > 3 and self.mag <= 5:
                    print("Mostly full")
                elif self.mag == 3:
                    print("Half full")
                elif self.mag <= 3:
                    print("A few bullets left")        
                elif self.mag == 0:
                    print("Empty")

            elif event.key == pygame.K_g:
                if self.chamber == 1:
                    print("Chambered")
                elif self.chamber == 0:
                    print("Nothing is chambered")

            elif event.key == pygame.K_v:
                if not self.current_mode >= 2:
                    self.current_mode += 1
                else:
                    self.current_mode = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.modes[self.current_mode] == "Safe":
                    print("*Click*")
                elif self.modes[self.current_mode] == "Single":
                    print("Fire shot")
                    self.chamber -=1
                    self.mag -=1
                elif self.modes[self.current_mode] == "Burst":
                    print("Fire shot")
                    self.chamber -=1
                    self.mag -=1
                    if self.mag >= 0:
                        self.mag -=1
                        self.chamber += 1
                    print("Fire shot")
                    self.chamber -=1
                    self.mag -=1
                    if self.mag >= 0:
                        self.mag -=1
                        self.chamber += 1
                    print("Fire shot")
                    self.chamber -=1
                    self.mag -=1
                    if self.mag >= 0:
                        self.mag -=1
                        self.chamber += 1

class PlayerComponent(Component):
    def __init__(self):
       self.shown = True

    def render(self, window:pygame.SurfaceType):
        player_img = pygame.image.load("data\\img\\player.png")
        window.blit(player_img, (1920/2, 1080/2))



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
        self.running = True

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

    def quit(self):
        pygame.quit()
        sys.exit(0)
        self.running = False

    def render(self):
        self.window = pygame.display.set_mode(self.window_size, self.flags)

        clock = pygame.time.Clock()
        
        while self.running:

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

