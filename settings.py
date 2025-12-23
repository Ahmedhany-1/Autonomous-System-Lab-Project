# settings.py

# Screen dimensions
WIDTH, HEIGHT = 600, 600
# Grid dimensions (Matrix size)
ROWS, COLS = 5, 5
CELL_SIZE = WIDTH // COLS

# Colors (R, G, B)
WHITE = (255, 255, 255) # Path
BLACK = (0, 0, 0)       # Wall
BLUE  = (0, 0, 255)     # Player (Manual)
GREEN = (0, 255, 0)     # Goal
RED   = (255, 0, 0)     # Player (AI Training)
YELLOW = (255, 255, 0)  # Solution Path
GRAY  = (200, 200, 200) # Grid Lines