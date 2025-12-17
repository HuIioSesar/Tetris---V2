# import pygame
# import random

# pygame.init()


# # Set the timer
# timer_duration = 0.05

# #screen
# screen_width = 400
# screen_height = 800

# #game window
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Tetris')

# #define variables
# cell_size = 40
# fall_speed = 500
# # globals
# move_delay = 100
# last_move_time = 0
# game_over_flag = False
# debug_mode = True
# score = 0
# lines_cleared = 0
# level = 0

# # Grid dimensions
# ROWS = screen_height // cell_size
# COLS = screen_width // cell_size

# # Create an empty grid filled with 0s
# grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# #define font
# font = pygame.font.SysFont("Arial", 30)
                 
# #define rectangle (play again)


# #define colours
# bg = (245, 222, 179)
# grid_col = (200, 170, 140)
# J_col = (100, 149, 237)
# L_col = (255, 140, 0)
# I_col = (175, 238, 238)
# O_col = (255, 239, 150)
# S_col = (144, 238, 144)
# Z_col = (240, 128, 128)
# T_col = (186, 85, 211)
# left_col = (233, 150, 122)
# left_out_col = (128,57,30)
# right_col = (135, 206, 250)
# right_out_col = (4,47,102)
# ball_col = (220, 240, 240)
# ball_out_col = (28,16,11)
# score_col = (100, 180, 200)


# #defin buttons
# again_rect = pygame.Rect(screen_width // 2 - 115 // 2, screen_height // 2 - 35 // 2, 135, 45)


# # Create tetromino class
# SHAPES = [
#     ([[1, 1, 1, 1]], I_col),           # I
#     ([[1, 1, 1], [1, 0, 0]], J_col),   # J
#     ([[1, 1, 1], [0, 0, 1]], L_col),   # L
#     ([[1, 1], [1, 1]], O_col),         # O
#     ([[1, 1, 1], [0, 1, 0]], T_col),   # T
#     ([[1, 1, 0], [0, 1, 1]], S_col),   # S
#     ([[0, 1, 1], [1, 1, 0]], Z_col),   # Z
# ]


#     # Check full rows and clear them
# def clear_full_rows():
#     global grid, score, lines_cleared, level
#     new_grid = []
#     rows_cleared = 0

#     for row in grid:
#         if all(cell != 0 for cell in row):
#             rows_cleared += 1
#         else:
#             new_grid.append(row)

#     for _ in range(rows_cleared):
#         new_grid.insert(0, [0 for _ in range(COLS)])

#     grid = new_grid

#     # Update stats
#     if rows_cleared > 0:
#         lines_cleared += rows_cleared
#         add_score(rows_cleared)

#         # Level up every 10 lines
#         level = lines_cleared // 10
#         print(score,lines_cleared,level)

# #Score
# def add_score(rows):
#     global score, level
#     points = {1: 40, 2: 100, 3: 300, 4: 1200}
#     score += points.get(rows, 0) * (level + 1)
        

# class Tetromino:
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#         self.row = 0
#         self.col = screen_width // (2 * cell_size) - len(shape[0]) // 2  # Start in the middle
#         self.last_fall_time = pygame.time.get_ticks()  # Track time for falling
#         self.landed = False  # Checks if piece has landed

#     def draw(self):
#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     pygame.draw.rect(screen, self.color, (self.col * cell_size + c * cell_size,
#                                                           self.row * cell_size + r * cell_size,
#                                                           cell_size, cell_size))
#                     pygame.draw.rect(screen, ball_col, (self.col * cell_size + c * cell_size,
#                                                      self.row * cell_size + r * cell_size,
#                                                      cell_size, cell_size), 2)

#     def check_collision(self, target_row, target_col):
#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     new_r = target_row + r
#                     new_c = target_col + c
#                     # Check if it's outside the bottom or overlapping another piece
#                     if new_r >= ROWS or new_c < 0 or new_c >= COLS or grid[new_r][new_c] != 0:
#                         return True
#         return False


#     # Save Tetromino position in the grid when it lands
#     def lock_tetromino(self):
#         global grid, game_over_flag

#         #Check if piece is above the top
#         piece_above_top = False
        
#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     grid[self.row + r][self.col + c] = self.color
#                     if self.row + r <= 0:
#                         game_over_flag = True
                        
#         clear_full_rows()
        
        
#     def move_left(self):
#         if self.col > 0:
#             self.col -= 1

#     def move_right(self):
#         if self.col + len(self.shape[0]) < screen_width // cell_size:
#             self.col += 1

#     def move_kdown(self):
#         #if self.row >= 0:
#         #    self.row += 1

#         #New movement checking collision
#         if not self.check_collision(self.row + 1, self.col):
#             self.row += 1
#         else:
#             self.landed = True
#             self.lock_tetromino()


#     #def rotation
#     def rotate(self):
#         rotated_shape = [list(row) for row in zip(*self.shape[::-1])]  # Rotate the shape
#         self.shape = rotated_shape  # Update the shape


#     # Define move down of tetromino
#     def move_down(self):        
#         current_time = pygame.time.get_ticks() 
#         if current_time - self.last_fall_time > fall_speed:
            
