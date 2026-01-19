class Settings:
    def __init__(self):
        # Scaling
        self.scale = 5
        self.tile_size = 8

        # Grid dimensions
        self.columns = 20
        self.rows = 18
        self.gamecolumns = 10
        self.x_offset = 2
        self.box_next = 4 #Next piece box

        # Screen size (derived)
        self.width = self.columns * self.tile_size * self.scale
        self.height = self.rows * self.tile_size * self.scale

        # Timing
        self.fps = 60

        # Speed
        self.max_speed = 6
        self.min_speed = 30 #48 valor original
        self.speed_increase = 5

        # Game Boy color palette
        self.gb_colours = {
            0: (255, 215, 154),  # background / beige
            1: (116, 198, 196),  # light blue
            2: (255, 99, 42),    # orange
            3: (49, 75, 98)      # dark blue
        }

        # Tetromino shape
        self.tetromino = [
            ([[1, 1, 1, 1]], "tetro_I"),           # I
            ([[1, 1, 1], [1, 0, 0]], "tetro_J"),   # J
            ([[1, 1, 1], [0, 0, 1]], "tetro_L"),   # L
            ([[1, 1], [1, 1]], "tetro_O"),         # O
            ([[1, 1, 1], [0, 1, 0]], "tetro_T"),   # T
            ([[1, 1, 0], [0, 1, 1]], "tetro_S"),   # S
            ([[0, 1, 1], [1, 1, 0]], "tetro_Z"),   # Z
        ]