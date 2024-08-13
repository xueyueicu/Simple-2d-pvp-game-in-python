import pygame
import sys
from settings import *
from level import Level
from button import Button


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Laser Shooting')
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.button_combat = Button('Combat', SCREEN_WIDTH / 2-100, SCREEN_HEIGHT / 2 - 300, 200, 50, (255, 255, 255), (0, 255, 0), lambda: self.level.set_mode("Combat"))
        self.button_bot1 = Button('Bot1', SCREEN_WIDTH / 2-100, SCREEN_HEIGHT / 2 - 100, 200, 50, (255, 255, 255), (0, 255, 0), lambda: self.level.set_mode("Bot1"))
        self.button_bot2 = Button('Bot2', SCREEN_WIDTH / 2-100, SCREEN_HEIGHT / 2 + 100, 200, 50, (255, 255, 255), (0, 255, 0), lambda: self.level.set_mode("Bot2"))
        self.button_BVB = Button('BVB', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 300, 200, 50, (255, 255, 255),(0, 255, 0), lambda: self.level.set_mode("BVB"))
        self.start = False

    def set_up(self):
        self.button_combat = Button('Combat', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 300, 200, 50, (255, 255, 255),
                                    (0, 255, 0), lambda: self.level.set_mode("Combat"))
        self.button_bot1 = Button('Bot1', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 100, 200, 50, (255, 255, 255),
                                  (0, 255, 0), lambda: self.level.set_mode("Bot1"))
        self.button_bot2 = Button('Bot2', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 100, 200, 50, (255, 255, 255),
                                  (0, 255, 0), lambda: self.level.set_mode("Bot2"))
        self.button_BVB = Button('BVB', SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 300, 200, 50, (255, 255, 255),
                                  (0, 255, 0), lambda: self.level.set_mode("BVB"))
        self.start = False
        self.level.reset()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not self.start:
                        mouse_pos = pygame.mouse.get_pos()
                        self.button_combat.handle_click(mouse_pos)
                        self.button_bot1.handle_click(mouse_pos)
                        self.button_bot2.handle_click(mouse_pos)
                        self.button_BVB.handle_click(mouse_pos)
                        self.start = self.button_combat.handle_click(mouse_pos) or self.button_bot1.handle_click(mouse_pos) or self.button_bot2.handle_click(mouse_pos) or self.button_BVB.handle_click(mouse_pos)
                        if self.start:
                            self.level.setup()

            if self.start:
                self.level.run(dt)
            if not self.start:
                self.button_combat.draw(self.screen)
                self.button_bot1.draw(self.screen)
                self.button_bot2.draw(self.screen)
                self.button_BVB.draw(self.screen)
            pygame.display.update()
            winner = None
            if self.level.player1 and self.level.player2:
                winner = 'player2' if self.level.player1.health <= 0 else 'player1' if self.level.player2.health <= 0 else None
            if winner:
                self.level.display_surface.blit(pygame.font.Font(None, 50).render(f'{winner} wins!', True, (0, 255, 0)), (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50))
                pygame.display.update()
                pygame.time.wait(2000)
                self.screen.fill((0, 0, 0))
                self.set_up()


if __name__ == '__main__':
    game = Game()
    game.run()
