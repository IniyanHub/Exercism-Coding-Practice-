def gamestate(board):
    def check_winner(player):
        # Rows and Columns
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True

        # Diagonals
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    # Count X and O
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    # Rule 1: Turn order
    if x_count < o_count:
        raise ValueError("Wrong turn order: O started")

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    # Check winners
    x_win = check_winner('X')
    o_win = check_winner('O')

    # ❗ FIXED MESSAGE HERE
    if x_win and o_win:
        raise ValueError("Impossible board: game should have ended after the game was won")

    # Validate win states
    if x_win:
        if x_count != o_count + 1:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    if o_win:
        if x_count != o_count:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"

    # Draw
    if x_count + o_count == 9:
        return "draw"

    return "ongoing"