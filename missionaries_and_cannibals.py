from collections import deque
from collections import defaultdict

'''
Housekeeping:
    Missionaries (M) = 3
    Cannibals (C) = 3
    Boat (B) = 1

    Boat Capacity = 1 or 2

    Missionaries >= Cannibals

    Initial State: (3, 3, 1)
    Goal State: (0, 0, 0)

    Actions: [M], [M, M], [M, C], [C], [C, C]

Solution:
    1. BFS is best for the solution for this problem because it 
    explores all possible moves level by level, and is guaranteed 
    to find the shortest path.

    2. The solution is found by exploring all possible states. DFS
    can get stuck in a loop and not find the solution. Also, the state 
    space is small enough to use BFS.

    3. Since, the state space is small, the time and space complexity is 
    constant. The maximum number of states is 36 (3 * 3 * 2) and the maximum
    number of actions is 5.

Please note:
    Answer to question 3 is in the comments below the code.
'''


class MissionariesAndCannibals:
    """
    Class to represent the Missionaries and Cannibals problem.

    Attributes:
        missionaries (int): Number of missionaries on the starting side.
        cannibals (int): Number of cannibals on the starting side.
        boat (int): Location of the boat (1 for starting side, 0 for goal side).
        path (list): List of actions taken to reach the current state.
    """

    def __init__(self, missionaries, cannibals, boat, path=None):
        """
        Constructor for the MissionariesAndCannibals class.
        Args:
            missionaries (int): Number of missionaries on the starting side.
            cannibals (int): Number of cannibals on the starting side.
            boat (int): Location of the boat (1 for starting side, 0 for goal side).
            path (list): List of actions taken to reach the current state.
        """
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.path = path or []

    def check_problem_validity(self):
        """
        Check if the given state is valid.
        Returns:
            bool: True if the state is valid, False otherwise.
        """
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if (3 - self.missionaries) < (3 - self.cannibals) and (3 - self.missionaries) > 0:
            return False
        return True

    def check_goal_state(self):
        """
        Check if the current state is the goal state.
        Returns:
            bool: True if the current state is the goal state, False otherwise.
        """
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_next_states(self):
        """
        Get the next possible states from the current state.
        Returns:
            list: List of next possible states.
        """
        moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]
        next_states = []

        for m, c in moves:
            if self.boat == 1:  # Boat on the starting side
                new_state = MissionariesAndCannibals(self.missionaries - m, self.cannibals - c, 0,
                                                     self.path + [(m, c, '→')])
            else:  # Boat on the goal side
                new_state = MissionariesAndCannibals(self.missionaries + m, self.cannibals + c, 1,
                                                     self.path + [(m, c, '←')])

            if new_state.check_problem_validity():
                next_states.append(new_state)

        return next_states


def bfs():
    """
    Perform a Breadth-First Search to find the solution to the Missionaries and Cannibals problem.
    Returns:
        list: List of actions taken to reach the goal state.
    """
    initial_state = MissionariesAndCannibals(3, 3, 1)
    queue = deque([initial_state])
    visited = set()

    while queue:
        state = queue.popleft()
        if state.check_goal_state():
            return state.path  # Return the optimal path

        visited.add((state.missionaries, state.cannibals, state.boat))

        for next_state in state.get_next_states():
            if (next_state.missionaries, next_state.cannibals, next_state.boat) not in visited:
                queue.append(next_state)

    return None

# Get and print optimal solution path
solution = bfs()
print("Optimal Path (M, C, Direction):", solution)

'''
Answer to question 3:
    Yes, it is a good idea to check for repeated states in the BFS algorithm.
    1. Checking for repeated states ensures that the algorithm does not get stuck in a loop.
    2. It also ensures that the algorithm does not explore the same state multiple times, 
        which can be computationally expensive.
    3. Checking repeated states ensures optimality of the solution. 
'''