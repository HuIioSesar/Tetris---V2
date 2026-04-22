import pygame
from utilities import Blinker
from screens.screen_utilities import ScreenUtilities

class StartScreen:
    def __init__(self, screen, settings, tiles, music):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.music = music
        self.arrow_x = 4 * settings.tile_size * settings.scale
        self.arrow_y = 14 * settings.tile_size * settings.scale
        self.clock = pygame.time.Clock()
        self.blinker = Blinker(self.settings.fps)

    # Draw blinking arrow
    def draw_arrow(self, blink_on):
        if not blink_on:
            self.tiles.draw_tile("arrow", self.arrow_x, self.arrow_y, self.screen)
        else:
            self.tiles.draw_tile("0", self.arrow_x, self.arrow_y, self.screen)

    def run(self):
        running = True
        self.music.play_music("assets/sounds/startscreen.mp3")        
        
        ScreenUtilities.draw_screen( ScreenUtilities.StartScreen, self.screen, self.settings, self.tiles )

        while running:
            self.clock.tick(self.settings.fps)
            blink_on = self.blinker.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                        return "options1"

            self.draw_arrow(blink_on)
            pygame.display.flip()