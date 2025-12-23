# environment.py
import numpy as np
import random
from settings import *

class MazeEnvironment:
    def __init__(self):
        # 1. Define the State Space (The Map)
        # 0 = Empty, 1 = Wall
        self.grid = np.zeros((ROWS, COLS), dtype=int)
        
        # 2. Setup Start and Goal
        self.start_pos = (0, 0)
        self.goal_pos = (ROWS - 1, COLS - 1)
        self.agent_pos = list(self.start_pos) # [row, col]

        # 3. Generate Random Obstacles
        self.generate_obstacles()

    def generate_obstacles(self):
        # Iterate through the matrix and randomly place walls
        for r in range(ROWS):
            for c in range(COLS):
                # Don't block start or goal
                if (r, c) == self.start_pos or (r, c) == self.goal_pos:
                    continue
                # 20% chance to be a wall
                if random.random() < 0.2:
                    self.grid[r, c] = 1

    def step(self, action):
        """
        Takes an action (direction) and returns the result.
        Actions: 0=Up, 1=Down, 2=Left, 3=Right
        Returns: (new_position, reward_message, done)
        """
        # Save old position to restore if we hit a wall
        old_r, old_c = self.agent_pos
        new_r, new_c = old_r, old_c

        if action == 0:   # UP
            new_r -= 1
        elif action == 1: # DOWN
            new_r += 1
        elif action == 2: # LEFT
            new_c -= 1
        elif action == 3: # RIGHT
            new_c += 1

        # Check Bounds
        if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
            return self.agent_pos, "Hit Boundary", False

        # Check Walls
        if self.grid[new_r, new_c] == 1:
            return self.agent_pos, "Hit Wall", False
        
        # Valid Move
        self.agent_pos = [new_r, new_c]
        
        # Check Goal
        if tuple(self.agent_pos) == self.goal_pos:
            return self.agent_pos, "Goal Reached", True
            
        return self.agent_pos, "Moved", False

    def reset(self):
        self.agent_pos = list(self.start_pos)