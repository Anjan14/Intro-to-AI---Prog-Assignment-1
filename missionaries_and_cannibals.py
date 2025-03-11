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
'''

class MissionariesAndCannibals:
    def __init__(self, missionaries, cannibals, boat, path):
        self.missionaries = missionaries
        self. cannibals = cannibals
        self.boat = boat
        self.path = path

    def check_problem_validity(self, missionaries, cannibals):
        if missionaries < 0 or cannibals < 0:
            return False
        elif missionaries > 3 and cannibals > 3:
            return False
        elif missionaries < cannibals and missionaries > 0:
            return False
        elif missionaries > cannibals and missionaries < 3:
            return False
        else:
            return True

    def check_goal_state(self, missionaries, cannibals):
        if missionaries == 0 and cannibals == 0:
            return True
        else:
            return False

    def check_path_validity(self, path):
        if path == []:
            return True
        else:
            return False

    def check_path_repetition(self, path, state):
        if state in path:
            return False
        else:
            return True

    def check_boat_capacity(self, boat):
        if boat == 0:
            return True
        else:
            return False

    def check_boat_capacity_2(self, boat):
        if boat == 1:
            return True
        else:
            return False

    def check_boat_capacity_3(self, boat):
        if boat == 2:
            return True
        else:
            return False

    def check_boat_capacity_4(self, boat):
        if boat >= 3:
            return False
        else:
            return True

    def check_boat_capacity_5(self, boat):
        if boat <= 2:
            return True
        else:
            return False

    def get_next_states(self):
        moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]
        next_states = []
        for move in moves:
            next_state = (self.missionaries + move[0], self.cannibals + move[1], self.boat - 1)
            if self.check_problem_validity(next_state[0], next_state[1]):
                next_states.append(next_state)
