import pygame
from screens.screen_utilities import ScreenUtilities

class VictoryScreenA:
    def __init__(self, screen, settings, tiles, music, sfx):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.clock = pygame.time.Clock()
        self.scale = settings.tile_size * settings.scale 

        # Rocket position (tile coordinates)
        self.rocket_x = 9 * self.scale   
        self.rocket_y = 12 * self.scale  

        self.frame_counter = 0
        self.flame_toggle = False

        # Animation control
        self.finished = False

    def draw_rocket(self):
        # Rocket nose
        self.tiles.draw_tile("rocket_nose", self.rocket_x, self.rocket_y, self.screen)

        # Rocket body
        self.tiles.draw_tile("rocket_body", self.rocket_x, self.rocket_y + 1 * self.scale, self.screen)
        self.tiles.draw_tile("rocket_body", self.rocket_x, self.rocket_y + 2 * self.scale, self.screen)

        # Flame animation
        flame_tile = "rocket_flame_1" if self.flame_toggle else "rocket_flame_2"
        self.tiles.draw_tile(flame_tile, self.rocket_x, self.rocket_y + 3 * self.scale, self.screen)

    def run(self):
        running = True

        while running:
            self.clock.tick(self.settings.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

            self.frame_counter += 1

            # Move rocket every 8 frames (slow GB‑style)
            if self.frame_counter % 2 == 0:
                self.rocket_y -= 1
                self.flame_toggle = not self.flame_toggle

            # When rocket leaves screen → end animation
            if self.rocket_y < -5:
                return "start"

            ScreenUtilities.draw_screen( ScreenUtilities.VictoryBackground, self.screen, self.settings, self.tiles )
            self.draw_rocket()

            pygame.display.flip()