import pygame
from player import Player1, Player2
from bot import Bot1, Bot2
from settings import *
from overlay import Overlay1, Overlay2
from skills import Laser1, Laser2


class Level:

    def __init__(self):
        self.mode = None
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()

        self.player1 = None
        self.player2 = None
        self.overlay1 = None
        self.overlay2 = None
        self.laser1 = None
        self.laser2 = None

    def setup(self):
        if self.mode == "Combat":
            self.player1 = Player1((SCREEN_WIDTH/4, SCREEN_HEIGHT/4), self.all_sprites)
            self.player2 = Player2((3*SCREEN_WIDTH / 4, 3*SCREEN_HEIGHT / 4), self.all_sprites)
        elif self.mode == "Bot1":

            self.player1 = Bot1((SCREEN_WIDTH/4, SCREEN_HEIGHT/4), self.all_sprites)
            self.player2 = Player2((3*SCREEN_WIDTH / 4, 3*SCREEN_HEIGHT / 4), self.all_sprites)
        elif self.mode == "Bot2":
            self.player1 = Player1((SCREEN_WIDTH/4, SCREEN_HEIGHT/4), self.all_sprites)
            self.player2 = Bot2((3*SCREEN_WIDTH / 4, 3*SCREEN_HEIGHT / 4), self.all_sprites)
        elif self.mode == "BVB":
            self.player1 = Bot1((SCREEN_WIDTH/4, SCREEN_HEIGHT/4), self.all_sprites)
            self.player2 = Bot2((3*SCREEN_WIDTH / 4, 3*SCREEN_HEIGHT / 4), self.all_sprites)

        self.overlay1 = Overlay1(self.player1)
        self.laser1 = Laser1(self.player1)
        self.overlay2 = Overlay2(self.player2)
        self.laser2 = Laser2(self.player2)

    def reset(self):
        self.all_sprites.empty()
        self.__init__()

    def set_mode(self, mode):
        self.mode = mode

    def run(self, dt):
        self.display_surface.fill((0, 0, 0))
        self.all_sprites.draw(self.display_surface)
        self.player1.update(dt, self.player2)
        self.player2.update(dt, self.player1)
        self.overlay1.display(self.player1)
        self.laser1.draw(self.player1, self.player2, dt)
        self.overlay2.display(self.player2)
        self.laser2.draw(self.player2, self.player1, dt)
        pygame.display.flip()
