import pygame
from settings import *
from timer import Timer
from skills import Bullet1, Bullet2
from support import Particle_Init
import random


class Bot1(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 32))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 400
        self.skill_cooldown_time = 3000
        self.cooldown_runtime = 0
        self.status = 'static'
        self.timers = {
            'skill use': Timer(500),
            'skill switch': Timer(200),
            'skill cooldown': Timer(self.skill_cooldown_time)
        }
        self.skills = ['laser', 'bullet', 'health_regen']
        self.skill_index = 0
        self.selected_skill = self.skills[self.skill_index]
        self.health = 100
        self.max_health = 100
        self.skill_activated = False
        self.bullet_key = 'a'
        self.bullets = {}
        self.health_regen_particles = {}
        self.health_regen_particle_key = 'a'
        self.timers['skill cooldown'].activate()


    def use_skill(self, dt):
        if self.skill_activated:

            print('Using skill', self.selected_skill)
            if self.selected_skill == 'health_regen':
                self.health += HEALTH_REGEN_AMOUNT
                if self.health > self.max_health:
                    self.health = self.max_health
                health_particle_pos = self.pos + pygame.math.Vector2(random.uniform(-32, 32), random.uniform(-32, 32))
                health_particle_img = pygame.image.load('graphics/particles/health_regen.png')
                self.health_regen_particles[self.health_regen_particle_key] = Particle_Init(health_particle_pos,
                                                                                            health_particle_img)
                self.health_regen_particle_key = chr(
                    ord(self.health_regen_particle_key) + 1) if self.health_regen_particle_key != 'z' else 'a'
        for particle in self.health_regen_particles.values():
            if particle.active:
                particle.update(dt)

    def input(self, target):
        if not self.timers['skill use'].active:
            if self.pos.y - 16 > target.pos.y:
                self.direction.y = -1
            elif self.pos.y + 16 < target.pos.y:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if abs(self.pos.x - target.pos.x) > 500:
                self.direction.x = 1
            elif abs(self.pos.x - target.pos.x) < 500:
                self.direction.x = -1

            if not self.timers['skill use'].active and not self.timers['skill cooldown'].active:
                self.timers['skill use'].activate()
                self.timers['skill cooldown'].activate()
                self.direction = pygame.math.Vector2(0, 0)
                self.skill_activated = True

            for i in target.bullets.values():
                if i.active and i.pos.distance_to(self.pos) < 100:
                    self.direction.y = self.direction.y + 1 if i.pos.y < self.pos.y else self.direction.y - 1 if i.pos.y > self.pos.y else self.direction.y
                    self.direction.x = self.direction.x - 1 if i.pos.x > self.pos.x else self.direction.x
            if target.selected_skill == 'laser' and target.timers['skill use'].active:

                self.direction.y = 5 if self.pos.y < SCREEN_HEIGHT/2 else -5

    def select_skill(self, target):
        if not self.timers['skill use'].active:
            self.selected_skill = "health_regen" if self.health < self.max_health / 10 else "laser" if target.pos.y - 16 < self.pos.y < target.pos.y + 16 else "bullet"

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):
        if not self.timers['skill use'].active:
            self.speed = random.randint(300, 500)
            if self.direction.magnitude() > 0:
                self.direction = self.direction.normalize()

            self.pos.x += self.direction.x * self.speed * dt if not (
                    self.rect.left <= 1 and self.direction.x < 0
            ) and not (
                    self.rect.right >= SCREEN_WIDTH/2 - 17 - 8 and self.direction.x > 0
            ) else 0
            self.rect.centerx = self.pos.x

            self.pos.y += self.direction.y * self.speed * dt if not (
                    self.rect.top <= 1 and self.direction.y < 0
            ) and not (
                    self.rect.bottom >= SCREEN_HEIGHT - 1 and self.direction.y > 0
            ) else 0
            self.rect.centery = self.pos.y

    def get_status(self):
        if self.timers['skill use'].active:
            self.status = f'Using {self.selected_skill}'
        else:
            self.skill_activated = False
        if self.timers['skill cooldown'].active:
            self.cooldown_runtime = self.timers['skill cooldown'].runtime
        else:
            self.cooldown_runtime = self.skill_cooldown_time
        if self.health <= 0:
            self.health = 0

    def get_position(self):
        return self.rect.center

    def shoot(self, dt, target):
        if self.skill_activated and self.selected_skill == 'bullet':
            self.bullets[self.bullet_key] = Bullet1(self)
            self.bullet_key = chr(ord(self.bullet_key) + 1) if self.bullet_key != 'A' else 'a'
        for bullet in self.bullets.values():
            if bullet.active:
                bullet.update(dt, target)

    def update(self, dt, target):
        self.use_skill(dt)
        self.input(target)
        self.select_skill(target)
        self.shoot(dt, target)
        self.move(dt)
        self.get_status()
        self.update_timers()


