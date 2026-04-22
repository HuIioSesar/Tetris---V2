import pygame
from utilities import ScoreManager

class GameOver:
    def __init__(self, screen, settings, tiles, music, sfx, game_payload):
        self.screen = screen
        self.settings = settings
        self.tiles = tiles
        self.sfx = sfx
        self.clock = pygame.time.Clock()

        self.grid = [["0" for _ in range(self.settings.gamecolumns)] 
                     for _ in range(self.settings.rows)]

        self.final_score = game_payload.get("score", 0)
        self.mode = game_payload.get("mode", "TypeA")

    # GAME OVER ANIMATION (no changes here)
    def play_game_over_animation(self):
        def draw_screen(self):
            for r, tile_row in enumerate(self.grid):
                for c, tile_name in enumerate(tile_row):
                    x = (c + self.settings.x_offset) * self.settings.tile_size * self.settings.scale
                    y = r * self.settings.tile_size * self.settings.scale
                    self.tiles.draw_tile(tile_name, x, y, self.screen)

        # Fill from bottom to top
        for row in range(self.settings.rows - 1, -1, -1):
            for col in range(self.settings.gamecolumns):
                self.grid[row][col] = "Go_block"
            draw_screen(self)
            pygame.display.flip()
            pygame.time.delay(30)

        # Clear from bottom to top
        for row in range(self.settings.rows - 1, -1, -1):
            for col in range(self.settings.gamecolumns):
                self.grid[row][col] = "0"
            draw_screen(self)
            pygame.display.flip()
            pygame.time.delay(30)

        # Final static GAME OVER screen
        self.grid = [
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*3+["G","A","M","E"]+["0"]*3,
            ["0"]*10,
            ["0"]*3+["O","V","E","R"]+["0"]*3,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]*10,
            ["0"]+["P","L","E","A","S","E"]+["0"]*3,
            ["0"]+["Go_underline"]*6+["0"]*3,
            ["0"]*2+["T","R","Y"]+["0"]*5,
            ["0"]*2+["Go_underline"]*3+["0"]*5,
            ["0"]*3+["A","G","A","I","N","Heart","0"],
            ["0"]*3+["Go_underline"]*5+["0"]*2,
        ]
        draw_screen(self)

    # MAIN LOOP
    def run(self):
        running = True

        self.play_game_over_animation()
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit", None

                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                        return "start", None

                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):

                        rank = ScoreManager.save_score(self.final_score, "", self.mode)

                        if rank is None:
                            return ("options2", {"name_entry": False,"mode": self.mode})

                        else:
                            return ("options2", {"name_entry": True,"rank": rank,"mode": self.mode})