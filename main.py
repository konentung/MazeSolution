import pygame
import sys
from map import Maze
import config
from sprite import Player, Goal
from screen_display import ScreenDisplay
from BFS import BFSSolver

# Initialize Pygame
pygame.init()

# Set up display
WIN = pygame.display.set_mode((config.COLS * config.CELL_SIZE, config.ROWS * config.CELL_SIZE))
pygame.display.set_caption("Maze Game")

# Set up fonts
FONT = pygame.font.Font(None, 36)
HOVER_FONT = pygame.font.Font(None, 48)  # 放大的字型

# Set up clock
CLOCK = pygame.time.Clock()

# Initialize screen display
screen_display = ScreenDisplay(WIN, FONT, HOVER_FONT)

# Initialize variables
maze = None
player = None
goal = None
game_mode = None
algorithm = None

# Check collision with goal
def check_collision():
    return pygame.sprite.collide_rect(player, goal)

# Main game loop
def main():
    global maze, player, goal, game_mode, algorithm

    # Display menu and get game mode
    game_mode = screen_display.display_menu()

    if game_mode == 'auto':
        algorithm = screen_display.display_algorithm_menu()
        print(f"Selected Algorithm: {algorithm}")  # Debugging line for selected algorithm

    # Initialize maze, player, and goal after selecting mode
    maze = Maze(config.ROWS, config.COLS, config.CELL_SIZE)
    player = Player(1, 1)
    goal = Goal(5, 1)

    if game_mode == 'manual':
        running = True
        while running:
            WIN.fill(config.WHITE)
            maze.draw(WIN, [config.WHITE, config.BLACK])
            all_sprites = pygame.sprite.Group()
            all_sprites.add(player, goal)
            all_sprites.draw(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.move(0, -1, maze)
                    elif event.key == pygame.K_DOWN:
                        player.move(0, 1, maze)
                    elif event.key == pygame.K_LEFT:
                        player.move(-1, 0, maze)
                    elif event.key == pygame.K_RIGHT:
                        player.move(1, 0, maze)

            if check_collision():
                screen_display.display_win_screen()
                running = False

            pygame.display.update()
            CLOCK.tick(60)

    elif game_mode == 'auto':
        if algorithm == 'BFS':
            bfs_solver = BFSSolver(maze.grid, config.CELL_SIZE, WIN)
            path = bfs_solver.solve_with_animation((1, 1), (5, 1), player)
            if path:
                screen_display.display_win_screen()
            else:
                WIN.fill(config.WHITE)
                text = FONT.render("No Solution Found!", True, config.BLACK)
                text_rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
                WIN.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()