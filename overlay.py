import pygame
from settings import *


class Overlay1:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.health_surf_length = (player.health / player.max_health) * HEALTH_BAR_WIDTH
        self.cooldown_surf_length = (player.cooldown_runtime / player.skill_cooldown_time) * COOLDOWN_BAR_WIDTH
        overlay_path = OVERLAY_PATH
        self.skills_surf = {
            skill: pygame.image.load(f'{overlay_path}{skill}.png').convert_alpha() for skill in player.skills
        }

    def display(self, player):
        # Display skills
        skill_surf = self.skills_surf[self.player.selected_skill]
        self.health_surf_length = (player.health / player.max_health) * HEALTH_BAR_WIDTH
        self.cooldown_surf_length = (player.cooldown_runtime / player.skill_cooldown_time) * COOLDOWN_BAR_WIDTH

        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (SKILL_OVERLAY_X-1, SKILL_OVERLAY_Y-1, SKILL_OVERLAY_X+2, SKILL_OVERLAY_Y+2))

        self.display_surface.blit(skill_surf, (SKILL_OVERLAY_X, SKILL_OVERLAY_Y))
        # Display Health
        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (HEALTH_OVERLAY_X-2, HEALTH_OVERLAY_Y-1, HEALTH_BAR_WIDTH+4, HEALTH_BAR_HEIGHT+2))

        pygame.draw.rect(self.display_surface,
                         (0, 0, 0),
                         (HEALTH_OVERLAY_X-1, HEALTH_OVERLAY_Y, HEALTH_BAR_WIDTH+2, HEALTH_BAR_HEIGHT))

        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (HEALTH_OVERLAY_X, HEALTH_OVERLAY_Y+1, self.health_surf_length, HEALTH_BAR_HEIGHT-2))

        pygame.draw.line(
            self.display_surface,
            (255, 255, 255),
            (self.health_surf_length+HEALTH_OVERLAY_X+1, HEALTH_BAR_HEIGHT-1),
            (self.health_surf_length+HEALTH_OVERLAY_X+1, HEALTH_OVERLAY_Y+HEALTH_BAR_HEIGHT-1),
            1)
        # Display Cooldown
        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (COOLDOWN_OVERLAY_X-2, COOLDOWN_OVERLAY_Y-1, COOLDOWN_BAR_WIDTH+4, COOLDOWN_BAR_HEIGHT+2))

        pygame.draw.rect(self.display_surface,
                         (0, 0, 0),
                         (COOLDOWN_OVERLAY_X-1, COOLDOWN_OVERLAY_Y, COOLDOWN_BAR_WIDTH+2, COOLDOWN_BAR_HEIGHT))

        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (COOLDOWN_OVERLAY_X, COOLDOWN_OVERLAY_Y+1, self.cooldown_surf_length, COOLDOWN_BAR_HEIGHT-2))

        pygame.draw.line(
            self.display_surface,
            (255, 255, 255),
            (self.cooldown_surf_length+COOLDOWN_OVERLAY_X+1, COOLDOWN_OVERLAY_Y-1),
            (self.cooldown_surf_length+COOLDOWN_OVERLAY_X+1, COOLDOWN_OVERLAY_Y+COOLDOWN_BAR_HEIGHT-1),
            1)
        
        
class Overlay2:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.health_surf_length = (player.health / player.max_health) * HEALTH_BAR_WIDTH
        self.cooldown_surf_length = (player.cooldown_runtime / player.skill_cooldown_time) * COOLDOWN_BAR_WIDTH
        overlay_path = OVERLAY_PATH
        self.skills_surf = {
            skill: pygame.image.load(f'{overlay_path}{skill}.png').convert_alpha() for skill in player.skills
        }

    def display(self, player):
        # Display skills
        skill_surf = self.skills_surf[self.player.selected_skill]
        self.health_surf_length = (player.health / player.max_health) * HEALTH_BAR_WIDTH
        self.cooldown_surf_length = (player.cooldown_runtime / player.skill_cooldown_time) * COOLDOWN_BAR_WIDTH

        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (SCREEN_WIDTH/2 + SKILL_OVERLAY_X-1,
                          SKILL_OVERLAY_Y-1, SKILL_OVERLAY_X+2, SKILL_OVERLAY_Y+2))

        self.display_surface.blit(skill_surf, (SCREEN_WIDTH/2 + SKILL_OVERLAY_X, SKILL_OVERLAY_Y))
        # Display Health
        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (SCREEN_WIDTH/2 + HEALTH_OVERLAY_X-2,
                          HEALTH_OVERLAY_Y-1,
                          HEALTH_BAR_WIDTH+4,
                          HEALTH_BAR_HEIGHT+2))

        pygame.draw.rect(self.display_surface,
                         (0, 0, 0),
                         (SCREEN_WIDTH/2 + HEALTH_OVERLAY_X-1,
                          HEALTH_OVERLAY_Y,
                          HEALTH_BAR_WIDTH+2,
                          HEALTH_BAR_HEIGHT))

        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (SCREEN_WIDTH/2 + HEALTH_OVERLAY_X,
                          HEALTH_OVERLAY_Y+1,
                          self.health_surf_length,
                          HEALTH_BAR_HEIGHT-2))

        pygame.draw.line(
            self.display_surface,
            (255, 255, 255),
            (self.health_surf_length+SCREEN_WIDTH/2 + HEALTH_OVERLAY_X+1,
             HEALTH_BAR_HEIGHT-1),
            (self.health_surf_length+SCREEN_WIDTH/2 + HEALTH_OVERLAY_X+1,
             HEALTH_OVERLAY_Y+HEALTH_BAR_HEIGHT-1),
            1)
        # Display Cooldown
        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (SCREEN_WIDTH/2 + COOLDOWN_OVERLAY_X-2,
                          COOLDOWN_OVERLAY_Y-1,
                          COOLDOWN_BAR_WIDTH+4,
                          COOLDOWN_BAR_HEIGHT+2))

        pygame.draw.rect(self.display_surface,
                         (0, 0, 0),
                         (SCREEN_WIDTH/2 + COOLDOWN_OVERLAY_X-1,
                          COOLDOWN_OVERLAY_Y,
                          COOLDOWN_BAR_WIDTH+2,
                          COOLDOWN_BAR_HEIGHT))

        pygame.draw.rect(self.display_surface,
                         (255, 255, 255),
                         (SCREEN_WIDTH/2 + COOLDOWN_OVERLAY_X,
                          COOLDOWN_OVERLAY_Y+1,
                          self.cooldown_surf_length,
                          COOLDOWN_BAR_HEIGHT-2))

        pygame.draw.line(
            self.display_surface,
            (255, 255, 255),
            (self.cooldown_surf_length+SCREEN_WIDTH/2 + COOLDOWN_OVERLAY_X+1,
             COOLDOWN_OVERLAY_Y-1),
            (self.cooldown_surf_length+SCREEN_WIDTH/2 + COOLDOWN_OVERLAY_X+1,
             COOLDOWN_OVERLAY_Y+COOLDOWN_BAR_HEIGHT-1),
            1)
