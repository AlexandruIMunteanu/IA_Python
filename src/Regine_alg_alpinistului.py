import random

def generate_board(size):
    """Generează un tablou de șah aleator."""
    board = []
    for _ in range(size):
        board.append(random.randint(0, size-1))
    return board

def count_conflicts(board):
    """Calculează numărul de conflicte între regine pe tabloul de șah."""
    conflicts = 0
    size = len(board)
    for i in range(size):
        for j in range(i+1, size):
            # Verifică dacă două regine sunt pe aceeași coloană sau pe aceeași diagonală
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def move_queen(board, column, step):
    """Mută o regină pe o coloană dată cu un număr de poziții specificat."""
    size = len(board)
    # Mută regina în sus pe coloană, luând în considerare încadrarea circulară
    board[column] = (board[column] + step) % size

def hill_climbing(size):
    """Implementează algoritmul Hill Climbing pentru problema reginelor."""
    # Generează un tablou de șah aleator
    board = generate_board(size)
    # Calculează numărul de conflicte pe tabloul inițial
    conflicts = count_conflicts(board)

    # Continuă căutarea soluției până când nu mai există conflicte
    while conflicts > 0:
        best_move = None
        best_conflicts = conflicts

        # Parcurge fiecare coloană a tabloului de șah
        for column in range(size):
            current_row = board[column]

            # Încercă să mute regina pe coloană în sus
            for step in range(1, size):
                # Mută regina și calculează noile conflicte
                move_queen(board, column, step)
                new_conflicts = count_conflicts(board)

                # Verifică dacă mutarea a redus numărul de conflicte
                if new_conflicts < best_conflicts:
                    best_move = (column, step)
                    best_conflicts = new_conflicts

                # Anulează mutarea pentru a reveni la starea inițială a tabloului
                move_queen(board, column, -step)

        # Dacă nu se găsește nicio mișcare pentru a reduce conflictele, oprește căutarea
        if best_move is None:
            break

        # Aplică cea mai bună mutare găsită pentru a reduce conflictele
        move_queen(board, best_move[0], best_move[1])
        conflicts = best_conflicts

    # Returnează tabloul de șah cu poziționarea reginelor
    return board
