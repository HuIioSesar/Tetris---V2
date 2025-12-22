import pygame

class Options2Screen:
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
            ["frame_top270"]+["filler"]*18+["frame_top90"],
            #4
            ["frame_top270"]+["filler"]*5+["corner_game_left"]+["frame_game_top"]*5+["corner_game_right"]+["filler"]*6+["frame_top90"],
            #5
            ["frame_top270"]+["filler"]*5+["frame_game_left"]+["L"]+["E"]+["V"]+["E"]+["L"]+["frame_game_right"]+["filler"]*6+["frame_top90"],
            #6
            ["frame_top270"]+["filler"]*3+["corner_type_leftU"]+["frame_type_top"]+["corner_game_typeL"]+["frame_game_type"]*5+["corner_game_typeR"]+["frame_type_top"]*1+["corner_type_rightU"]+["filler"]*4+["frame_top90"],
            #7
            ["frame_top270"]+["filler"]*3+["frame_type_left"]+["P0-op2"]+["frame_type_middle"]+["P1"]+["frame_type_middle"]+["P2-op2"]+["frame_type_middle"]+["P3"]+["frame_type_middle"]+["P4"]+["frame_type_right"]+["filler"]*4+["frame_top90"],
            #8
            ["frame_top270"]+["filler"]*3+["frame_type_typeL"]+["frame_type_type"]*9+["frame_type_typeR"]+["filler"]*4+["frame_top90"],
            #9
            ["frame_top270"]+["filler"]*3+["frame_type_left"]+["P5-op2"]+["frame_type_middle"]+["P6"]+["frame_type_middle"]+["P7"]+["frame_type_middle"]+["P8"]+["frame_type_middle"]+["P9"]+["frame_type_right"]+["filler"]*4+["frame_top90"],
            #10
            ["frame_top270"]+["filler"]*3+["corner_type_leftD"]+["frame_type_bottom"]*9+["corner_type_rightD"]+["filler"]*4+["frame_top90"],
            #11
            ["frame_top270"]+["filler"]*3+["corner_game_left"]+["frame_game_top"]*9+["corner_game_right"]+["filler"]*4+["frame_top90"],
            #12
            ["frame_top270"]+["filler"]*3+["frame_game_left"]+["T"]+["O"]+["P"]+["-"]+["S"]+["C"]+["O"]+["R"]+["E"]+["frame_game_right"]+["filler"]*4+["frame_top90"],
            #13
            ["frame_top270"]+["corner_type_leftU"]+["frame_type_top"]*2+["corner_game_typeL"]+["frame_game_type"]*9+["corner_game_typeR"]+["frame_type_top"]*3+["corner_type_rightU"]+["frame_top90"],
            #14
            ["frame_top270"]+["frame_type_left"]+["P1-3"]+["frame_type_middle"]+["dot"]*7+["0"]+["dot"]*6+["frame_type_right"]+["frame_top90"],
            #15
            ["frame_top270"]+["frame_type_left"]+["P2-3"]+["frame_type_middle"]+["dot"]*7+["0"]+["dot"]*6+["frame_type_right"]+["frame_top90"],
            #16
            ["frame_top270"]+["frame_type_left"]+["P3-3"]+["frame_type_middle"]+["dot"]*7+["0"]+["dot"]*6+["frame_type_right"]+["frame_top90"],
            #17
            ["frame_top270"]+["corner_type_leftD"]+["frame_type_bottom"]*2+["frame_type_bottom"]*11+["frame_type_bottom"]*3+["corner_type_rightD"]+["frame_top90"],
            #18
            ["corner_top270"]+["frame_top180"]*18+["corner_top180"]
        ]

        self.level_options = [
            {"tiles": ["P0-op2", "P1", "P2-op2", "P3", "P4"], "row": 6, "col_start": 5, "spacing": 2},
            {"tiles": ["P5-op2", "P6", "P7", "P8", "P9"], "row": 8, "col_start": 5, "spacing": 2}
        ]

        self.selected_row = 0
        self.selected_col = 0

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
        for i, option in enumerate(self.level_options):
            row = option["row"]
            col_start = option["col_start"]

            for j, char in enumerate(option["tiles"]):
                x = (col_start + j * option["spacing"]) * self.settings.tile_size * self.settings.scale
                y = row * self.settings.tile_size * self.settings.scale

                tile_matrix = self.tiles.tiles[char]

                # Si es la opción seleccionada y blink_on está activo, recolorear
                if i == self.selected_row and j == self.selected_col and not blink_on:
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
                        return "options1"  # Volver a pantalla anterior

                    elif event.key == pygame.K_RETURN:
                        # Calculamos el nivel seleccionado y pasamos a la siguiente pantalla
                        starting_level = self.selected_row * len(self.level_options[0]["tiles"]) + self.selected_col
                        return ("game", starting_level)

                    # Navegación
                    if event.key == pygame.K_LEFT:
                        self.selected_col = max(0, self.selected_col - 1)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_col = min(len(self.level_options[self.selected_row]["tiles"]) - 1, self.selected_col + 1)
                    elif event.key == pygame.K_UP:
                        self.selected_row = max(0, self.selected_row - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected_row = min(len(self.level_options) - 1, self.selected_row + 1)

            # Blink cada 30 frames
            frame_count += 1
            if frame_count % 30 == 0:
                blink_on = not blink_on
                self.draw_selected_options(blink_on)
                pygame.display.flip()  # Refresh screen after arrow update   