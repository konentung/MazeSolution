import pygame
import sys
import os
import random
import time
import config
import map

# Initialize Pygame
pygame.init()

# Set up display
map.window()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up fonts
FONT = pygame.font.Font(None, 32)

# Set up clock
CLOCK = pygame.time.Clock()

# Set up maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Set up player
player = {
    "x": 1,
    "y": 1,
    "width": 20,
    "height": 20,
    "color": config.RED,
    "speed": 5
}

# Set up goal
goal = {
    "x": 8,
    "y": 5,
    "width": 20,
    "height": 20,
    "color": config.GREEN
}

# Set helper functions
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                pygame.draw.rect(WIN, config.BLACK, (x * 40, y * 40, 40, 40))

def draw_player():
    pygame.draw.rect(WIN, player["color"], (player["x"] * 40, player["y"] * 40, player["width"], player["height"]))

def draw_goal():
    pygame.draw.rect(WIN, goal["color"], (goal["x"] * 40, goal["y"] * 40, goal["width"], goal["height"]))
    text = FONT.render("GOAL", True, config.BLACK)
    WIN.blit(text, (goal["x"] * 40, goal["y"] * 40))
    
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if maze[player["y"] - 1][player["x"]] == 0:
            player["y"] -= 1
    if keys[pygame.K_DOWN]:
        if maze[player["y"] + 1][player["x"]] == 0:
            player["y"] += 1
    if keys[pygame.K_LEFT]:
        if maze[player["y"]][player["x"] - 1] == 0:
            player["x"] -= 1
    if keys[pygame.K_RIGHT]:
        if maze[player["y"]][player["x"] + 1] == 0:
            player["x"] += 1

def check_collision():
    if player["x"] == goal["x"] and player["y"] == goal["y"]:
        return True
    return False

def main():
    running = True
    while running:
        WIN.fill(config.WHITE)
        draw_maze()
        draw_player()
        draw_goal()
        move_player()
        if check_collision():
            text = FONT.render("YOU WIN!", True, config.BLACK)
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            time.sleep(2)
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        CLOCK.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

