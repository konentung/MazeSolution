import pygame
import sys
import config

class ScreenDisplay:
    def __init__(self, win, font, hover_font):
        self.win = win
        self.font = font
        self.hover_font = hover_font

    def display_menu(self):
        self.win.fill(config.WHITE)
        title = self.font.render("Select Game Mode", True, config.BLACK)

        manual_option = self.font.render("Manual Solve", True, config.BLACK)
        auto_option = self.font.render("Auto Solve", True, config.BLACK)

        title_rect = title.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 4))
        manual_rect = manual_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
        auto_rect = auto_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + 50))

        while True:
            self.win.fill(config.WHITE)
            self.win.blit(title, title_rect)

            # 檢查滑鼠是否懸停在按鈕上
            mouse_pos = pygame.mouse.get_pos()
            if manual_rect.collidepoint(mouse_pos):
                manual_option = self.hover_font.render("Manual Solve", True, config.BLACK)
                manual_rect = manual_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
            else:
                manual_option = self.font.render("Manual Solve", True, config.BLACK)
                manual_rect = manual_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))

            if auto_rect.collidepoint(mouse_pos):
                auto_option = self.hover_font.render("Auto Solve", True, config.BLACK)
                auto_rect = auto_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + 50))
            else:
                auto_option = self.font.render("Auto Solve", True, config.BLACK)
                auto_rect = auto_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + 50))

            self.win.blit(manual_option, manual_rect)
            self.win.blit(auto_option, auto_rect)

            pygame.display.update()

            # 檢查滑鼠點擊
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if manual_rect.collidepoint(mouse_pos):
                        return 'manual'
                    elif auto_rect.collidepoint(mouse_pos):
                        return 'auto'

    def display_algorithm_menu(self):
        self.win.fill(config.WHITE)
        title = self.font.render("Select Solving Algorithm", True, config.BLACK)

        options = ["Dijkstra", "Kruskal", "Greedy", "BFS", "DFS"]
        option_rects = []

        title_rect = title.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 4))

        # Generate options dynamically
        for i, option in enumerate(options):
            text = self.font.render(option, True, config.BLACK)
            rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + i * 50))
            option_rects.append((text, rect))

        while True:
            self.win.fill(config.WHITE)
            self.win.blit(title, title_rect)

            mouse_pos = pygame.mouse.get_pos()

            # Draw options and handle hover
            for i, (text, rect) in enumerate(option_rects):
                if rect.collidepoint(mouse_pos):
                    text = self.hover_font.render(options[i], True, config.BLACK)
                    rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + i * 50))
                else:
                    text = self.font.render(options[i], True, config.BLACK)
                    rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + i * 50))
                option_rects[i] = (text, rect)
                self.win.blit(text, rect)

            pygame.display.update()

            # Check for mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (_, rect) in enumerate(option_rects):
                        if rect.collidepoint(mouse_pos):
                            return options[i]

    def display_win_screen(self):
        self.win.fill(config.WHITE)
        text = self.font.render("YOU WIN! Click anywhere to exit.", True, config.BLACK)
        text_rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))
        self.win.blit(text, text_rect)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False