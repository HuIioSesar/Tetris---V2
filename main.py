import pygame
from settings import Settings
from tiles import Tiles
from screens.startscreen import StartScreen
from screens.options1 import Options1Screen
from screens.options2 import Options2Screen
from screens.game_over import GameOver
from screens.victory_screen_A import VictoryScreenA
from assets.sounds.music import MusicManager
from assets.sounds.sfx import SFXManager
from game_loop import GameLoop

def main():
    pygame.init()

    # Create settings and screen
    settings = Settings()
    music = MusicManager()
    sfx = SFXManager()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Tetris")

    # Shared Tiles object
    tiles = Tiles(settings.gb_colours, settings.tile_size, settings.scale)

    # Start with StartScreen
    current_screen = "start"
    starting_level = 0
    options_payload = None

    while current_screen != "quit":
        if current_screen == "start":
            next_screen = StartScreen(screen, settings, tiles, music).run()

        elif current_screen == "options1":
            next_screen = Options1Screen(screen, settings, tiles, music, sfx).run()

        elif current_screen == "options2":
            # Options2Screen may return either "game" or a tuple ("game", starting_level)
            result = Options2Screen(screen, settings, tiles, music, sfx, options_payload).run()
            if isinstance(result, tuple):
                next_screen, starting_level = result
            else:
                next_screen = result
            # After name-entry, reset payload so Options2 returns to normal
            options_payload = None

        elif current_screen == "game":
            # GameLoop now returns (next_screen, payload)
            next_screen, game_payload = GameLoop(screen, settings, tiles, starting_level, music, sfx).run()

        elif current_screen == "game_over":
            # GameOver now returns (next_screen, payload_for_options2)
            next_screen, options_payload = GameOver(screen, settings, tiles, music, sfx, game_payload).run()

        current_screen = next_screen

    pygame.quit()

if __name__ == "__main__":
    main()