class Bot2(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 32))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 400
        self.skill_cooldown_time = 3000
        self.cooldown_runtime = 0
        self.status = 'static'
        self.timers = {
            'skill use': Timer(500),
            'skill switch': Timer(200),
            'skill cooldown': Timer(self.skill_cooldown_time)
        }
        self.skills = ['laser', 'bullet', 'health_regen']
        self.skill_index = 0
        self.selected_skill = self.skills[self.skill_index]
        self.health = 100
        self.max_health = 100
        self.skill_activated = False
        self.bullet_key = 'a'
        self.bullets = {}
        self.health_regen_particles = {}
        self.health_regen_particle_key = 'a'
        self.timers['skill cooldown'].activate()

    def use_skill(self, dt):
        if self.skill_activated:

            print('Using skill', self.selected_skill)
            if self.selected_skill == 'health_regen':
                self.health += HEALTH_REGEN_AMOUNT
                if self.health > self.max_health:
                    self.health = self.max_health
                health_particle_pos = self.pos + pygame.math.Vector2(random.uniform(-32, 32), random.uniform(-32, 32))
                health_particle_img = pygame.image.load('graphics/particles/health_regen.png')
                self.health_regen_particles[self.health_regen_particle_key] = Particle_Init(health_particle_pos,
                                                                                            health_particle_img)
                self.health_regen_particle_key = chr(
                    ord(self.health_regen_particle_key) + 1) if self.health_regen_particle_key != 'z' else 'a'
        for particle in self.health_regen_particles.values():
            if particle.active:
                particle.update(dt)

    def input(self, target):

        if not self.timers['skill use'].active:
            if self.pos.y - 16 > target.pos.y:
                self.direction.y = -1
            elif self.pos.y + 16 < target.pos.y:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if abs(self.pos.x - target.pos.x) > 500:
                self.direction.x = -1
            elif abs(self.pos.x - target.pos.x) < 500:
                self.direction.x = 1
            else:
                self.direction.x = 0

            for i in target.bullets.values():
                if i.active and i.pos.distance_to(self.pos) < 100:
                    self.direction.y = self.direction.y + 1 if i.pos.y < self.pos.y else self.direction.y - 1 if i.pos.y > self.pos.y else self.direction.y
                    self.direction.x = self.direction.x + 1 if i.pos.x < self.pos.x else self.direction.x

            if not self.timers['skill use'].active and not self.timers['skill cooldown'].active:
                self.timers['skill use'].activate()
                self.timers['skill cooldown'].activate()
                self.direction = pygame.math.Vector2(0, 0)
                self.skill_activated = True

            if target.selected_skill == 'laser' and target.timers['skill use'].active:
                    self.direction.y = 5 if self.pos.y < SCREEN_HEIGHT/2 else -5

    def select_skill(self, target):
        if not self.timers['skill use'].active:
            self.selected_skill = "health_regen" if self.health < self.max_health / 10 else "laser" if target.pos.y - 16 < self.pos.y < target.pos.y + 16 else "bullet"

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):
        if not self.timers['skill use'].active:
            self.speed = random.randint(300, 500)
            if self.direction.magnitude() > 0:
                self.direction = self.direction.normalize()

            self.pos.x += self.direction.x * self.speed * dt if not (
                    self.rect.left <= SCREEN_WIDTH/2 - 16 - 8 and self.direction.x < 0
            ) and not (
                    self.rect.right >= SCREEN_WIDTH - 1 and self.direction.x > 0
            ) else 0
            self.rect.centerx = self.pos.x

            self.pos.y += self.direction.y * self.speed * dt if not (
                    self.rect.top <= 1 and self.direction.y < 0
            ) and not (
                    self.rect.bottom >= SCREEN_HEIGHT - 1 and self.direction.y > 0
            ) else 0
            self.rect.centery = self.pos.y

    def get_status(self):
        if self.timers['skill use'].active:
            self.status = f'Using {self.selected_skill}'
        else:
            self.skill_activated = False
        if self.timers['skill cooldown'].active:
            self.cooldown_runtime = self.timers['skill cooldown'].runtime
        else:
            self.cooldown_runtime = self.skill_cooldown_time
        if self.health <= 0:
            self.health = 0

    def get_position(self):
        return self.rect.center

    def shoot(self, dt, target):
        if self.skill_activated and self.selected_skill == 'bullet':
            self.bullets[self.bullet_key] = Bullet2(self)
            self.bullet_key = chr(ord(self.bullet_key) + 1) if self.bullet_key != 'A' else 'a'
        for bullet in self.bullets.values():
            if bullet.active:
                bullet.update(dt, target)

    def update(self, dt, target):
        self.use_skill(dt)
        self.input(target)
        self.select_skill(target)
        self.shoot(dt, target)
        self.move(dt)
        self.get_status()
        self.update_timers()
