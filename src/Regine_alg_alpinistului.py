import random

def generate_board(size):
    """Genereaza un tablou de sah aleator."""
    board = []
    for _ in range(size):
        board.append(random.randint(0, size-1))
    return board

def count_conflicts(board):
    """Calculeaza numarul de conflicte intre regine pe tabloul de sah."""
    conflicts = 0
    size = len(board)
    for i in range(size):
        for j in range(i+1, size):
            # Verifica daca doua regine sunt pe aceeasi coloana sau pe aceeasi diagonala
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def move_queen(board, column, step):
    """Muta o regina pe o coloana data cu un numar de pozitii specificat."""
    size = len(board)
    # Muta regina in sus pe coloana, luand in considerare incadrarea circulara
    board[column] = (board[column] + step) % size

def hill_climbing(size):
    """Implementeaza algoritmul Hill Climbing pentru problema reginelor."""
    # Genereaza un tablou de sah aleator
    board = generate_board(size)
    # Calculeaza numarul de conflicte pe tabloul initial
    conflicts = count_conflicts(board)

    # Continua cautarea solutiei pana cand nu mai exista conflicte
    while conflicts > 0:
        best_move = None
        best_conflicts = conflicts

        # Parcurge fiecare coloana a tabloului de sah
        for column in range(size):
            current_row = board[column]

            # Incearca sa mute regina pe coloana in sus
            for step in range(1, size):
                # Muta regina si calculeaza noile conflicte
                move_queen(board, column, step)
                new_conflicts = count_conflicts(board)

                # Verifica daca mutarea a redus numarul de conflicte
                if new_conflicts < best_conflicts:
                    best_move = (column, step)
                    best_conflicts = new_conflicts

                # Anuleaza mutarea pentru a reveni la starea initiala a tabloului
                move_queen(board, column, -step)

        # Daca nu se gaseste nicio miscare pentru a reduce conflictele, opreste cautarea
        if best_move is None:
            break

        # Aplica cea mai buna mutare gasita pentru a reduce conflictele
        move_queen(board, best_move[0], best_move[1])
        conflicts = best_conflicts

    # Returneaza tabloul de sah cu pozitionarea reginelor
    return board
