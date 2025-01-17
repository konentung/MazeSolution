import pygame
import config

class WallFollowerSolver:
    def __init__(self, maze, cell_size, win):
        self.maze = maze
        self.cell_size = cell_size
        self.win = win

    def solve_with_animation(self, start, goal, player):
        x, y = start
        direction = (0, 1)  # 初始方向：向下

        visited = set()
        path = [start]

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 上右下左

        while (x, y) != goal:
            visited.add((x, y))
            
            # 測試右邊是否有牆
            direction_idx = directions.index(direction)
            right_idx = (direction_idx + 1) % 4
            right_direction = directions[right_idx]
            nx, ny = x + right_direction[0], y + right_direction[1]

            self.highlight_direction((x, y), right_direction, visited)

            if 0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze) and self.maze[ny][nx] == 0:
                # 如果右側無牆，轉向右側並前進
                direction = right_direction
                x, y = nx, ny
            else:
                # 右側有牆，沿著牆前進
                nx, ny = x + direction[0], y + direction[1]
                self.highlight_direction((x, y), direction, visited)
                if 0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze) and self.maze[ny][nx] == 0:
                    x, y = nx, ny
                else:
                    # 如果前方有牆，左轉
                    left_idx = (direction_idx - 1) % 4
                    direction = directions[left_idx]

            self.clear_highlight((x, y), right_direction, visited)

            path.append((x, y))

            # 動畫渲染
            self.animate_step((x, y), visited, player, goal)

        return path

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
        清除當前點正在檢查的方向標示，恢復成原本顏色。
        """
        x, y = current
        dx, dy = direction
        highlight_x, highlight_y = x + dx, y + dy

        if 0 <= highlight_x < len(self.maze[0]) and 0 <= highlight_y < len(self.maze):
            # 根據迷宮格子的狀態恢復顏色
            if self.maze[highlight_y][highlight_x] == 1:
                color = config.BLACK  # 牆壁
            elif (highlight_x, highlight_y) in visited:
                color = config.LIGHT_BLUE  # 已訪問
            else:
                color = config.WHITE  # 空白未訪問

            pygame.draw.rect(
                self.win, color,
                (highlight_x * self.cell_size, highlight_y * self.cell_size, self.cell_size, self.cell_size)
            )
            pygame.display.update()