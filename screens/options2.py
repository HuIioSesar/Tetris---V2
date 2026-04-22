import pygame
from utilities import ScoreManager,Blinker
from screens.screen_utilities import ScreenUtilities

class Options2Screen:
    def __init__(self, screen, settings, tiles, music, sfx, options_payload):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.music = music
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.blinker = Blinker(self.settings.fps)
                
        # Name entry mode state
        self.name_entry_active = False     # Are we editing the name?
        self.name_entry_row = None         # Which high-score row (0,1,2)
        self.name_entry_pos = 0            # Cursor position 0-5
        self.name_chars = [""] * 6         # Temporary 6-character name buffer
        self.allowed_chars = [chr(c) for c in range(ord("A"), ord("Z")+1)] + ["Heart"] + ["0"]

        # Payload from GameOver / previous screen
        self.options_payload = options_payload or {}
        self.mode = self.options_payload.get("mode", "TypeA")

        # Load current highscores via ScoreManager
        self.high_scores = ScoreManager.load_top_scores(self.mode, limit=3)

        # Activate name-entry mode if payload says so
        if self.options_payload.get("name_entry"):
            # rank is which row in the high-score table (0, 1, 2)
            self.name_entry_row = self.options_payload.get("rank", 0)
            self.name_entry_active = True
            self.name_entry_pos = 0
            self.name_chars = [""] * 6
            self.name_chars[0] = "A"

        self.level_options = [
            {"tiles": ["N0", "N1", "N2", "N3", "N4"], "row": 6, "col_start": 5, "spacing": 2},
            {"tiles": ["N5", "N6", "N7", "N8", "N9"], "row": 8, "col_start": 5, "spacing": 2} 
        ]

        self.selected_row = 0
        self.selected_col = 0

    def cycle_character(self, current, direction):
        if not current:
            idx = 0  # Start at 'A'
        else:
            try:
                idx = self.allowed_chars.index(current)
            except ValueError:
                idx = 0  # If somehow not in list, reset to 'A'

        idx = (idx + direction) % len(self.allowed_chars)
        return self.allowed_chars[idx]

    @staticmethod
    def recolor_tile(tile_matrix):
        return [
            [   3 if pixel == 1 else
                1 if pixel == 3 else
                0
                for pixel in row ]
            for row in tile_matrix ]
   
    def number_to_tiles(self, score: int):
        return [f"N{digit}" for digit in str(score)]
            
    def name_to_tiles(self, name: str):
        name_tiles = []
        # Work in uppercase so 'player' and 'PLAYER' behave the same
        for ch in name.upper():
            if "A" <= ch <= "Z":
                name_tiles.append(ch)
            elif ch == "*":
                name_tiles.append("Heart")
            elif ch == " ":
                name_tiles.append("0")
            else:
                continue
        return name_tiles

    def draw_number_tiles(self, tile_keys, right_col: int, row: int):
        tile_size_scaled = self.settings.tile_size * self.settings.scale

        for i, tile_key in enumerate(reversed(tile_keys)):
            col = right_col - i
            x = col * tile_size_scaled
            y = row * tile_size_scaled
            self.tiles.draw_tile(tile_key, x, y, self.screen)
    
    def draw_name_tiles( self, tile_keys, row: int, selected_pos: int = None, blink_on: bool = True ):
        name_start_col = 4
        tile_keys = tile_keys[:6]

        for i, tile_key in enumerate(tile_keys):
            if not tile_key or tile_key == " ":
                continue

            col = name_start_col + i
            x = col * self.settings.tile_size * self.settings.scale
            y = row * self.settings.tile_size * self.settings.scale

            tile_matrix = self.tiles.tiles[tile_key]
            is_selected = (i == selected_pos)

            if is_selected and not blink_on:
                tile_matrix = self.recolor_tile(tile_matrix)

            self.tiles.draw_tile(tile_matrix, x, y, self.screen)

    def draw_top_scores(self, blink_on):
        score_rows = [13, 14, 15]
        right_col = 17

        for row_idx, (name, score) in enumerate(self.high_scores):
            row = score_rows[row_idx]

            # NAME
            if self.name_entry_active and self.name_entry_row == row_idx:
                self.draw_name_tiles( self.name_chars, row, selected_pos=self.name_entry_pos, blink_on=blink_on )
            else:
                if name:
                    name_tiles = self.name_to_tiles(name)
                    self.draw_name_tiles( name_tiles, row )

            if score is not None:
                digit_tiles = self.number_to_tiles(score)
                self.draw_number_tiles(digit_tiles, right_col, row)

    # def draw_selected_options(self, blink_on):
    #     for i, option in enumerate(self.level_options):

    #         for j, char in enumerate(option["tiles"]):
    #             x = (option["col_start"] + j * option["spacing"]) * self.settings.tile_size * self.settings.scale
    #             y = option["row"] * self.settings.tile_size * self.settings.scale

    #             invert = True

    #             if i == self.selected_row and j == self.selected_col and not blink_on:
    #                 invert = False 
                
    #             self.tiles.draw_tile(char, x, y, self.screen, recolor=invert)
    
    def draw_selected_options(self, blink_on):
        for i, option in enumerate(self.level_options):
            for j, char in enumerate(option["tiles"]):
                x = (option["col_start"] + j * option["spacing"]) * self.settings.tile_size * self.settings.scale
                y = option["row"] * self.settings.tile_size * self.settings.scale

                invert = True
                if self.name_entry_active:
                    invert = True

                else:
                    if i == self.selected_row and j == self.selected_col and not blink_on:
                        invert = False

                self.tiles.draw_tile(char, x, y, self.screen, recolor=invert)

    
    def compile_name(self, tile_keys) -> str:
        name_keys = []
        for ch in tile_keys[:6]:
            if ch == "Heart":
                name_keys.append("*")
            elif not ch or ch == "0":
                name_keys.append(" ")
            else:
                name_keys.append(ch)
        return "".join(name_keys)

    def run(self):
        running = True
        ScreenUtilities.draw_screen( ScreenUtilities.Options2, self.screen, self.settings, self.tiles )

        while running:
            self.clock.tick(self.settings.fps)
            blink_on = self.blinker.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                elif event.type == pygame.KEYDOWN:

                    #  NAME ENTRY MODE
                    if self.name_entry_active:
                        # Only handle name-input keys
                        if event.key == pygame.K_LEFT:
                            self.name_entry_pos = max(0, self.name_entry_pos - 1)
                            self.sfx.play_blip()
                        elif event.key == pygame.K_RIGHT:
                            self.name_entry_pos = min(5, self.name_entry_pos + 1)
                            if not self.name_chars[self.name_entry_pos]:
                                self.name_chars[self.name_entry_pos] = "A"
                            self.sfx.play_blip()
                        elif event.key == pygame.K_UP:
                            current = self.name_chars[self.name_entry_pos]
                            self.name_chars[self.name_entry_pos] = self.cycle_character(current, +1)
                            self.sfx.play_blip()
                        elif event.key == pygame.K_DOWN:
                            current = self.name_chars[self.name_entry_pos]
                            self.name_chars[self.name_entry_pos] = self.cycle_character(current, -1)
                            self.sfx.play_blip()
                        elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                            name = self.compile_name(self.name_chars)
                            if name.strip() == "":
                                name = "PLAYER"

                            ScoreManager.update_name(self.name_entry_row, name)
                            self.name_entry_active = False
                            return "options2"

                        # Ignore other keys while in name entry
                        continue

                    #  NORMAL OPTIONS2 MODE
                    if event.key == pygame.K_BACKSPACE:
                        return "options1"
                    elif event.key == pygame.K_RETURN:
                        starting_level = self.selected_row * len(self.level_options[0]["tiles"]) + self.selected_col
                        return ("game", starting_level)

                    if event.key == pygame.K_LEFT:
                        self.selected_col = max(0, self.selected_col - 1)
                        self.sfx.play_blip()
                    elif event.key == pygame.K_RIGHT:
                        self.selected_col = min(len(self.level_options[self.selected_row]["tiles"]) - 1, self.selected_col + 1)
                        self.sfx.play_blip()
                    elif event.key == pygame.K_UP:
                        self.selected_row = max(0, self.selected_row - 1)
                        self.sfx.play_blip()
                    elif event.key == pygame.K_DOWN:
                        self.selected_row = min(len(self.level_options) - 1, self.selected_row + 1)
                        self.sfx.play_blip()

            self.draw_top_scores(blink_on)

            self.draw_selected_options(blink_on)

            pygame.display.flip()