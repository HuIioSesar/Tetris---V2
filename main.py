import pygame
from settings import Settings
from tiles import Tiles
from screens.startscreen import StartScreen
from screens.options1 import Options1Screen
from screens.options2 import Options2Screen
# from screens.game_background import GameBackgroundScreen
from game_loop import GameLoop

def main():
    pygame.init()

    # Create settings and screen
    settings = Settings()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Tetris")

    # Shared Tiles object
    tiles = Tiles(settings.gb_colours, settings.tile_size, settings.scale)

    # Start with StartScreen
    current_screen = "start"
    starting_level = 0


    while current_screen != "quit":
        if current_screen == "start":
            next_screen = StartScreen(screen, settings, tiles).run()
        elif current_screen == "options1":
            next_screen = Options1Screen(screen, settings, tiles).run()
        elif current_screen == "options2":
            result = Options2Screen(screen, settings, tiles).run()
            if isinstance(result, tuple):
                next_screen, starting_level = result  # Unpack tuple
#que feo es el putas
            else:
                next_screen = result

        elif current_screen == "game":
            next_screen = GameLoop(screen, settings, tiles, starting_level).run()
        else:
            next_screen = "quit"

        current_screen = next_screen

    pygame.quit()

if __name__ == "__main__":
    main()









# import pygame
# from screens import menu, options1, options2, game_background
# import game_loop
# from screens.options1 import game_options, music_options, tiles_op1, selected_game_index, selected_music_index
# from screens.options2 import level_options, tiles_op2, selected_level_row, selected_level_col
# from game_loop import Tetromino


# pygame.init()
# SCALE = 5
# TILE_SIZE = 8
# COLUMNS = 20
# ROWS = 18
# WIDTH = COLUMNS * TILE_SIZE * SCALE
# HEIGHT = ROWS * TILE_SIZE * SCALE
# selected_level = 0
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# frame_count = 0
# clock = pygame.time.Clock()

# GB_colours = {
#     0: (255, 215, 154),
#     1: (116, 198, 196),
#     2: (255, 99, 42),
#     3: (49, 75, 98)
# }

# screen_state = "menu" 
# running = True
# clock.tick(60)

# while running:
#     frame_count += 1
#     # Determine blink state (True = dark colour, False = clear colour)
#     blink_on = (frame_count // 20) % 2 == 0

#     if screen_state == "menu":
#         menu.draw_menu(screen, GB_colours, TILE_SIZE, SCALE, blink_on)
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     screen_state = "options1"
#                     game_music_option = 1    #game 1 music 2
#                 # For closing the game later
#                 # elif evento.key == pygame.K_BACKSPACE:  
#                 #     screen_state = "close?"
#     elif screen_state == "options1":
#         options1.draw_options1(screen, GB_colours, TILE_SIZE, SCALE)
#         options1.draw_options1_selected(screen, GB_colours, TILE_SIZE, SCALE, tiles_op1, game_options, music_options, selected_game_index, selected_music_index, blink_on)
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if game_music_option == 1:
#                     if event.key == pygame.K_LEFT:
#                         selected_game_index = max(0, selected_game_index - 1)
#                     elif event.key == pygame.K_RIGHT:
#                         selected_game_index = min(len(game_options) - 1, selected_game_index + 1)
#                     elif event.key == pygame.K_RETURN:
#                         game_music_option = 2  # Move to music selection
#                     elif event.key == pygame.K_BACKSPACE:
#                         screen_state = "menu"  # Go back to previous screen
#                 elif game_music_option == 2:
#                     if event.key == pygame.K_LEFT:
#                         selected_music_index = max(0, selected_music_index - 1)
#                     elif event.key == pygame.K_RIGHT:
#                         selected_music_index = min(len(music_options) - 1, selected_music_index + 1)
#                     elif event.key == pygame.K_UP:
#                         selected_music_index = max(0, selected_music_index - 2)  # Move up by 2
#                     elif event.key == pygame.K_DOWN:
#                         selected_music_index = min(len(music_options) - 1, selected_music_index + 2)  # Move down by 2
#                     elif event.key == pygame.K_RETURN:
#                         screen_state = "options2"  # Move to next screen
#                     elif event.key == pygame.K_BACKSPACE:
#                         game_music_option = 1  # Go back to game type selection

#     elif screen_state == "options2":
#         options2.draw_options2(screen, GB_colours, TILE_SIZE, SCALE)
#         options2.draw_options2_selected(screen, GB_colours, TILE_SIZE, SCALE, tiles_op2, level_options, selected_level_row, selected_level_col, blink_on)
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:               
#                 if event.key == pygame.K_LEFT:
#                     selected_level_col = max(0, selected_level_col - 1)
#                 elif event.key == pygame.K_RIGHT:
#                     selected_level_col = min(len(level_options[selected_level_row]["tiles_op2"]) - 1, selected_level_col + 1)
#                 elif event.key == pygame.K_UP:
#                     selected_level_row = max(0, selected_level_row - 1)
#                 elif event.key == pygame.K_DOWN:
#                     selected_level_row = min(len(level_options) - 1, selected_level_row + 1)
#                 elif event.key == pygame.K_RETURN:
#                     starting_level = selected_level_row * len(level_options[0]["tiles_op2"]) + selected_level_col
#                     screen_state = "game"                     
#                 elif event.key == pygame.K_BACKSPACE:
#                     screen_state = "options1"  # Go back to previous screen

#     elif screen_state == "game":
#         game_background.draw_background(screen, GB_colours, TILE_SIZE, SCALE)
#         game_loop.game(screen, GB_colours, TILE_SIZE, SCALE, starting_level)
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 # if event.key == pygame.K_RETURN:
#                 #     screen_state = "game"  
#                 if event.key == pygame.K_BACKSPACE:
#                     screen_state = "options2"  # Go back to previous screen

# # Lista de pantallas en orden
# # pantallas = [menu, options1, options2, game_background]
# # indice_actual = 0

# # running = True
# # while running:
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             running = False
# #         elif evento.type == pygame.KEYDOWN:
# #             if evento.key == pygame.K_RETURN:  # Enter → siguiente pantalla
# #                 indice_actual = (indice_actual + 1) % len(pantallas)
# #             elif evento.key == pygame.K_BACKSPACE:  # Backspace → pantalla anterior
# #                 indice_actual = (indice_actual - 1) % len(pantallas)

# #     # Dibujar pantalla actual
# #     pantalla_activa = pantallas[indice_actual]
# #     pantalla_activa.draw(screen, GB_colours, TILE_SIZE, SCALE)
# #     if pantalla_activa == options1:
# #         pantalla_activa.draw_menu(screen, GB_colours, TILE_SIZE, SCALE, tiles, game_options, music_options, selected_game_index, selected_music_index)

#     pygame.display.flip()

# pygame.quit()