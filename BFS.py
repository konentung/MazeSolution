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

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 上下左右

        while queue:
            current = queue.popleft()

            # Render current step
            self.animate_step(current, visited, player, goal)

            x, y = current
            for dx, dy in directions:  # 檢查每個方向
                nx, ny = x + dx, y + dy

                # 動畫：標示目前正在檢查的方向
                self.highlight_direction((x, y), (dx, dy), visited)

                if (0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze) and
                        self.maze[ny][nx] == 0 and (nx, ny) not in visited):
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current

                # 動畫：清除方向標示
                self.clear_highlight((x, y), (dx, dy), visited)

            if current == goal:
                # 找到路徑後還原並返回路徑
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

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
            (goal[0] * self.cell_size, goal[1] * self.cell_size, self.cell_size, self.cell_size)
        )

        # Update player position
        player.x, player.y = current
        player.rect.topleft = (current[0] * self.cell_size, current[1] * self.cell_size)

        all_sprites = pygame.sprite.Group(player)
        all_sprites.draw(self.win)

        pygame.display.update()
        pygame.time.delay(config.DELAYS["algorithm_step"])  # 使用 algorithm_step 延遲


    def highlight_direction(self, current, direction, visited):
        """
        標示當前點正要檢查的方向。
        """
        x, y = current
        dx, dy = direction
        highlight_x, highlight_y = x + dx, y + dy

        if 0 <= highlight_x < len(self.maze[0]) and 0 <= highlight_y < len(self.maze):
            # 如果該點已經被訪問過，使用淺藍色
            color = config.LIGHT_BLUE if (highlight_x, highlight_y) in visited else config.YELLOW
            pygame.draw.rect(
                self.win, color,  # 用淺藍色或黃色標示
                (highlight_x * self.cell_size, highlight_y * self.cell_size, self.cell_size, self.cell_size)
            )
            pygame.display.update()
            pygame.time.delay(config.DELAYS["algorithm_step"])  # 使用 algorithm_step 延遲
    
    def clear_highlight(self, current, direction, visited):
        """
        清除當前點正在檢查的方向標示。
        """
        x, y = current
        dx, dy = direction
        highlight_x, highlight_y = x + dx, y + dy

        if 0 <= highlight_x < len(self.maze[0]) and 0 <= highlight_y < len(self.maze):
            # 如果該點已經被訪問過，重新填充淺藍色；否則使用白色
            color = config.LIGHT_BLUE if (highlight_x, highlight_y) in visited else config.WHITE
            pygame.draw.rect(
                self.win, color,  # 用淺藍色或白色清除標示
                (highlight_x * self.cell_size, highlight_y * self.cell_size, self.cell_size, self.cell_size)
            )
            pygame.display.update()