#             # Use the check_collision function instead of repeating the logic
#             if not self.check_collision(self.row + 1, self.col):
#                 self.row += 1
#             else:
#                 self.landed = True
#                 self.lock_tetromino()

#             self.last_fall_time = current_time
      
#     def draw_ghost(self):
#         ghost_row = self.row
#         while not self.check_collision(ghost_row + 1, self.col):
#             ghost_row += 1

#         for r in range(len(self.shape)):
#             for c in range(len(self.shape[r])):
#                 if self.shape[r][c] == 1:
#                     pygame.draw.rect(screen, (255, 242, 199), 
#                                      (self.col * cell_size + c * cell_size,
#                                       ghost_row * cell_size + r * cell_size,
#                                       cell_size, cell_size))
#                     pygame.draw.rect(screen, (175, 175, 175), 
#                                      (self.col * cell_size + c * cell_size,
#                                       ghost_row * cell_size + r * cell_size,
#                                       cell_size, cell_size), 2)


# # Function to create a new Tetromino
# def new_tetromino():
#         shape, color = random.choice(SHAPES)
#         return Tetromino(shape, color)

# # Create the first Tetromino
# current_tetromino = new_tetromino()


# #screen 
# def draw_screen():
#     screen.fill(bg) 
#     for x in range(0,screen_height // cell_size):
#         pygame.draw.line(screen, grid_col, (0, x * cell_size),(screen_width, x * cell_size))
#     for x in range(0,screen_width // cell_size):
#         pygame.draw.line(screen, grid_col, (x * cell_size, 0),(x * cell_size, screen_height))


# #score



# #game over
# def show_game_over():
#     if game_over_flag:

#         text = font.render("GAME OVER", True, (255, 0, 0))
#         subtext = font.render("Press R to restart or ESC to quit", True, (0, 0, 0))
#         screen.blit(text, (screen_width // 2 - 100, screen_height // 2 - 40))
#         screen.blit(subtext, (screen_width // 2 - 150, screen_height // 2 + 10))
#         pygame.display.update()


# #restart
# def restart_game():
#     global grid, current_tetromino, game_over_flag
#     grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
#     current_tetromino = new_tetromino()
#     game_over_flag = False

# #debug mode
# def draw_debug_overlay():
# # Highlight filled grid cells
#     for r in range(ROWS):
#         for c in range(COLS):
#             if grid[r][c] != 0:
#                 pygame.draw.rect(screen, (255, 255, 255), 
#                                  (c * cell_size, r * cell_size, cell_size, cell_size), 1)


# # Game loop
# clock = pygame.time.Clock()
# run = True

# print(score,lines_cleared,level)


# while run:
#     current_time = pygame.time.get_ticks()

#     #draw_tile(screen, menu, tiles, GB_colours, TILE_SIZE, SCALE)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         elif event.type == pygame.KEYDOWN:
#             # ACTIVE GAME CONTROLS
#             if not game_over_flag:
#                 if event.key == pygame.K_LEFT:
#                     current_tetromino.move_left()
#                     last_move_time = current_time
#                 elif event.key == pygame.K_RIGHT:
#                     current_tetromino.move_right()
#                     last_move_time = current_time
#                 elif event.key == pygame.K_DOWN:
#                     current_tetromino.move_kdown()
#                     last_move_time = current_time
#                 elif event.key in (pygame.K_SPACE, pygame.K_UP):
#                     current_tetromino.rotate()
#                 elif event.key == pygame.K_d:
#                     debug_mode = not debug_mode

#             # GAME OVER CONTROLS
#             else:
#                 if event.key == pygame.K_r:  # Restart
#                     restart_game()
#                 elif event.key == pygame.K_ESCAPE:
#                     run = False

#     # GAME RUNNING STATE
#     if not game_over_flag:
#         # Background + Grid
#         draw_screen()

#         # Smooth movement if holding keys
#         keys = pygame.key.get_pressed()
#         if current_time - last_move_time > move_delay:
#             if keys[pygame.K_LEFT]:
#                 current_tetromino.move_left()
#                 last_move_time = current_time
#             elif keys[pygame.K_RIGHT]:
#                 current_tetromino.move_right()
#                 last_move_time = current_time
#             elif keys[pygame.K_DOWN]:
#                 current_tetromino.move_kdown()
#                 last_move_time = current_time

#         # Move current tetromino down automatically
#         current_tetromino.move_down()

#         # If it landed, lock and spawn new
#         if current_tetromino.landed:
#             # The lock_tetromino() method should internally call check_game_over()
#             # If game over, game_over_flag becomes True
#             current_tetromino = new_tetromino()

#         # Draw all locked pieces from grid
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] != 0:
#                     pygame.draw.rect(screen, grid[r][c],
#                                      (c * cell_size, r * cell_size, cell_size, cell_size))

#         # Draw the active falling piece
#         current_tetromino.draw()
        
#         if debug_mode:
#             current_tetromino.draw_ghost()
#             draw_debug_overlay()
            

#     # GAME OVER STATE
#     else:
#         show_game_over()

#     pygame.display.update()
#     clock.tick(30)
