
import pygame

class StartScreen:
    def __init__(self, screen, settings, tiles):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.arrow_x = 4 * settings.tile_size * settings.scale
        self.arrow_y = 14 * settings.tile_size * settings.scale
        self.clock = pygame.time.Clock()

        #Define screen matrix
        self.screengrid = [
            ["3"]*20,
            ["top_corner"] + ["top_frame"] * 18 + ["top_corner_mirror"],
            ["side_frame","T_1_1","T_1_2","T_1_3","T_1_4","T_1_5","T_1_6","T_1_7","T_1_2","T_1_3","T_1_4","T_1_11","T_1_12","T_1_13","T_1_14","T_1_15","T_1_16","T_1_17","T_1_18","side_frame_mirror"],
            ["side_frame","T_2_1","T_2_2","T_2_3","T_2_4","T_2_5","T_2_6","T_2_7","T_2_2","T_2_3","T_2_4","T_2_11","T_2_12","T_2_13","T_2_14","T_2_15","T_2_16","T_2_17","0","side_frame_mirror"],
            ["side_frame","0","T_3_2","T_3_3","0","T_3_5","T_3_6","T_3_7","T_3_2","T_3_3","0","T_3_11","T_3_12","T_3_13","T_3_14","T_3_15","T_3_16","T_3_17","0","side_frame_mirror"],
            ["side_frame","0","T_4_2","T_4_3","0","T_4_5","T_4_6","T_4_7","T_4_2","T_4_3","0","T_4_11","T_4_12","T_4_13","T_4_14","T_4_15","T_4_16","T_4_17","0","side_frame_mirror"],
            ["bottom_corner"]+["bottom_frame"]*18+["bottom_corner_mirror"],
            ["3"]+["k_top_frame"]*13+["k_11"]+["k_12"]+["k_top_frame"]*3+["3"],
            ["3","1","1","sun_1","sun_2","1","1","small_star","1","1","1","1","1","small_star","k_21","k_22","big_star","1","1","3"],
            ["3","small_star","1","sun_3","sun_4","1","1","1","1","big_star","1","1","1","1","k_31","k_32","1","1","1","3"],    
            ["3"]+["1"]*12+["k_41"]+["k_42"]+["k_43"]+["k_44"]+["k_45"]+["k_46"]+["3"],
            ["3","1","1","1","1","small_star","1","1","1","1","k_51","k_52","1","k_54","k_55","k_56","k_57","k_58","k_59","3"],
            ["3","1","1","1","1","1","1","1","1","k_61","k_62","k_63","k_64","k_65","k_66","k_67","k_68","k_69","k_60","3"],
            ["k_bottom"]*20,
            ["0"]*5+["P"]+["R"]+["E"]+["S"]+["S"]+["0"]+["S"]+["T"]+["A"]+["R"]+["T"]+["0"]*4,
            ["0"]*5+["underline"]*11+["0"]*4,
            ["0"]*5+["c"]+["P2-start"]+["P0-start"]+["P2-start"]+["P5-start"]+["0"]+["p"]+["p"]+["s"]+["g"]+["ib"]+["0"]*4,
            ["0"]*20
            ]

    #Draw screen    
    def draw_screen(self):
        for row_index, tile_row in enumerate(self.screengrid):
            for col_index, tile_name in enumerate(tile_row):
                x = col_index * self.settings.tile_size * self.settings.scale
                y = row_index * self.settings.tile_size * self.settings.scale
                self.tiles.draw_tile(tile_name, x, y, self.screen)


    # Draw blinking arrow
    def draw_arrow(self, blink_on):
        if not blink_on:
            self.tiles.draw_tile("arrow", self.arrow_x, self.arrow_y, self.screen)
        else:
            self.tiles.draw_tile("0", self.arrow_x, self.arrow_y, self.screen)


    def run(self):
        """Bucle principal de la pantalla de inicio."""
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
                    running = False
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter para continuar
                        running = False
                        return "options1"


            # Blink every 30 frames
            frame_count += 1
            if frame_count % 30 == 0:
                blink_on = not blink_on
                self.draw_arrow(blink_on)
                pygame.display.flip()  # Refresh screen after arrow update