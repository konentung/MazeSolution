import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((config.CELL_SIZE, config.CELL_SIZE))
        self.image.fill(config.RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * config.CELL_SIZE, y * config.CELL_SIZE)
        self.x = x
        self.y = y

    def move(self, dx, dy, maze):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < config.COLS and 0 <= new_y < config.ROWS and maze.grid[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y
            self.rect.topleft = (self.x * config.CELL_SIZE, self.y * config.CELL_SIZE)

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((config.CELL_SIZE, config.CELL_SIZE))
        self.image.fill(config.GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * config.CELL_SIZE, y * config.CELL_SIZE)
