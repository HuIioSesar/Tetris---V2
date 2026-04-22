
import pygame

class PauseScreen:
    def __init__(self, screen, settings, tiles):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles

        # Pause grid layout
        self.grid = [
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*3+["H"]+["I"]+["T"]+["0"]*4,
            ["0"]*3+["Go_underline"]*3+["0"]*4,
            ["0"]*2+["S"]+["T"]+["A"]+["R"]+["T"]+["0"]*3,
            ["0"]*2+["Go_underline"]*5+["0"]*3,
            ["0"]*4+["T"]+["O"]+["0"]*4,
            ["0"]*4+["Go_underline"]*2+["0"]*4,
            ["0"]*1+["C"]+["O"]+["N"]+["T"]+["I"]+["N"]+["U"]+["E"]+["0"]*1,
            ["0"]*1+["Go_underline"]*8+["0"]*1,
            ["0"]*3+["G"]+["A"]+["M"]+["E"]+["0"]*3,
            ["0"]*3+["Go_underline"]*4+["0"]*3,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
        ]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_p, pygame.K_ESCAPE):
                        return "resume"

            # Draw the grid
            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    tile = self.grid[row][col]
                    x = (col + self.settings.x_offset) * self.settings.tile_size * self.settings.scale
                    y = row * self.settings.tile_size * self.settings.scale
                    self.tiles.draw_tile(tile, x, y, self.screen)

            pygame.display.flip()
