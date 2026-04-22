import pygame

# --- LOGICAL GB CONSTANTS ---
TILES_X = 20
TILES_Y = 18
TILE_SIZE = 8

LOGICAL_WIDTH = TILES_X * TILE_SIZE   # 160
LOGICAL_HEIGHT = TILES_Y * TILE_SIZE  # 144

OUTPUT_FILE = "extracted_tiles.py"

GB_PALETTE = {
    0: (255, 215, 154),  # background / beige
    1: (116, 198, 196),  # light blue
    2: (255, 99, 42),    # orange
    3: (49, 75, 98),     # dark blue
}


def closest_gb_colour(colour):
    r, g, b, a = colour

    best_index = 0
    best_distance = float("inf")

    for index, (pr, pg, pb) in GB_PALETTE.items():
        dist = (r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2
        if dist < best_distance:
            best_distance = dist
            best_index = index

    return best_index


def main():
    pygame.init()
    pygame.display.set_mode((1, 1))

    image = pygame.image.load("Rocket.png").convert_alpha()
    img_width, img_height = image.get_size()

    # ✅ AUTO-DETECT SCALE
    scale_x = img_width // LOGICAL_WIDTH
    scale_y = img_height // LOGICAL_HEIGHT

    print(f"Detected scale: {scale_x}x{scale_y}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Auto-generated GB tiles (scale-aware)\n\n")
        f.write("tiles = {\n")

        tile_id = 0

        for tile_y in range(TILES_Y):
            for tile_x in range(TILES_X):
                f.write(f'    "tile_{tile_id:03d}": [\n')

                for py in range(TILE_SIZE):
                    row = []
                    for px in range(TILE_SIZE):

                        # ✅ Map logical pixel → real pixel
                        real_x = (tile_x * TILE_SIZE + px) * scale_x + scale_x // 2
                        real_y = (tile_y * TILE_SIZE + py) * scale_y + scale_y // 2

                        colour = image.get_at((real_x, real_y))
                        row.append(closest_gb_colour(colour))

                    f.write(f"        {row},\n")

                f.write("    ],\n\n")
                tile_id += 1

        f.write("}\n")

    pygame.quit()
    print(f"Extracted {tile_id} tiles (expected 360)")


if __name__ == "__main__":
    main()