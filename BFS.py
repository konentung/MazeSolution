import pygame
from collections import deque
import config

class BFSSolver:
    def __init__(self, maze, cell_size, win):
        self.maze = maze
        self.cell_size = cell_size
        self.win = win

    def solve_with_animation(self, start, goal, player):
        queue = deque([start])
        visited = set()
        visited.add(start)
        parent = {start: None}

        while queue:
            current = queue.popleft()

            # Render current step
            self.animate_step(current, visited, player, goal)

            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]  # 返回從起點到終點的路徑

            x, y = current
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 上下左右
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze) and
                        self.maze[ny][nx] == 0 and (nx, ny) not in visited):
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current

        return None  # 無解

    def animate_step(self, current, visited, player, goal):
        self.win.fill(config.WHITE)

        # Draw maze
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                color = config.BLACK if self.maze[y][x] == 1 else config.WHITE
                pygame.draw.rect(self.win, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        # Draw visited nodes
        for node in visited:
            pygame.draw.rect(
                self.win, config.LIGHT_BLUE,
                (node[0] * self.cell_size, node[1] * self.cell_size, self.cell_size, self.cell_size)
            )

        # Draw current step in yellow
        pygame.draw.rect(
            self.win, config.YELLOW,
            (current[0] * self.cell_size, current[1] * self.cell_size, self.cell_size, self.cell_size)
        )

        # Draw goal
        pygame.draw.rect(
            self.win, config.GREEN,
            (goal.rect.x, goal.rect.y, goal.rect.width, goal.rect.height)
        )

        # Update player position
        player.x, player.y = current
        player.rect.topleft = (current[0] * self.cell_size, current[1] * self.cell_size)

        all_sprites = pygame.sprite.Group(player)
        all_sprites.draw(self.win)

        pygame.display.update()
        pygame.time.delay(200)  # 每步延遲 200 毫秒
