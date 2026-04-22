import pygame
import random

class Tetromino:
    
    def __init__(self, screen, settings, tiles, starting_level):

        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.clock = pygame.time.Clock()

        # Pick a random tetromino
        self.shape, self.tile_key = random.choice(self.settings.tetromino)

        self.row = 0
        self.col = self.settings.gamecolumns // 2 - len(self.shape[0]) // 2 
        self.last_fall_time = pygame.time.get_ticks()  # Track time for falling
        self.landed = False  # Checks if piece has landed
        self.current_level = starting_level
        self.soft_drop_distance = 0
        self.hard_drop_distance = 0

        self.rotation_state = 0
        
    def draw(self):
        for r in range(len(self.shape)):
            for c in range(len(self.shape[r])):
                if self.shape[r][c] == 1:
                    # Calculate pixel position based on tile system
                    x = (self.col + c + self.settings.x_offset) * self.settings.tile_size * self.settings.scale # +2 so it's on the third column of the background
                    y = (self.row + r) * self.settings.tile_size * self.settings.scale
                    # Get the correct tile pattern for this tetromino type
                    self.tiles.draw_tile(self.tile_key, x, y, self.screen)
    
    def draw_next(self, next_x, next_y):
        for r in range(len(self.shape)):
            for c in range(len(self.shape[r])):
                if self.shape[r][c] == 1:
                    x = (next_x + ((self.settings.box_next - len(self.shape[0])) // 2) + c) * self.settings.tile_size * self.settings.scale
                    y = (next_y + ((self.settings.box_next - len(self.shape)) // 2) + r) * self.settings.tile_size * self.settings.scale
                    self.tiles.draw_tile(self.tile_key, x, y, self.screen)


    def move_down(self, grid):        
        current_time = pygame.time.get_ticks() 

        fall_speed = max(self.settings.max_speed, self.settings.min_speed - self.current_level * self.settings.speed_increase)
        fall_speed_ms = fall_speed * (1000 // 60) 

        if current_time - self.last_fall_time > fall_speed_ms:
            if not self.check_collision(grid, self.row + 1, self.col):
                self.row += 1
            else:
                self.landed = True
                result = self.lock_tetromino(grid)
                return result
            self.last_fall_time = current_time

    def move_left(self, grid):
        if not self.check_collision(grid, self.row, self.col - 1):
            self.col -= 1
    def move_right(self, grid):
        if not self.check_collision(grid, self.row, self.col + 1):
            self.col += 1
    def soft_drop(self, grid):
        if not self.check_collision(grid, self.row + 1, self.col):
            self.row += 1
            self.soft_drop_distance += 1
        else:
            self.landed = True
            self.lock_tetromino(grid)
    def hard_drop(self, grid):
        while not self.check_collision(grid, self.row + 1, self.col):
            self.row += 1
            self.hard_drop_distance += 1
        self.landed = True
        self.lock_tetromino(grid)

    def rotate(self, grid, direction=1):
        if direction != 1:
            direction = 1

        old_shape = self.shape
        old_state = self.rotation_state
        new_state = (self.rotation_state + 1) % 4

        rotated_shape = [list(row) for row in zip(*self.shape[::-1])]

        if self.tile_key == "tetro_I":
            kick_table = self.settings.srs_kicks_i
        elif self.tile_key == "tetro_O":
            kick_table = self.settings.srs_kicks_o
        else:
            kick_table = self.settings.srs_kicks_jlstz

        kicks = kick_table.get((old_state, new_state), [(0, 0)])

        for dx, dy in kicks:
            test_col = self.col + dx
            test_row = self.row + dy

            if not self.check_collision(grid, test_row, test_col, shape=rotated_shape):
                self.shape = rotated_shape
                self.col = test_col
                self.row = test_row
                self.rotation_state = new_state
                return

        self.shape = old_shape
        self.rotation_state = old_state
  
    def check_collision(self, grid, target_row, target_col, shape=None):
        if shape is None:
            shape = self.shape

        for r in range(len(shape)):
            for c in range(len(shape[r])):
                if shape[r][c] == 1:
                    new_r = target_row + r
                    new_c = target_col + c

                    # 1) Check vertical bounds (top and bottom)
                    if new_r < 0 or new_r >= self.settings.rows:
                        return True

                    # 2) Check horizontal bounds (left and right walls)
                    if new_c < 0 or new_c >= self.settings.gamecolumns:
                        return True

                    # 3) Check collision with locked blocks
                    if grid[new_r][new_c] != 0:
                        return True

        return False

    #lock tetromino if bottom or touching a previous piece  
    def lock_tetromino(self, grid):
        for r in range(len(self.shape)):
            for c in range(len(self.shape[r])):
                if self.shape[r][c] == 1:
                    grid[self.row + r][self.col + c] = self.tile_key
                    if self.row + r <= 0:
                        return "Game Over"
