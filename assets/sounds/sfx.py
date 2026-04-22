import pygame

class SFXManager:
    def __init__(self):
        pygame.mixer.init()

        self.blip = pygame.mixer.Sound("assets/sounds/blip.wav")
        self.blip.set_volume(0.2)
        self.line_clear = pygame.mixer.Sound("assets/sounds/line_clear.wav")
        self.tetris_lock = pygame.mixer.Sound("assets/sounds/tetro_lock.wav")


    def play_blip(self):
        self.blip.play()

    def play_line_clear(self):
        self.line_clear.play()

    def play_tetro_lock(self):
         self.tetris_lock.play()
