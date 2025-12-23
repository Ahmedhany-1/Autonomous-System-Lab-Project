# 🧠 RL vs DSA: Intelligent Maze Solver

### A Comparative Simulation: Classical Algorithms vs. Reinforcement Learning

## 📖 Overview

This project is an interactive simulation designed to compare two distinct approaches to pathfinding:

1. **Classical Data Structures (DSA):** Using **Breadth-First Search (BFS)** to calculate the mathematically optimal path instantly.
2. **Artificial Intelligence (RL):** Using **Q-Learning (Reinforcement Learning)** to train an autonomous agent that learns to navigate the maze through trial and error.

The application allows users to visualize the difference between "computing" a path (checking nodes) and "learning" a behavior (optimizing steps).

## ✨ Key Features

* **Interactive Environment:** fully playable Maze Game built with PyGame.
* **Dual Solvers:**
* **BFS Solver:** Visualizes the shortest path instantly (Yellow).
* **RL Agent:** Visualizes the learning process in real-time (Red).


* **Real-Time Analytics:** Compares "BFS Operations" (computational cost) vs. "AI Steps" (movement efficiency).
* **Turbo Mode:** Speed up training by 100x to see instant convergence.
* **Infinite Levels:** Procedurally generated mazes ensures the AI learns general logic, not just one map.

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/rl-maze-solver.git
cd rl-maze-solver

```


2. **Install dependencies:**
This project requires `pygame` for the GUI and `numpy` for matrix operations.
```bash
pip install pygame numpy

```


3. **Run the simulation:**
```bash
python main.py

```



## 🎮 Controls

| Key | Action | Description |
| --- | --- | --- |
| **⬆️ ⬇️ ⬅️ ➡️** | **Manual Move** | Control the Blue agent manually to test the maze physics. |
| **SPACE** | **Run BFS** | Calculate and display the optimal path (Yellow) using Breadth-First Search. |
| **T** | **Train AI** | Toggle Q-Learning training mode. Watch the agent learn from scratch. |
| **F** | **Turbo Mode** | Toggle fast-forward (disable rendering) to speed up training. |
| **N** | **New Maze** | Generate a new random maze and reset the agent's memory. |

## 🧠 How It Works

### 1. The Environment (DSA)

The maze is represented as a **2D Grid (Matrix)** where `0` is a path and `1` is a wall.

* **Files:** `environment.py`, `settings.py`
* **Logic:** The environment handles state transitions, collision detection, and reward assignment (+100 for Goal, -5 for Wall).

### 2. The Algorithmic Solver (BFS)

We use **Breadth-First Search** to guarantee the shortest path.

* **File:** `algorithms.py`
* **Metric:** We track **"Operations"** (how many grid cells the algorithm had to check) to measure computational cost.

### 3. The AI Agent (Q-Learning)

The agent uses a **Q-Table** to store the value of every action in every state.

* **File:** `rl_agent.py`
* **Equation:** The agent updates its knowledge using the Bellman Equation:


* **Metric:** We track **"Steps"**. As training progresses, the AI's step count converges to match the BFS path length exactly.

## 📂 Project Structure

```bash
.
├── main.py           # The Game Loop, GUI, and Input Handling
├── environment.py    # The Maze Logic (Matrix & Physics)
├── algorithms.py     # BFS Implementation (The Benchmark)
├── rl_agent.py       # Q-Learning Implementation (The Brain)
├── settings.py       # Constants, Colors, and Configuration
└── README.md         # Documentation

```

## 🚀 Future Improvements

* Add Deep Q-Networks (DQN) for complex input states.
* Implement A* Search to compare heuristic performance against BFS.
* Add dynamic obstacles (moving enemies).


---

*This project was developed as a final lab assignment for the Reinforcement Learning course.*
