import pygame
from screens.tetrominos import Tetromino
from screens.screen_utilities import ScreenUtilities

class GameLoop:
    def __init__(self, screen, settings, tiles, starting_level, music, sfx):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.music = music
        self.sfx = sfx
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(self.settings.gamecolumns)] for _ in range(self.settings.rows)]
        # Score       
        self.game_mode = "TypeA" 
        self.score = 0
        self.level = starting_level
        self.lines_cleared = 0
        # Create two first tetrominos
        self.current_tetromino = Tetromino(screen, settings, tiles, starting_level)
        self.next_tetromino = Tetromino(screen, settings, tiles, starting_level)  
        # Movement repeat timing (ms)
        self.move_delay = 100       
        self.last_move_time = 0    
        # Clear rows animation
        self.state = "falling"              
        self.cleared_rows = []
        self.line_clear_blinks = 0         
        self.max_blinks = 7                
        self.blink_interval = 100          
        self.last_blink_time = 0
 
    def draw_locked_grid(self):
        for r in range(self.settings.rows):
            for c in range(self.settings.gamecolumns):
                cell = self.grid[r][c]
                if cell == 0:
                    continue  

                if self.state == "line_clear" and r in self.cleared_rows:
                    blink = self.line_clear_blinks
                    if blink > 5:
                        continue
                    elif blink in (1, 3, 5):
                        tile_name = cell
                    elif blink in (0, 2, 4):
                        tile_name = "1"
                else:
                    tile_name = self.grid[r][c]

                x_offset = (c + self.settings.x_offset) * self.settings.tile_size * self.settings.scale
                y_offset = r * self.settings.tile_size * self.settings.scale
                self.tiles.draw_tile(tile_name, x_offset, y_offset, self.screen)
            
    def detect_full_rows(self):
        full_rows = []
        for r, row in enumerate(self.grid):
            if all(cell != 0 for cell in row):
                full_rows.append(r)
        return full_rows

    def update_line_clear(self, current_time):
        if current_time - self.last_blink_time >= self.blink_interval:
            self.last_blink_time = current_time

            self.line_clear_blinks += 1

            if self.line_clear_blinks >= self.max_blinks:
                self.finish_line_clear()

    def finish_line_clear(self):
        self.clear_full_rows()

        self.sfx.play_tetro_lock()
        self.cleared_rows = []
        self.show_cleared_rows = True
        self.line_clear_blinks = 0

        self.state = "falling"
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = Tetromino(self.screen, self.settings, self.tiles, self.level)

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

        if self.current_tetromino.soft_drop_distance > 0:
            self.score += self.current_tetromino.soft_drop_distance * 1
        if self.current_tetromino.hard_drop_distance > 0:
            self.score += self.current_tetromino.hard_drop_distance * 2
    
    def draw_number_tiles(self, number, right_col, row):
        for i, digit in enumerate(reversed(str(number))):
            col = right_col - i
            x = col * self.settings.tile_size * self.settings.scale
            y = row * self.settings.tile_size * self.settings.scale
            #Changes number into tile and draws it
            self.tiles.draw_tile(f"N{digit}", x, y, self.screen)

    def draw_stats(self):
        right_col = 17    
        score_row = 3
        level_row = 7
        lines_row = 10

        self.draw_number_tiles(self.score, right_col, score_row)
        self.draw_number_tiles(self.level, right_col, level_row)
        self.draw_number_tiles(self.lines_cleared, right_col, lines_row)

    def run(self):
        running = True

        while running:
            events = pygame.event.get()
            current_time = pygame.time.get_ticks()

            ScreenUtilities.draw_screen( ScreenUtilities.GameBackground, self.screen, self.settings, self.tiles )
            self.draw_locked_grid()
            self.draw_stats()
            self.next_tetromino.draw_next(next_x=15, next_y=13)

            for event in events:
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:                 
                    if event.key in (pygame.K_ESCAPE, pygame.K_p):
                        from screens.pause import PauseScreen
                        result = PauseScreen(self.screen, self.settings, self.tiles).run()

                        if result != "resume":
                            return "quit"

            # --- STATE: FALLING (normal gameplay) ---
            if self.state == "falling":
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.current_tetromino.rotate(self.grid)
                        elif event.key == pygame.K_SPACE:
                            self.current_tetromino.hard_drop(self.grid)

                pressed = pygame.key.get_pressed()
                if current_time - self.last_move_time > self.move_delay:
                    if pressed[pygame.K_LEFT]:
                        self.current_tetromino.move_left(self.grid)
                        self.last_move_time = current_time
                        self.sfx.play_blip()
                    elif pressed[pygame.K_RIGHT]:
                        self.current_tetromino.move_right(self.grid)
                        self.last_move_time = current_time
                        self.sfx.play_blip()
                    elif pressed[pygame.K_DOWN]:
                        self.current_tetromino.soft_drop(self.grid)
                        self.last_move_time = current_time
                        self.sfx.play_blip()

                self.current_tetromino.move_down(self.grid)
                self.current_tetromino.draw()

                if self.current_tetromino.landed:
                    if self.current_tetromino.lock_tetromino(self.grid) == "Game Over":
                        return "game_over", {"score": self.score, "mode": self.game_mode}
                
                    self.cleared_rows = self.detect_full_rows()

                    if self.cleared_rows:
                        self.rows_cleared = len(self.cleared_rows)
                        self.sfx.play_line_clear()
                        self.add_score()
                        self.state = "line_clear"
                        self.show_cleared_rows = True
                        self.line_clear_blinks = 0
                        self.last_blink_time = current_time
                    else:
                        self.sfx.play_tetro_lock()
                        self.rows_cleared = 0
                        self.add_score()
                        self.current_tetromino = self.next_tetromino
                        self.next_tetromino = Tetromino(self.screen, self.settings, self.tiles, self.level)
                    
            # --- STATE: LINE_CLEAR (blinking full rows) ---
            elif self.state == "line_clear":
                self.update_line_clear(current_time)

            pygame.display.flip()