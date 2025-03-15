import random
import matplotlib.pyplot as plt

# 8-Puzzle Functions
def find_blank(state):
    """
    Function to find the blank tile in the puzzle.
    Args:
        state (list): Current state of the puzzle.
    Returns:
        tuple: Position of the blank tile.
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None

def manhattan_distance(state):
    """
    Function to calculate the Manhattan distance heuristic of the 8-puzzle state.
    Args:
        state (list): Current state of the puzzle.
    Returns:
        int: Manhattan distance heuristic value.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

def generate_initial_puzzle():
    """
    Function to generate a random initial state for the 8-puzzle.
    Args:
        None
    Returns:
        list: Random initial state of the 8-puzzle.
    """
    state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for _ in range(1000):
        blank_row, blank_col = find_blank(state)
        directions = []
        if blank_row > 0:
            directions.append((-1, 0))
        if blank_row < 2:
            directions.append((1, 0))
        if blank_col > 0:
            directions.append((0, -1))
        if blank_col < 2:
            directions.append((0, 1))
        if directions:
            dr, dc = random.choice(directions)
            new_row = blank_row + dr
            new_col = blank_col + dc
            state[blank_row][blank_col], state[new_row][new_col] = state[new_row][new_col], state[blank_row][blank_col]
    return state

def get_puzzle_neighbors(state):
    """
    Function to get the neighboring states of the current 8-puzzle state.
    Args:
        state (list): Current state of the puzzle.
    Returns:
        list: List of neighboring states.
    """
    neighbors = []
    blank_row, blank_col = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dr, dc in directions:
        new_row = blank_row + dr
        new_col = blank_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row.copy() for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)
    return neighbors

def hill_climbing_puzzle(initial_state):
    """
    Function to solve the 8-puzzle using hill climbing with random restarts.
    Args:
        initial_state (list): Initial state of the 8-puzzle.
    Returns:
        int: Minimum cost found by the algorithm.
        list: State of the puzzle with the minimum cost.
    """
    current_state = [row.copy() for row in initial_state]
    current_cost = manhattan_distance(current_state)
    best_state = [row.copy() for row in current_state]
    best_cost = current_cost
    while True:
        neighbors = get_puzzle_neighbors(current_state)
        if not neighbors:
            break
        min_neighbor_cost = current_cost
        best_neighbor = current_state
        for neighbor in neighbors:
            cost = manhattan_distance(neighbor)
            if cost < min_neighbor_cost:
                min_neighbor_cost = cost
                best_neighbor = neighbor
        if min_neighbor_cost < current_cost:
            current_state = best_neighbor
            current_cost = min_neighbor_cost
            if current_cost < best_cost:
                best_cost = current_cost
                best_state = [row.copy() for row in current_state]
        else:
            break
    return best_cost, best_state

# 8-Queens Functions
def attacking_pairs(state):
    """
    Function to calculate the number of attacking pairs in the 8-queens state.
    Args:
        state (list): Current state of the 8-queens.
    Returns:
        int: Number of attacking pairs in the state.
    """
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def generate_initial_queens():
    """
    Function to generate a random initial state for the 8-queens.
    Args:
        None
    Returns:
        list: Random initial state of the 8-queens.
    """
    return random.sample(range(8), 8)

def get_queen_neighbors(state):
    """
    Function to get the neighboring states of the current 8-queens state.
    Args:
        state (list): Current state of the 8-queens.
    Returns:
        list: List of neighboring states
    """
    neighbors = []
    for col in range(8):
        current_row = state[col]
        for row in range(8):
            if row != current_row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing_queens(initial_state):
    """
    Function to solve the 8-queens using hill climbing with random restarts.
    Args:
        initial_state (list): Initial state of the 8-queens.
    Returns:
        int: Minimum cost found by the algorithm.
        list: State of the 8-queens with the minimum cost.
    """
    current_state = initial_state.copy()
    current_cost = attacking_pairs(current_state)
    best_state = current_state.copy()
    best_cost = current_cost
    while True:
        neighbors = get_queen_neighbors(current_state)
        min_neighbor_cost = current_cost
        best_neighbor = current_state
        for neighbor in neighbors:
            cost = attacking_pairs(neighbor)
            if cost < min_neighbor_cost:
                min_neighbor_cost = cost
                best_neighbor = neighbor.copy()
        if min_neighbor_cost < current_cost:
            current_state = best_neighbor
            current_cost = min_neighbor_cost
            if current_cost < best_cost:
                best_cost = current_cost
                best_state = current_state.copy()
        else:
            break
    return best_cost, best_state

# Running Experiments and Plotting
def run_experiment(problem, iterations):
    """
    Function to run the hill climbing with random restarts experiment.
    Args:
        problem (str): Problem to solve ('puzzle' or 'queens').
        iterations (int): Number of iterations to run.
    Returns:
        list: List of best costs found at each iteration.
    """
    best_costs = []
    best_so_far = float('inf')
    for i in range(iterations):
        if problem == 'puzzle':
            initial = generate_initial_puzzle()
            cost, _ = hill_climbing_puzzle(initial)
        elif problem == 'queens':
            initial = generate_initial_queens()
            cost, _ = hill_climbing_queens(initial)
        if cost < best_so_far:
            best_so_far = cost
        best_costs.append(best_so_far)
    return best_costs

iterations = 1000

# Run experiments
puzzle_costs = run_experiment('puzzle', iterations)
queens_costs = run_experiment('queens', iterations)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(range(iterations), puzzle_costs, label='8-Puzzle (Manhattan Distance)')
plt.xlabel('Iteration')
plt.ylabel('Best Cost')
plt.title('8-Puzzle: Hill Climbing with Random Restarts')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(range(iterations), queens_costs, label='8-Queens (Attacking Pairs)')
plt.xlabel('Iteration')
plt.ylabel('Best Cost')
plt.title('8-Queens: Hill Climbing with Random Restarts')
plt.grid(True)
plt.show()