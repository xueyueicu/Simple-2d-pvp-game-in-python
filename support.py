import random

import pygame


class Particle_Init(pygame.sprite.Sprite):

    def __init__(self, pos, image, speed=random.uniform(50, 100), direction=pygame.math.Vector2(0, -1), life=random.uniform(400, 500)):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.pos = pos
        self.image = image
        self.speed = speed
        self.direction = direction
        self.life = life
        self.born_time = pygame.time.get_ticks()
        self.active = True
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos = self.pos + self.direction * self.speed * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def draw(self):
        self.display_surface.blit(self.image, self.rect)

    def update(self, dt):
        self.move(dt)
        self.draw()
        self.active = not pygame.time.get_ticks() - self.born_time > self.life
        if not self.active:
            self.kill()


def generate_health_particle(player, pos, image, dt,speed=0, direction=pygame.math.Vector2(0, 0), life=500):
    particles = {}
    particle_key = 'a'
    if player.skill_activated and player.selected_skill == 'health_regen':
        particles[particle_key] = Particle_Init(pos, image, speed, direction, life)
        particle_key = chr(ord(particle_key) + 1) if particle_key.isalpha() else 'a'

    for particle in particles.values():
        if particle.active:
            particle.update(dt)
