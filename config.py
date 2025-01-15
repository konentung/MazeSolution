# postion: root
START = (1, 1)
GOAL = (1, 11)

# display settings
CELL_SIZE = 40
ROWS = 15
COLS = 15
WIDTH = ROWS * CELL_SIZE
HEIGHT = COLS * CELL_SIZE

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_PURPLE = (221, 160, 221)
LIGHT_ORANGE = (255, 160, 122)
LIGHT_PINK = (255, 182, 193)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (169, 169, 169)
BROWN = (165, 42, 42)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)
CYAN = (0, 255, 255)

# message
MESSAGES = {
    "warning": [
        "Please wait for the animation to finish...",
        "Avoid closing the window abruptly."
    ],
    "no_solution": "No Solution Found!"
}

# delay
DELAYS = {
    "warning_screen": 2000,  # 警告畫面延遲
    "no_solution": 3000,     # 無解畫面延遲
    "algorithm_step": 10,   # 演算法動畫延遲
}