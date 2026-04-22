class ScreenUtilities:
    StartScreen = [
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
        ["3","1","1","1","1","1","1","1","1","k_61","k_62","k_63","k_64","k_65","k_66","k_67","k_68","k_69","k_610","3"],
        ["k_bottom"]*20,
        ["0"]*5+["P"]+["R"]+["E"]+["S"]+["S"]+["0"]+["S"]+["T"]+["A"]+["R"]+["T"]+["0"]*4,
        ["0"]*5+["underline"]*11+["0"]*4,
        ["0"]*5+["c"]+["N2-start"]+["N0-start"]+["N2-start"]+["N5-start"]+["0"]+["p"]+["p"]+["s"]+["g"]+["ib"]+["0"]*4,
        ["0"]*20
        ]
    Options1 = [
        ["corner_top"]+["frame_top"]*18+["corner_top90"],
        ["frame_top270"]+["filler"]*18+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["corner_game_left"]+["frame_game_top"]*9+["corner_game_right"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["frame_game_left"]+["G"]+["A"]+["M"]+["E"]+["0"]+["T"]+["Y"]+["P"]+["E"]+["frame_game_right"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]+["corner_type_leftU"]+["frame_type_top"]+["corner_game_typeL"]+["frame_game_type"]*9+["corner_game_typeR"]+["frame_type_top"]*2+["corner_type_rightU"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]+["frame_type_left"]+["A"]+["-"]+["T"]+["Y"]+["P"]+["E"]+["0"]+["|"]+["B"]+["-"]+["T"]+["Y"]+["P"]+["E"]+["frame_type_right"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]+["corner_type_leftD"]+["frame_type_bottom"]*14+["corner_type_rightD"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]*18+["frame_top90"],
        ["frame_top270"]+["filler"]*18+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["corner_game_left"]+["frame_game_top"]*10+["corner_game_right"]+["filler"]*3+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["frame_game_left"]+["M","U","S","I","C","0","T","Y","P","E"]+["frame_game_right"]+["filler"]*3+["frame_top90"],
        ["frame_top270"]+["filler"]+["corner_type_leftU"]+["frame_type_top"]+["corner_game_typeL"]+["frame_game_type"]*10+["corner_game_typeR"]+["frame_type_top"]+["corner_type_rightU"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]+["frame_type_left"]+["A"]+["-"]+["T"]+["Y"]+["P"]+["E"]+["0"]+["|"]+["B"]+["-"]+["T"]+["Y"]+["P"]+["E"]+["frame_type_right"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]+["frame_type_typeL"]+["frame_type_type"]*14+["frame_type_typeR"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]+["frame_type_left"]+["C"]+["-"]+["T"]+["Y"]+["P"]+["E"]+["0"]+["|"]+["0"]+["O"]+["F"]+["F"]+["0"]+["0"]+["frame_type_right"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]+["corner_type_leftD"]+["frame_type_bottom"]*14+["corner_type_rightD"]+["filler"]+["frame_top90"],
        ["frame_top270"]+["filler"]*18+["frame_top90"],
        ["corner_top270"]+["frame_top180"]*18+["corner_top180"]
        ]
    Options2 = [
        ["corner_top"]+["frame_top"]*18+["corner_top90"],
        ["frame_top270"]+["filler"]*18+["frame_top90"],
        ["frame_top270"]+["filler"]*18+["frame_top90"],
        ["frame_top270"]+["filler"]*5+["corner_game_left"]+["frame_game_top"]*5+["corner_game_right"]+["filler"]*6+["frame_top90"],
        ["frame_top270"]+["filler"]*5+["frame_game_left"]+["L"]+["E"]+["V"]+["E"]+["L"]+["frame_game_right"]+["filler"]*6+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["corner_type_leftU"]+["frame_type_top"]+["corner_game_typeL"]+["frame_game_type"]*5+["corner_game_typeR"]+["frame_type_top"]*1+["corner_type_rightU"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["frame_type_left"]+["N0"]+["frame_type_middle"]+["N1"]+["frame_type_middle"]+["N2"]+["frame_type_middle"]+["N3"]+["frame_type_middle"]+["N4"]+["frame_type_right"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["frame_type_typeL"]+["frame_type_type"]*9+["frame_type_typeR"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["frame_type_left"]+["N5"]+["frame_type_middle"]+["N6"]+["frame_type_middle"]+["N7"]+["frame_type_middle"]+["N8"]+["frame_type_middle"]+["N9"]+["frame_type_right"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["corner_type_leftD"]+["frame_type_bottom"]*9+["corner_type_rightD"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["corner_game_left"]+["frame_game_top"]*9+["corner_game_right"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["filler"]*3+["frame_game_left"]+["T"]+["O"]+["P"]+["-"]+["S"]+["C"]+["O"]+["R"]+["E"]+["frame_game_right"]+["filler"]*4+["frame_top90"],
        ["frame_top270"]+["corner_type_leftU"]+["frame_type_top"]*2+["corner_game_typeL"]+["frame_game_type"]*9+["corner_game_typeR"]+["frame_type_top"]*3+["corner_type_rightU"]+["frame_top90"],
        ["frame_top270"]+["frame_type_left"]+["N1"]+["frame_type_middle"]+["dot"]*6+["0"]*2+["dot"]*6+["frame_type_right"]+["frame_top90"],
        ["frame_top270"]+["frame_type_left"]+["N2"]+["frame_type_middle"]+["dot"]*6+["0"]*2+["dot"]*6+["frame_type_right"]+["frame_top90"],
        ["frame_top270"]+["frame_type_left"]+["N3"]+["frame_type_middle"]+["dot"]*6+["0"]*2+["dot"]*6+["frame_type_right"]+["frame_top90"],
        ["frame_top270"]+["corner_type_leftD"]+["frame_type_bottom"]*2+["frame_type_bottom"]*11+["frame_type_bottom"]*3+["corner_type_rightD"]+["frame_top90"],
        ["corner_top270"]+["frame_top180"]*18+["corner_top180"]
        ]
    GameBackground = [
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_r1_corner"]+["score_topline"]*5+["score_corner_top"],  
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r2"]+["S"]+["C"]+["O"]+["R"]+["E"]+["score_right_frame"],    
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r3"]+["score_bottom_frame"]*5+["score_corner_frame"],
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["0"]*7,                     
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r5"]+["score_bottomline"]*6,          
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r1_corner"]+["score_topline"]*5+["score_corner_top"], 
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_r7"]+["L"]+["E"]+["V"]+["E"]+["L"]+["score_rightline"],   
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r7"]+["0"]*5+["score_rightline"],
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r9"]+["score_dobleline"]*5+["score_corner_doble"],
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_r7"]+["L"]+["I"]+["N"]+["E"]+["S"]+["score_rightline"],
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_r7"]+["0"]*5+["score_rightline"],
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_r12_corner"]+["score_bottomline"]*5+["score_corner_bottom"],
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_right"]+["next_piece_corner"]+["next_piece_line"]*4+["next_piece_corner90"],
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        ["frame_left"]+["bricks_1"]+["0"]*10+["bricks_1"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        ["frame_left"]+["bricks_2"]+["0"]*10+["bricks_2"]+["frame_right"]+["next_piece_line270"]+["0"]*4+["next_piece_line90"],
        ["frame_left"]+["bricks_3"]+["0"]*10+["bricks_3"]+["frame_right"]+["next_piece_corner270"]+["next_piece_line180"]*4+["next_piece_corner180"],
    ]

    VictoryBackground = [
        [f"tile_{row * 20 + col:03d}" for col in range(20)]
        for row in range(18)
    ]

    def draw_screen(grid, screen, settings, tiles):
            for row_index, row in enumerate(grid):
                y = row_index * settings.tile_size * settings.scale
                for col_index, tile_name in enumerate(row):
                    x = col_index * settings.tile_size * settings.scale
                    tiles.draw_tile(tile_name, x, y, screen)