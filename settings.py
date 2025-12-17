class Settings:
    def __init__(self):
        # Scaling
        self.scale = 5
        self.tile_size = 8

        # Grid dimensions
        self.columns = 20
        self.rows = 18

        # Screen size (derived)
        self.width = self.columns * self.tile_size * self.scale
        self.height = self.rows * self.tile_size * self.scale

        # Timing
        self.fps = 60

        # Game Boy color palette
        self.gb_colours = {
            0: (255, 215, 154),  # background / beige
            1: (116, 198, 196),  # light blue
            2: (255, 99, 42),    # orange
            3: (49, 75, 98)      # dark blue
        }