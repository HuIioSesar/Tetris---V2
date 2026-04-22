import pygame

class MusicManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None

    def play_music(self, musicpath, loop=True):
        if musicpath != self.current_track:
            pygame.mixer.music.load(musicpath)
            pygame.mixer.music.play(-1 if loop else 0)
            self.current_track = musicpath

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None
