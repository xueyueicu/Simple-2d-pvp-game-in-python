import random
import pygame
from settings import *


class Laser1:
    def __init__(self, player):
        self.player = player
        self.direction = self.player.direction
        self.activate = False
        self.image = pygame.image.load('graphics/laser/laser_usage.png').convert_alpha()
        self.x = int(player.pos.x)+16
        self.y = int(player.pos.y)-16
        self.rect = self.image.get_rect()
        self.display_surface = pygame.display.get_surface()
        self.damage_particles = {}
        self.damage_particles_key = 'a'

    def draw(self, player, target, dt):
        self.x = int(player.pos.x) + 16
        self.y = int(player.pos.y) - 16
        self.activate = player.skill_activated and player.selected_skill == 'laser'

        if self.activate:
            if self.y+45 > target.pos.y > self.y-15:
                target.health -= 0.2
                self.damage_particles[self.damage_particles_key] = Particle1((target.pos.x - 16, player.pos.y))
                self.damage_particles_key = chr(ord(self.damage_particles_key) + 1) if self.damage_particles_key != 'A' else 'a'
                for i in range(self.x, int(target.pos.x)-16, 1):
                    self.display_surface.blit(self.image, (i, self.y))

            else:
                for i in range(self.x, SCREEN_WIDTH, 1):
                    self.display_surface.blit(self.image, (i, self.y))
        for particle in self.damage_particles.values():
            if particle.active:
                particle.update(dt)


class Laser2:
    def __init__(self, player):
        self.player = player
        self.direction = self.player.direction
        self.activate = False
        self.image = pygame.image.load('graphics/laser/laser_usage.png').convert_alpha()
        self.x = int(player.pos.x)+16
        self.y = int(player.pos.y)-16
        self.rect = self.image.get_rect()
        self.display_surface = pygame.display.get_surface()
        self.damage_particles = {}
        self.damage_particles_key = 'a'

    def draw(self, player, target, dt):
        self.x = int(player.pos.x) - 17
        self.y = int(player.pos.y) - 16
        self.activate = player.skill_activated and player.selected_skill == 'laser'

        if self.activate:
            if self.y + 50 > target.pos.y > self.y - 10:
                target.health -= 0.2
                self.damage_particles[self.damage_particles_key] = Particle2((target.pos.x + 16, player.pos.y))
                self.damage_particles_key = chr(
                    ord(self.damage_particles_key) + 1) if self.damage_particles_key != 'A' else 'a'
                for i in range(self.x, int(target.pos.x) + 16, -1):
                    self.display_surface.blit(self.image, (i, self.y))

            else:
                for i in range(self.x, 0, -1):
                    self.display_surface.blit(self.image, (i, self.y))

        for particle in self.damage_particles.values():
            if particle.active:
                particle.update(dt)


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.feathered_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.direction = pygame.math.Vector2(random.uniform(0.5, 1), random.uniform(-1, 1))
        self.rect = player.rect.copy()
        self.rect.center = (int(player.pos.x), int(player.pos.y))
        self.speed = 500
        self.pos = pygame.math.Vector2(self.rect.center)
        self.life_time = random.uniform(5000, 6000)
        self.born_time = pygame.time.get_ticks()
        self.active = True

    def move(self, dt):
        self.pos = self.pos + self.direction * self.speed * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def draw(self):
        color = (255, 255, 255)
        center = self.rect.center
        radius = 12
        feather_radius = 4

        for r in range(radius + feather_radius, radius, -1):
            alpha = 255 - int(255 * (r - radius) / feather_radius)
            feather_color = color + (alpha,)
            pygame.draw.circle(self.feathered_surface,
                               feather_color,
                               (radius + feather_radius, radius + feather_radius), r)
        self.display_surface.blit(self.feathered_surface,
                                  (center[0] - radius - feather_radius, center[1] - radius - feather_radius)
                                  )

    def damage(self, target):
        if self.rect.colliderect(target.rect):
            self.active = False
            target.health -= 2

    def update(self, dt, target):
        self.move(dt)
        self.draw()
        self.damage(target)
        if self.life_time < pygame.time.get_ticks() - self.born_time:
            self.active = False
        if not self.active:
            self.kill()


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.feathered_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.direction = pygame.math.Vector2(random.uniform(-0.5, -1), random.uniform(-1, 1))
        self.rect = player.rect.copy()
        self.rect.center = (int(player.pos.x), int(player.pos.y))
        self.speed = 500
        self.pos = pygame.math.Vector2(self.rect.center)
        self.life_time = random.uniform(5000, 6000)
        self.born_time = pygame.time.get_ticks()
        self.active = True

    def move(self, dt):
        self.pos = self.pos + self.direction * self.speed * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def draw(self):
        color = (255, 255, 255)
        center = self.rect.center
        radius = 12
        feather_radius = 4

        for r in range(radius + feather_radius, radius, -1):
            alpha = 255 - int(255 * (r - radius) / feather_radius)
            feather_color = color + (alpha,)
            pygame.draw.circle(self.feathered_surface,
                               feather_color,
                               (radius + feather_radius, radius + feather_radius), r)
        self.display_surface.blit(self.feathered_surface,
                                  (center[0] - radius - feather_radius, center[1] - radius - feather_radius)
                                  )

    def damage(self, target):
        if self.rect.colliderect(target.rect):
            target.health -= 2.5
            self.active = False

    def update(self, dt, target):
        self.move(dt)
        self.draw()
        self.damage(target)
        if self.life_time < pygame.time.get_ticks() - self.born_time:
            self.active = False
        if not self.active:
            self.kill()


class Particle1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.pos = pos
        self.speed = 500
        self.rect = pygame.Rect(0, 0, 4, 4)
        self.radius = 2
        self.life_time = random.uniform(0, 500)
        self.born_time = pygame.time.get_ticks()
        self.direction = pygame.math.Vector2(random.uniform(-0.5, -1), random.uniform(-1, 1))
        self.feathered_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.active = True

    def move(self, dt):
        self.pos = self.pos + self.direction * self.speed * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def draw(self):
        color = (255, 255, 255)

        pygame.draw.circle(self.display_surface, color, (self.rect.centerx, self.rect.centery), 1)

    def update(self, dt):
        self.move(dt)
        self.draw()
        self.active = not pygame.time.get_ticks() - self.born_time > self.life_time
        if not self.active:
            self.kill()


class Particle2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.pos = pos
        self.speed = 500
        self.rect = pygame.Rect(0, 0, 4, 4)
        self.radius = 2
        self.life_time = random.uniform(0, 500)
        self.born_time = pygame.time.get_ticks()
        self.direction = pygame.math.Vector2(random.uniform(0.5, 1), random.uniform(-1, 1))
        self.feathered_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.active = True

    def move(self, dt):
        self.pos = self.pos + self.direction * self.speed * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def draw(self):
        color = (255, 255, 255)

        pygame.draw.circle(self.display_surface, color, (self.rect.centerx, self.rect.centery), 1)

    def update(self, dt):
        self.move(dt)
        self.draw()
        self.active = not pygame.time.get_ticks() - self.born_time > self.life_time
        if not self.active:
            self.kill()
