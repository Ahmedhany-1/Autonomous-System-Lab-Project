# rl_agent.py
import numpy as np
import random
from settings import *

class QLearningAgent:
    def __init__(self):
        # The Brain: A 3D Array [Row, Col, Action]
        # It stores the score for every possible move.
        self.q_table = np.zeros((ROWS, COLS, 4))
        
        # Hyperparameters (The Learning Settings)
        self.alpha = 0.1      # Learning Rate (How fast we overwrite old memory)
        self.gamma = 0.9      # Discount Factor (How much we care about future rewards)
        self.epsilon = 1.0    # Exploration Rate (1.0 = 100% Random at start)
        self.epsilon_decay = 0.995 # How fast we stop being random
        self.min_epsilon = 0.01

    def choose_action(self, state):
        # Epsilon-Greedy Strategy
        # Sometimes explore (random), sometimes exploit (use brain)
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, 3) # Explore
        else:
            r, c = state
            return np.argmax(self.q_table[r, c]) # Exploit (Best known move)

    def learn(self, state, action, reward, next_state):
        """
        The Core Math: The Bellman Equation Update
        NewEstimate = OldEstimate + LearningRate * (Reward + Discount * FutureValue - OldEstimate)
        """
        r, c = state
        next_r, next_c = next_state
        
        old_value = self.q_table[r, c, action]
        next_max = np.max(self.q_table[next_r, next_c])
        
        # Update the Q-Value
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
        self.q_table[r, c, action] = new_value

    def decay_epsilon(self):
        # Reduce randomness over time so the agent stabilizes
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)