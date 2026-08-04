def insert_updated_score(board, score):
    board = board[:]
    board.append(score)
    i = len(board) - 2
    while i >= 0 and board[i] < score:
        board[i + 1] = board[i]
        i -= 1
    board[i + 1] = score
    return board, len(board) - 2 - i

board = [980, 875, 760, 690, 500]
print(insert_updated_score(board, 820))