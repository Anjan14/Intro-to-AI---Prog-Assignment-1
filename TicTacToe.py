import math
'''
Housekeeping:
    Board: 3x3 grid
    Players: AI (X) and Human (O)
    Initial State: Empty board
    Goal State: 3 in a row for either player or a draw
    Actions: [1-9] (1-9 positions on the board)
    All Possible Win States: [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                                (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                                (0, 4, 8), (2, 4, 6)]
'''
def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    Args:
        board (list): List representing the Tic-Tac-Toe board.
    Return:
        None
    """
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("-" * 9)
    print("\n")


def check_winner(board, player):
    """
    Function to check which player (AI or Human) has won the game.
    Args:
        board (list): List representing the Tic-Tac-Toe board.
        player (str): Player to check for win.
    Return:
        bool: True if the player has won, False otherwise.
    """
    win_states = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_states)


def is_full(board):
    """
    Function to check if the board is full.
    Args:
        board (list): List representing the Tic-Tac-Toe board.
    Return:
        bool: True if the board is full, False otherwise.
    """
    return all(spot != ' ' for spot in board)


def minimax(board, depth, alpha, beta, is_maximizing):
    """
    Function to implement the Minimax algorithm. Optimized using Alpha-Beta Pruning.
    Args:
        board (list): List representing the Tic-Tac-Toe board.
        depth (int): Depth of the game tree.
        alpha (int): Alpha value for pruning.
        beta (int): Beta value for pruning.
        is_maximizing (bool): Flag to indicate if the current player is maximizing or minimizing.
    Return:
        int: Score of the best move.
    """
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return min_eval


def best_move(board):
    """
    Function to find the best move for the AI using the Minimax algorithm.
    Args:
        board (list): List representing the Tic-Tac-Toe board.
    Return:
        int: Best move for the AI.
    """
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


def tic_tac_toe():
    """
    Function to play the Tic-Tac-Toe game.
    Args:
        None
    Return:
        None
    """
    board = [' '] * 9
    print("Tic-Tac-Toe: AI (X) vs Human (O)")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            move = best_move(board)
            print("AI chooses position:", move + 1)
            board[move] = 'X'
        else:
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if board[move] == ' ':
                        board[move] = 'O'
                        break
                    else:
                        print("Invalid move. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter a number between 1-9.")

        print_board(board)

        if check_winner(board, 'X'):
            print("AI wins!")
            return
        if check_winner(board, 'O'):
            print("You win!")
            return

    print("It's a draw!")


tic_tac_toe()
