import pygame
import config
import heapq

class DijkstraSolver:
    def __init__(self, maze, cell_size, win):
        self.maze = maze
        self.cell_size = cell_size
        self.win = win

    def solve_with_animation(self, start, goal, player):
        # 優先隊列，用來存儲節點及其累積距離
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))  # (累積距離, 節點)
        visited = set()
        parent = {start: None}
        distances = {start: 0}

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 上下左右

        while priority_queue:
            current_distance, current = heapq.heappop(priority_queue)

            if current in visited:
                continue
            visited.add(current)

            # Render current step
            self.animate_step(current, visited, player, goal)

            if current == goal:
                # 找到路徑後還原並返回路徑
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            x, y = current
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 確認是否在邊界內，且節點可通行
                if 0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze) and self.maze[ny][nx] == 0:
                    next_distance = current_distance + 1
                    if (nx, ny) not in distances or next_distance < distances[(nx, ny)]:
                        distances[(nx, ny)] = next_distance
                        heapq.heappush(priority_queue, (next_distance, (nx, ny)))
                        parent[(nx, ny)] = current

                        # 標示檢查中的節點
                        self.highlight_direction((x, y), (dx, dy), visited)

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
