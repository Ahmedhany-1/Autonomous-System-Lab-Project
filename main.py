# main.py
import pygame
from settings import *
from environment import MazeEnvironment
from algorithms import BFSSolver
from rl_agent import QLearningAgent

class GameApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT + 50)) # Added 50px for Stats Bar
        pygame.display.set_caption("RL vs DSA - Final Project")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        
        self.env = MazeEnvironment()
        self.solver = BFSSolver()
        self.agent = QLearningAgent()
        
        # Statistics
        self.solution_path = []
        self.bfs_operations = 0
        self.bfs_path_len = 0
        
        self.training_mode = False
        self.episode_count = 0
        self.current_steps = 0 # Steps in current episode

    def draw_grid(self):
        # Draw the Stats Bar (Top 50 pixels)
        pygame.draw.rect(self.screen, (50, 50, 50), (0, 0, WIDTH, 50))
        
        # 1. DSA Stats Text
        dsa_text = f"DSA (BFS): Ops={self.bfs_operations} | Path={self.bfs_path_len}"
        img1 = self.font.render(dsa_text, True, YELLOW)
        self.screen.blit(img1, (10, 15))

        # 2. AI Stats Text
        ai_text = f"AI (RL): Ep={self.episode_count} | Steps={self.current_steps} | Eps={self.agent.epsilon:.2f}"
        color = RED if self.training_mode else WHITE
        img2 = self.font.render(ai_text, True, color)
        self.screen.blit(img2, (300, 15))

        # Draw the Grid (Shifted down by 50 pixels)
        offset_y = 50 
        pygame.draw.rect(self.screen, WHITE, (0, offset_y, WIDTH, HEIGHT))

        for r in range(ROWS):
            for c in range(COLS):
                rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE + offset_y, CELL_SIZE, CELL_SIZE)
                
                if self.env.grid[r, c] == 1:
                    pygame.draw.rect(self.screen, BLACK, rect)
                elif (r, c) == self.env.goal_pos:
                    pygame.draw.rect(self.screen, GREEN, rect)
                elif (r, c) in self.solution_path:
                    pygame.draw.rect(self.screen, YELLOW, rect)
                
                pygame.draw.rect(self.screen, GRAY, rect, 1)

        # Draw Agent
        agent_r, agent_c = self.env.agent_pos
        agent_rect = pygame.Rect(agent_c * CELL_SIZE, agent_r * CELL_SIZE + offset_y, CELL_SIZE, CELL_SIZE)
        color = RED if self.training_mode else BLUE
        pygame.draw.rect(self.screen, color, agent_rect)

    def run(self):
        running = True
        while running:
            # -------------------------------------------------
            # 1. AI Logic
            # -------------------------------------------------
            if self.training_mode:
                self.current_steps += 1
                state = tuple(self.env.agent_pos)
                action = self.agent.choose_action(state)
                next_pos, msg, done = self.env.step(action)
                next_state = tuple(next_pos)
                
                # Rewards
                if done:       reward = 100
                elif msg == "Hit Wall": reward = -5
                else:          reward = -1
                
                self.agent.learn(state, action, reward, next_state)
                
                # --- THE FIX: AUTO-STOP LOGIC ---
                if done:
                    self.agent.decay_epsilon()
                    
                    # If the AI is smart enough (less than 10% random moves)
                    # We STOP the training so you can see the result.
                    if self.agent.epsilon < 0.1: 
                        self.training_mode = False
                        print(f"🎉 AI CONVERGED! Final Path: {self.current_steps} Steps.")
                        # We do NOT reset the env here, so the agent stays at the goal
                        # and the 'Steps' counter stays visible.
                    else:
                        # If not smart yet, keep training
                        self.env.reset()
                        self.episode_count += 1
                        self.current_steps = 0
            
            # -------------------------------------------------
            # 2. Input Handling
            # -------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        self.training_mode = not self.training_mode
                        if self.training_mode:
                            # If we start training again, reset to start
                            self.env.reset()
                            self.current_steps = 0
                    
                    elif event.key == pygame.K_f:
                        self.turbo_mode = not getattr(self, 'turbo_mode', False)

                    elif event.key == pygame.K_n: # New Maze
                        self.env = MazeEnvironment()
                        self.agent = QLearningAgent()
                        self.solution_path = []
                        self.bfs_operations = 0
                        self.bfs_path_len = 0
                        self.episode_count = 0
                        self.current_steps = 0
                        self.training_mode = False

                    elif event.key == pygame.K_SPACE:
                        path, ops = self.solver.solve(self.env.grid, self.env.start_pos, self.env.goal_pos)
                        self.solution_path = path
                        self.bfs_operations = ops
                        self.bfs_path_len = len(path)

                    # Manual Control
                    if not self.training_mode:
                        action = -1
                        if event.key == pygame.K_UP: action = 0
                        elif event.key == pygame.K_DOWN: action = 1
                        elif event.key == pygame.K_LEFT: action = 2
                        elif event.key == pygame.K_RIGHT: action = 3
                        if action != -1: self.env.step(action)

            # -------------------------------------------------
            # 3. Rendering
            # -------------------------------------------------
            if not getattr(self, 'turbo_mode', False):
                self.draw_grid()
                pygame.display.flip()
                # Fast FPS for training, normal for manual
                fps = 60 if self.training_mode else 30
                self.clock.tick(fps)

        pygame.quit()

if __name__ == "__main__":
    game = GameApp()
    game.run()