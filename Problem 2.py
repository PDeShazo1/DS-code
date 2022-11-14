
def hanoi(rings, i, j, k, moves):
    if rings == 1:
        moves.append((i, k))
    else:
        hanoi(rings-1, i, k, j, moves)
    moves.append((i, k))
    hanoi(rings-1, j, i, k, moves)
    return moves
moves = hanoi(7, 'A', 'B', 'C', [])