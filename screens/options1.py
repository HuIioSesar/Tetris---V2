import pygame

class Options1Screen:
    def __init__(self, screen, settings, tiles):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.clock = pygame.time.Clock()
 
        self.screengrid = [
            #1
            ["corner_top"]+["frame_top"]*18+["corner_top90"],
            #2
            ["frame_top270"]+["filler"]*18+["frame_top90"],
            #3
            ["frame_top270"]+["filler"]*3+["corner_game_left"]+["frame_game_top"]*9+["corner_game_right"]+["filler"]*4+["frame_top90"],
            #4
            ["frame_top270"]+["filler"]*3+["frame_game_left"]+["G-3"]+["A-3"]+["M-3"]+["E-3"]+["0"]+["T-3"]+["Y-3"]+["P-3"]+["E-3"]+["frame_game_right"]+["filler"]*4+["frame_top90"],
            #5
            ["frame_top270"]+["filler"]+["corner_type_leftU"]+["frame_type_top"]+["corner_game_typeL"]+["frame_game_type"]*9+["corner_game_typeR"]+["frame_type_top"]*2+["corner_type_rightU"]+["filler"]+["frame_top90"],
            #6
            ["frame_top270"]+["filler"]+["frame_type_left"]+["A-1"]+["--1"]+["T-1"]+["Y-1"]+["P-1"]+["E-1"]+["0"]+["|"]+["B-1"]+["--1"]+["T-1"]+["Y-1"]+["P-1"]+["E-1"]+["frame_type_right"]+["filler"]+["frame_top90"],
            #7
            ["frame_top270"]+["filler"]+["corner_type_leftD"]+["frame_type_bottom"]*14+["corner_type_rightD"]+["filler"]+["frame_top90"],
            #8
            ["frame_top270"]+["filler"]*18+["frame_top90"],
            #9
            ["frame_top270"]+["filler"]*18+["frame_top90"],
            #10
            ["frame_top270"]+["filler"]*3+["corner_game_left"]+["frame_game_top"]*10+["corner_game_right"]+["filler"]*3+["frame_top90"],
            #11
            ["frame_top270"]+["filler"]*3+["frame_game_left"]+["M-3","U-3","S-3","I-3","C-3","0","T-3","Y-3","P-3","E-3"]+["frame_game_right"]+["filler"]*3+["frame_top90"],
            #12
            ["frame_top270"]+["filler"]+["corner_type_leftU"]+["frame_type_top"]+["corner_game_typeL"]+["frame_game_type"]*10+["corner_game_typeR"]+["frame_type_top"]+["corner_type_rightU"]+["filler"]+["frame_top90"],
            #13
            ["frame_top270"]+["filler"]+["frame_type_left"]+["A-1"]+["--1"]+["T-1"]+["Y-1"]+["P-1"]+["E-1"]+["0"]+["|"]+["B-1"]+["--1"]+["T-1"]+["Y-1"]+["P-1"]+["E-1"]+["frame_type_right"]+["filler"]+["frame_top90"],
            #14
            ["frame_top270"]+["filler"]+["frame_type_typeL"]+["frame_type_type"]*14+["frame_type_typeR"]+["filler"]+["frame_top90"],
            #15
            ["frame_top270"]+["filler"]+["frame_type_left"]+["C-1"]+["--1"]+["T-1"]+["Y-1"]+["P-1"]+["E-1"]+["0"]+["|"]+["0"]+["O-1"]+["F-1"]+["F-1"]+["0"]+["0"]+["frame_type_right"]+["filler"]+["frame_top90"],
            #16
            ["frame_top270"]+["filler"]+["corner_type_leftD"]+["frame_type_bottom"]*14+["corner_type_rightD"]+["filler"]+["frame_top90"],
            #17
            ["frame_top270"]+["filler"]*18+["frame_top90"],
            #18
            ["corner_top270"]+["frame_top180"]*18+["corner_top180"]
        ]

        #Two lists with options as dictionary
        self.game_options = [
            {"tiles": ["A-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 5, "col_start": 3},
            {"tiles": ["B-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 5, "col_start": 11}
        ]

        self.selected_game_index = 0

        self.music_options = [
            {"tiles": ["A-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 12, "col_start": 3},
            {"tiles": ["B-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 12, "col_start": 11},
            {"tiles": ["C-1", "--1", "T-1", "Y-1", "P-1", "E-1"], "row": 14, "col_start": 3},
            {"tiles": ["O-1", "F-1", "F-1"], "row": 14, "col_start": 12}
        ]

        self.selected_music_index = 0

        self.selection_phase = 1  # 1 = game selection, 2 = music selection


    @staticmethod
    def recolor_tile(tile_matrix, old_color=1, new_color=3):
        return [
            [new_color if pixel == old_color else pixel for pixel in row]
            for row in tile_matrix
        ]
    

    #In the future, all screens could be together? The draw in the same way, just need a diferent matrix to print
    def draw_screen(self):
        for row_index, tile_row in enumerate(self.screengrid):
            for col_index, tile_name in enumerate(tile_row):
                x = col_index * self.settings.tile_size * self.settings.scale
                y = row_index * self.settings.tile_size * self.settings.scale
                self.tiles.draw_tile(tile_name, x, y, self.screen)


    def draw_selected_options(self, blink_on):
        # Game options
        for i, option in enumerate(self.game_options):
            row = option["row"]
            col_start = option["col_start"]

            for j, char in enumerate(option["tiles"]):
                x = (col_start + j) * self.settings.tile_size * self.settings.scale
                y = row * self.settings.tile_size * self.settings.scale

                tile_matrix = self.tiles.tiles[char]

                # If game selection is confirmed (phase 2), keep it black
                if self.selection_phase == 2 and i == self.selected_game_index:
                    tile_matrix = self.recolor_tile(tile_matrix)
                # If game selection is active and blinking
                elif self.selection_phase == 1 and i == self.selected_game_index and not blink_on:
                    tile_matrix = self.recolor_tile(tile_matrix)

                self.tiles.draw_tile(tile_matrix, x, y, self.screen)

        # Music options
        for i, option in enumerate(self.music_options):
            row = option["row"]
            col_start = option["col_start"]

            for j, char in enumerate(option["tiles"]):
                x = (col_start + j) * self.settings.tile_size * self.settings.scale
                y = row * self.settings.tile_size * self.settings.scale

                tile_matrix = self.tiles.tiles[char]

                # If music selection is active and blinking
                if self.selection_phase == 2 and i == self.selected_music_index and not blink_on:
                    tile_matrix = self.recolor_tile(tile_matrix)

                self.tiles.draw_tile(tile_matrix, x, y, self.screen)


    def run(self):
        running = True
        blink_on = True
        frame_count = 0
        
        #Draws background
        self.draw_screen()
        pygame.display.flip()

        while running:
            self.clock.tick(self.settings.fps)


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
                        else:
                            return "options2"  # Move to next screen

                    # Navigation logic
                    if self.selection_phase == 1:
                        # Game selection
                        if event.key == pygame.K_LEFT:
                            self.selected_game_index = max(0, self.selected_game_index - 1)
                        elif event.key == pygame.K_RIGHT:
                            self.selected_game_index = min(len(self.game_options) - 1, self.selected_game_index + 1)

                    elif self.selection_phase == 2:
                        # Music selection
                        if event.key == pygame.K_LEFT:
                            self.selected_music_index = max(0, self.selected_music_index - 1)
                        elif event.key == pygame.K_RIGHT:
                            self.selected_music_index = min(len(self.music_options) - 1, self.selected_music_index + 1)
                        elif event.key == pygame.K_UP:
                            self.selected_music_index = max(0, self.selected_music_index - 2)  # Move up by 2
                        elif event.key == pygame.K_DOWN:
                            self.selected_music_index = max(0, self.selected_music_index + 2)  # Move down by 2

            # Blink every 30 frames
            frame_count += 1
            if frame_count % 30 == 0:
                blink_on = not blink_on
                self.draw_selected_options(blink_on)
                pygame.display.flip()  # Refresh screen after arrow update                    