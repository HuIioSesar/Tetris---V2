import pygame

class GameBackgroundScreen:
    def __init__(self, screen, settings, tiles):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.clock = pygame.time.Clock()

        self.screengrid = [
        #1
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_r1_corner"]+["score_topline"]*5+["score_corner_top"],  
        #2    
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r2"]+["S"]+["C"]+["O"]+["R"]+["E"]+["score_right_frame"],    
        #3            
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r3"]+["score_bottom_frame"]*5+["score_corner_frame"],
        #4
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["0"]*7,                     
        #5
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r5"]+["score_bottomline"]*6,          
        #6      
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r1_corner"]+["score_topline"]*5+["score_corner_top"], 
        #7               
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_r7"]+["L"]+["E"]+["V"]+["E"]+["L"]+["score_rightline"],   
        #8 
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r7"]+["0"]*5+["score_rightline"],
        #9
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r9"]+["score_dobleline"]*5+["score_corner_doble"],
        #10
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_r7"]+["L"]+["I"]+["N"]+["E"]+["S"]+["score_rightline"],
        #11
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r7"]+["0"]*5+["score_rightline"],
        #12
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r12_corner"]+["score_bottomline"]*5+["score_corner_bottom"],
        #13
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_right"]+["next_piece_corner"]+["next_piece_line"]*4+["next_piece_corner90"],
        #14
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        #15
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        #16
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        #17
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        #18
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_right"]+["next_piece_corner270"]+["next_piece_line180"]*4+["next_piece_corner180"],
    ]

    #In the future, all screens could be together? The draw in the same way, just need a diferent matrix to print
    def draw_screen(self):
        for row_index, tile_row in enumerate(self.screengrid):
            for col_index, tile_name in enumerate(tile_row):
                x = col_index * self.settings.tile_size * self.settings.scale
                y = row_index * self.settings.tile_size * self.settings.scale
                self.tiles.draw_tile(tile_name, x, y, self.screen)
                