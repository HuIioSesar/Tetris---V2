import pygame
from utilities import Blinker
from screens.screen_utilities import ScreenUtilities

class Options1Screen:
    def __init__(self, screen, settings, tiles, music, sfx):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.music = music
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.blinker = Blinker(self.settings.fps)
 
        #Two lists with options as dictionary
        # self.game_options = [
        #     {"tiles": ["A-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 5, "col_start": 3},
        #     {"tiles": ["B-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 5, "col_start": 11}
        # ]
        self.game_options = [
            {"tiles": ["A", "-", "T", "Y", "P", "E"], "row": 5, "col_start": 3},
            {"tiles": ["B", "-", "T", "Y", "P", "E"], "row": 5, "col_start": 11}
        ]

        self.selected_game_index = 0

        self.music_options = [
            {"tiles": ["A", "-", "T", "Y", "P", "E"], "row": 12, "col_start": 3, "file": "assets/sounds/typeA.mp3"},
            {"tiles": ["B", "-", "T", "Y", "P", "E"], "row": 12, "col_start": 11, "file": "assets/sounds/typeB.mp3"},
            {"tiles": ["C", "-", "T", "Y", "P", "E"], "row": 14, "col_start": 3, "file": "assets/sounds/typeC.mp3"},
            {"tiles": ["O", "F", "F"], "row": 14, "col_start": 12, "file": None}
        ]

        self.selected_music_index = 0

        self.selection_phase = 1  # 1 = game selection, 2 = music selection
        
    def update_music_selection(self):
        musicpath = self.music_options[self.selected_music_index]["file"]
        if musicpath is None:
            self.music.stop_music()  # OFF
        else:
            self.music.play_music(musicpath)
    
    def move_music_selection(self, delta):
        old_index = self.selected_music_index

        new_index = self.selected_music_index + delta
        new_index = max(0, min(len(self.music_options) - 1, new_index))

        if new_index != old_index:
            self.selected_music_index = new_index
            self.sfx.play_blip()
            self.update_music_selection()


    def draw_selected_options(self, blink_on):
        # ---------- GAME OPTIONS ----------
        for i, option in enumerate(self.game_options):
            is_selected = (i == self.selected_game_index)

            for j, char in enumerate(option["tiles"]):
                x = (option["col_start"] + j) * self.settings.tile_size * self.settings.scale
                y = option["row"] * self.settings.tile_size * self.settings.scale

                invert = True
                if self.selection_phase == 1:
                    if is_selected and not blink_on:
                        invert = False  
                else:  
                    if is_selected:
                        invert = False

                self.tiles.draw_tile(char, x, y, self.screen, recolor=invert)

        # ---------- MUSIC OPTIONS ----------
        for i, option in enumerate(self.music_options):
            is_selected = (i == self.selected_music_index)

            for j, char in enumerate(option["tiles"]):
                x = (option["col_start"] + j) * self.settings.tile_size * self.settings.scale
                y = option["row"] * self.settings.tile_size * self.settings.scale

                invert = True
                if self.selection_phase == 2:
                    if is_selected and not blink_on:
                        invert = False

                self.tiles.draw_tile(char, x, y, self.screen, recolor=invert)

    def run(self):
        running = True
        
        ScreenUtilities.draw_screen( ScreenUtilities.Options1, self.screen, self.settings, self.tiles )

        while running:
            self.clock.tick(self.settings.fps)
            blink_on = self.blinker.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.selection_phase == 1:
                            return "start"  # Go back to previous screen
                        else:
                            self.selection_phase = 1  # Go back to game selection

                    elif event.key == pygame.K_RETURN:
                        if self.selection_phase == 1:
                            self.selection_phase = 2  # Move to music selection
                            self.update_music_selection()
                        else:
                            return "options2"  # Move to next screen

                    # Navigation logic
                    if self.selection_phase == 1:
                        # Game selection
                        if event.key == pygame.K_LEFT:
                            self.selected_game_index = max(0, self.selected_game_index - 1)
                            self.sfx.play_blip()
                        elif event.key == pygame.K_RIGHT:
                            self.selected_game_index = min(len(self.game_options) - 1, self.selected_game_index + 1)
                            self.sfx.play_blip()

                    elif self.selection_phase == 2:
                        if event.key == pygame.K_LEFT:
                            self.move_music_selection(-1)
                        elif event.key == pygame.K_RIGHT:
                            self.move_music_selection(+1)
                        elif event.key == pygame.K_UP:
                            self.move_music_selection(-2)
                        elif event.key == pygame.K_DOWN:
                            self.move_music_selection(+2)
                
            self.draw_selected_options(blink_on)
            pygame.display.flip()

                                    