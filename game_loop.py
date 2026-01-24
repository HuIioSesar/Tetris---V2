import pygame
from screens.game_background import GameBackgroundScreen
from screens.tetrominos import Tetromino

class GameLoop:
    def __init__(self, screen, settings, tiles, starting_level):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.background = GameBackgroundScreen(screen, settings, tiles)
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(self.settings.gamecolumns)] for _ in range(self.settings.rows)]
        # Score        
        self.score = 0
        self.level = starting_level
        self.lines_cleared = 0
        # Create two first tetrominos
        self.current_tetromino = Tetromino(screen, settings, tiles, starting_level)
        self.next_tetromino = Tetromino(screen, settings, tiles, starting_level)   
    
    def draw_locked_grid(self):
        for r in range(self.settings.rows):
            for c in range(self.settings.gamecolumns):
                if self.grid[r][c] != 0:  # If cell is occupied
                    tile_name = self.grid[r][c]  # This stores the tetromino tile key
                    x_offset = (c + self.settings.x_offset) * self.settings.tile_size * self.settings.scale
                    y_offset = r * self.settings.tile_size * self.settings.scale
                    self.tiles.draw_tile(tile_name, x_offset, y_offset, self.screen)

    def clear_full_rows(self):
        new_grid = []
        self.rows_cleared = 0

        for row in self.grid:
            if all(cell != 0 for cell in row):
                self.rows_cleared += 1
            else:
                new_grid.append(row)
        for _ in range(self.rows_cleared):
            new_grid.insert(0, [0 for _ in range(self.settings.gamecolumns)])

        self.grid = new_grid

    def add_score(self):
        points = {1: 40, 2: 100, 3: 300, 4: 1200}
        if self.rows_cleared > 0:
            self.score += points.get(self.rows_cleared, 0) * (self.level + 1)
            self.lines_cleared += self.rows_cleared

            if self.lines_cleared >= (self.level + 1) * 10:
                self.level += 1
        print(self.score, self.level,self.lines_cleared)
    
    def number_to_tiles(self, number):
        # Convert number to string
        num_str = str(number)
        return [f"N{digit}" for digit in num_str]
    
    def draw_number_tiles(self, tile_keys, right_col, row):
        for i, tile_key in enumerate(reversed(tile_keys)):
            col = right_col - i
            x = col * self.settings.tile_size * self.settings.scale
            y = row * self.settings.tile_size * self.settings.scale
            self.tiles.draw_tile(tile_key, x, y, self.screen)

    def draw_stats(self):
        # position score on grid
        right_col = 17    
        score_row = 3
        level_row = 7
        lines_row = 10
        self.draw_number_tiles(self.number_to_tiles(self.score), right_col, score_row)
        self.draw_number_tiles(self.number_to_tiles(self.level), right_col, level_row)
        self.draw_number_tiles(self.number_to_tiles(self.lines_cleared), right_col, lines_row)

    def run(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "options2"  # Go back to previous menu
            
            # Draw background
            self.background.draw_screen()
            self.draw_locked_grid()

            # Draw current tetromino
            self.current_tetromino.draw()
            self.next_tetromino.draw_next(next_x=15, next_y=13)
            self.draw_stats()
            self.current_tetromino.move_down(self.grid)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_tetromino.move_left(self.grid)
                    elif event.key == pygame.K_RIGHT:
                        self.current_tetromino.move_right(self.grid)
                    elif event.key == pygame.K_DOWN:
                        self.current_tetromino.soft_drop(self.grid)
                    elif event.key == pygame.K_UP:
                        self.current_tetromino.rotate()
            
            if self.current_tetromino.landed:
                result = self.current_tetromino.lock_tetromino(self.grid)
                if result == "Game Over":
                    return "game_over"  # Or trigger a game over screen later
                else:
                    self.clear_full_rows()
                    self.add_score()
                    self.current_tetromino = self.next_tetromino
                    self.next_tetromino = Tetromino(self.screen, self.settings, self.tiles, self.level)  

            # Update display
            pygame.display.flip()

                    



# score = 0
# lines_cleared = 0
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# frame_count = 0
# fall_speed = 48


# # Check full rows and clear them



# #Score
# def add_score(rows):
#     global score, current_level
#     points = {1: 40, 2: 100, 3: 300, 4: 1200}
#     score += points.get(rows, 0) * (current_level + 1)


# #Dibujar main
# def draw_tile(tile, x_offset, y_offset, screen, GB_colours, TILE_SIZE, SCALE):
#     for row in range(TILE_SIZE):
#         for col in range(TILE_SIZE):
#             value = tile[row][col]  # valor numérico del píxel
#             color = GB_colours.get(value, (0, 0, 0))  # color RGB, negro si no existe
#             pygame.draw.rect(screen, color, (
#                 x_offset + col * SCALE,
#                 y_offset + row * SCALE,
#                 SCALE,
#                 SCALE
#             ))


# #Definimos las clase tetromino (draw, colisions, landed, etc)
# class Tetromino:
    
#     def __init__(self, shape, tile_key, starting_level):
#         self.shape = shape
#         self.tile_key = tile_key
#         self.row = 0
#         self.col = GAME_COLUMNS // 2 - len(shape[0]) // 2  # Start in the middle
#         self.last_fall_time = pygame.time.get_ticks()  # Track time for falling
#         self.landed = False  # Checks if piece has landed
#         self.current_level = starting_level
        
    
#     def draw(self):
#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     # Calculate pixel position based on tile system
#                     x_offset = (self.col + c + 2) * TILE_SIZE * SCALE # +2 so it's on the third column of the background
#                     y_offset = (self.row + r) * TILE_SIZE * SCALE

#                     # Get the correct tile pattern for this tetromino type
#                     tile_pattern = tiles_tetros[self.tile_key]

#                     # Draw the tile using your function
#                     draw_tile(tile_pattern, x_offset, y_offset, screen, GB_colours, TILE_SIZE, SCALE)

#     #checks if at the bottom or collision with other piece
#     def check_collision(self, target_row, target_col):
#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     new_r = target_row + r
#                     new_c = target_col + c
#                     # Check if it's outside the bottom or left and right walls
#                     if new_r >= ROWS or new_c < 0 or new_c >= GAME_COLUMNS:
#                         return True
#                     # Check if cell is occupied
#                     if grid[new_r][new_c] is not 0:
#                         return True
#         return False

#     #lock tetromino if bottom or touching a previous piec
#     def lock_tetromino(self):
#         global grid, game_over_flag

#         #Check if piece is above the top
#         # piece_above_top = False
        
#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     grid[self.row + r][self.col + c] = self.tile_key
#                     if self.row + r <= 0:
#                         game_over_flag = True
                        
#         self.clear_full_rows()

#     def clear_full_rows(self):
#         global grid, score, lines_cleared
#         new_grid = []
#         rows_cleared = 0

#         for row in grid:
#             if all(cell != 0 for cell in row):
#                 rows_cleared += 1
#             else:
#                 new_grid.append(row)

#         for _ in range(rows_cleared):
#             new_grid.insert(0, [0 for _ in range(GAME_COLUMNS)])

#         grid = new_grid

#         # Update stats
#         if rows_cleared > 0:
#             lines_cleared += rows_cleared
#             add_score(rows_cleared)

#             # Level up every 10 lines
#             self.current_level = self.current_level + lines_cleared // 10
#             print(score,lines_cleared,self.current_level)
        
        
    
#     #def rotation
#     def rotate(self):
#         rotated_shape = [list(row) for row in zip(*self.shape[::-1])]  # Rotate the shape
#         self.shape = rotated_shape  # Update the shape

#     #def movement
#     def move_down(self):        
#         current_time = pygame.time.get_ticks() 

#         fall_speed = max(13, 48 - self.current_level * 5)
#         # Convert frames to milliseconds
#         fall_speed_ms = fall_speed * (1000 // 60) 

#         if current_time - self.last_fall_time > fall_speed_ms:
            
#             # Use the check_collision function instead of repeating the logic
#             if not self.check_collision(self.row + 1, self.col):
#                 self.row += 1
#             else:
#                 self.landed = True
#                 self.lock_tetromino()

#             self.last_fall_time = current_time


# # Function to create a new Tetromino
# def new_tetromino():
#         shape, tile_key = random.choice(SHAPES)
#         return Tetromino(shape, tile_key)

# current_tetromino = new_tetromino()


# #draws background for game area
# def draw_game_area(screen, GB_colours, TILE_SIZE, SCALE):
#     game_width = GAME_COLUMNS * TILE_SIZE * SCALE
#     game_height = ROWS * TILE_SIZE * SCALE
#     pygame.draw.rect(screen, GB_colours.get(0), (2 * TILE_SIZE * SCALE, 0, game_width, game_height)) # *2 so it's on the third column of the background



# #drea locked tetros
# def draw_locked_grid(screen, grid, GB_colours, TILE_SIZE, SCALE):
#     for r in range(ROWS):
#         for c in range(GAME_COLUMNS):
#             if grid[r][c] != 0:  
#                 tile_pattern = tiles_tetros[grid[r][c]] 
#                 x_offset = (c + 2) * TILE_SIZE * SCALE # +2 so it's on the third column of the background
#                 y_offset = r * TILE_SIZE * SCALE
#                 draw_tile(tile_pattern, x_offset, y_offset, screen, GB_colours, TILE_SIZE, SCALE)


# # el juego si consigo que funcione
# def game(screen, GB_colours, TILE_SIZE, SCALE, starting_level=0):
#     global current_tetromino, game_over_flag

#     running = True
#     while running:

#         # GAME RUNNING STATE
#         if not game_over_flag:
#             # Background + Grid
#             draw_game_area(screen, GB_colours, TILE_SIZE, SCALE)
#             draw_locked_grid(screen, grid, GB_colours, TILE_SIZE, SCALE)
#             current_tetromino.draw()
#             # # Smooth movement if holding keys
#             # keys = pygame.key.get_pressed()
#             # if current_time - last_move_time > move_delay:
#             #     if keys[pygame.K_LEFT]:
#             #         current_tetromino.move_left()
#             #         last_move_time = current_time
#             #     elif keys[pygame.K_RIGHT]:
#             #         current_tetromino.move_right()
#             #         last_move_time = current_time
#             #     elif keys[pygame.K_DOWN]:
#             #         current_tetromino.move_kdown()
#             #         last_move_time = current_time

#             # Move current tetromino down automatically
#             current_tetromino.move_down()

#             # If it landed, lock and spawn new
#             if current_tetromino.landed:
#                 current_tetromino = new_tetromino()
            
#         pygame.display.flip()

