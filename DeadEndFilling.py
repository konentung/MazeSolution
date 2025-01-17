import pygame
import config

class DeadEndFillingSolver:
    def __init__(self, maze, cell_size, win):
        self.maze = maze
        self.cell_size = cell_size
        self.win = win

    def solve_with_animation(self, start, goal, player):
        return self.solve_with_dead_end_filling(start, goal, player)

    def solve_with_dead_end_filling(self, start, goal, player):
        rows, cols = len(self.maze), len(self.maze[0])
        dead_ends = set()
        path = []

        # 初始化訪問狀態
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # 堆疊只存放未確定是否為死路的節點
        stack = [start]
        while stack:
            x, y = stack.pop()

            if visited[y][x]:
                continue

            visited[y][x] = True
            path.append((x, y))

            # 檢查是否到達目標
            if (x, y) == goal:
                print("找到解答")
                self.animate_dead_end_filling((x, y), dead_ends, path, player, goal)
                pygame.time.delay(2000)  # 顯示目標達成的延遲
                return path  # 回傳完整路徑

            # 測試是否為死路
            if (x, y) != start and self.is_dead_end((x, y), goal, visited, dead_ends):
                dead_ends.add((x, y))
                path.remove((x, y))  # 從路徑中移除死路

            # 動畫渲染
            self.animate_dead_end_filling((x, y), dead_ends, path, player, goal)

            # 添加相鄰節點
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx] and self.maze[ny][nx] == 0:
                    stack.append((nx, ny))

        # 若走訪結束仍未找到目標
        print("無法找到解答")
        return None  # 無解時回傳 None

    def is_dead_end(self, cell, goal, visited, dead_ends):
        """
        檢查是否為死路，若是死路則回傳 True。
        """
        x, y = cell

        # 出發點和目標不能標記為死路
        if cell == goal:
            return False

        # 計算通行的鄰居數量
        neighbors = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze):
                if self.maze[ny][nx] == 0 and (nx, ny) not in dead_ends:
                    neighbors += 1

        return neighbors <= 1

    def animate_dead_end_filling(self, current, dead_ends, path, player, goal):
        self.win.fill(config.WHITE)

        # Draw maze
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                color = config.BLACK if self.maze[y][x] == 1 else config.WHITE
                pygame.draw.rect(self.win, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        # Draw dead ends
        for node in dead_ends:
            pygame.draw.rect(
                self.win, config.ORANGE,  # 使用紅色標示死路
                (node[0] * self.cell_size, node[1] * self.cell_size, self.cell_size, self.cell_size)
            )

        # Draw path
        for node in path:
            pygame.draw.rect(
                self.win, config.LIGHT_BLUE,  # 使用淺藍色標示路徑
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