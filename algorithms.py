# algorithms.py
import collections
from settings import *

class BFSSolver:
    def solve(self, grid, start, goal):
        """
        Returns: (path_list, operations_count)
        """
        queue = collections.deque([[start]])
        visited = set()
        visited.add(start)
        
        operations = 0 # Counter for "Thinking Steps"

        while queue:
            operations += 1 # We are processing a node
            path = queue.popleft()
            r, c = path[-1]

            if (r, c) == goal:
                return path, operations # Return both!

            neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            
            for nr, nc in neighbors:
                operations += 1 # We are checking a neighbor
                
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    grid[nr, nc] != 1 and (nr, nc) not in visited):
                    
                    visited.add((nr, nc))
                    new_path = list(path)
                    new_path.append((nr, nc))
                    queue.append(new_path)
                    
        return [], operations