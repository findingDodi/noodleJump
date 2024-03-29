import pygame
import math

import conf


class GameCore:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.last_event = None
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        self.noodle = pygame.image.load('./assets/images/noodle.png')
        self.noodle_rect = self.noodle.get_rect()
        self.noodle_rect[0] = 20
        self.noodle_rect[1] = self.screen_height / 2

        self.noodle_min_position_x = 20
        self.noodle_max_position_x = self.screen_width - self.noodle_rect[2] - 20

    def move_noodle(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            if self.noodle_rect[0] > self.noodle_min_position_x:
                self.noodle_rect[0] -= 20

        elif keys_pressed[pygame.K_RIGHT]:
            if self.noodle_rect[0] < self.noodle_max_position_x:
                self.noodle_rect[0] += 20

    def border_patrol(self):
        if self.noodle_rect[0] < self.noodle_min_position_x:
            self.noodle_rect[0] = self.noodle_min_position_x
        elif self.noodle_rect[0] > self.noodle_max_position_x:
            self.noodle_rect[0] = self.noodle_max_position_x

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("Noodle Jump")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit framespeed to 30fps
            clock.tick(30)
            self.screen.fill((55, 55, 55), self.background_rect)
            self.screen.blit(self.noodle, self.noodle_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False

            self.move_noodle()
            self.border_patrol()

            # final draw
            pygame.display.flip()
