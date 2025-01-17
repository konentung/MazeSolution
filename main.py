import pygame
import sys
from map import Maze
import config
from sprite import Player, Goal
from screen_display import ScreenDisplay
from BFS import BFSSolver
from DFS import DFSSolver
from Dijkstra import DijkstraSolver
from WallFollower import WallFollowerSolver
from AStar import AStarSolver
from DeadEndFilling import DeadEndFillingSolver

# Initialize Pygame
pygame.init()

# Set up display
WIN = pygame.display.set_mode((config.COLS * config.CELL_SIZE, config.ROWS * config.CELL_SIZE))
pygame.display.set_caption("Maze Game")

# Set up fonts
FONT = pygame.font.Font(None, 36)
HOVER_FONT = pygame.font.Font(None, 48)  # Enlarged font for hover effect

# Set up clock
CLOCK = pygame.time.Clock()

# Initialize screen display
screen_display = ScreenDisplay(WIN, FONT, HOVER_FONT)

# Global variables
maze = None
player = None
goal = None

# Check collision between the player and the goal
def check_collision():
    return pygame.sprite.collide_rect(player, goal)

# Handle maze-solving algorithms
def handle_algorithm(maze, config, WIN, FONT, screen_display, player):
    """
    Handle solving the maze using BFS or DFS algorithms, with the option to return.
    """
    while True:
        # Display algorithm selection menu
        algorithm = screen_display.display_algorithm_menu()

        if algorithm == 'Back':  # Return to the main menu
            return

        solver = None
        if algorithm == 'BFS':
            screen_display.display_warning_screen(config.MESSAGES["warning"])
            solver = BFSSolver(maze.grid, config.CELL_SIZE, WIN)
        if algorithm == 'DFS':
            screen_display.display_warning_screen(config.MESSAGES["warning"])
            solver = DFSSolver(maze.grid, config.CELL_SIZE, WIN)
        if algorithm == 'Dijkstra':
            screen_display.display_warning_screen(config.MESSAGES["warning"])
            solver = DijkstraSolver(maze.grid, config.CELL_SIZE, WIN)
        if algorithm == 'WallFollower':
            screen_display.display_warning_screen(config.MESSAGES["warning"])
            solver = WallFollowerSolver(maze.grid, config.CELL_SIZE, WIN)
        if algorithm == 'A*':
            screen_display.display_warning_screen(config.MESSAGES["warning"])
            solver = AStarSolver(maze.grid, config.CELL_SIZE, WIN)
        if algorithm == 'DeadEndFilling':
            screen_display.display_warning_screen(config.MESSAGES["warning"])
            solver = DeadEndFillingSolver(maze.grid, config.CELL_SIZE, WIN)

        if solver:  # Ensure solver is initialized
            path = solver.solve_with_animation(config.START, config.GOAL, player)
            if path:
                screen_display.display_win_screen()
            else:
                display_no_solution(WIN, FONT, config)
            return
        else:
            print("Invalid algorithm selection. Please try again.")

# Display "No Solution Found" message
def display_no_solution(WIN, FONT, config):
    """
    Display a message indicating that no solution was found.
    """
    WIN.fill(config.WHITE)
    text = FONT.render(config.MESSAGES["no_solution"], True, config.BLACK)
    text_rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
    WIN.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(config.DELAYS["no_solution"])  # Delay for no solution screen

# Main game loop
def main():
    global maze, player, goal

    while True:  # Main menu loop
        # Display the main menu to select the game mode
        game_mode = screen_display.display_menu()

        # Initialize maze, player, and goal
        maze = Maze(config.ROWS, config.COLS, config.CELL_SIZE)
        player = Player(1, 1)
        goal = Goal(5, 1)

        if game_mode == 'manual':
            # Manual game loop
            running = True
            while running:
                WIN.fill(config.WHITE)
                maze.draw(WIN, [config.WHITE, config.BLACK])
                all_sprites = pygame.sprite.Group()
                all_sprites.add(player, goal)
                all_sprites.draw(WIN)

                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            player.move(0, -1, maze)
                        elif event.key == pygame.K_DOWN:
                            player.move(0, 1, maze)
                        elif event.key == pygame.K_LEFT:
                            player.move(-1, 0, maze)
                        elif event.key == pygame.K_RIGHT:
                            player.move(1, 0, maze)

                # Check for goal collision
                if check_collision():
                    screen_display.display_win_screen()
                    running = False

                pygame.display.update()
                CLOCK.tick(60)

        elif game_mode == 'auto':
            # Auto mode - solve the maze
            handle_algorithm(maze, config, WIN, FONT, screen_display, player)
        
        elif game_mode == 'QUIT':
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()