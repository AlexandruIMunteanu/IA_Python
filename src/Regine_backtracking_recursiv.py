def is_safe(board, row, col, N):
    # Verifica daca o regina poate fi plasata pe pozitia (row, col)
    # Verifica daca exista vreo regina pe aceeasi coloana
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Verifica daca exista vreo regina pe diagonala stanga sus
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Verifica daca exista vreo regina pe diagonala dreapta sus
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, N):
    # Daca toate reginele sunt plasate, True
    if row >= N:
        return True
    
    # Incercam sa plasam regina pe fiecare coloana in randul curent
    for i in range(N):
        if is_safe(board, row, i, N):
            # Daca pozitia este sigura, plasam regina
            board[row][i] = 1
            
            # Apelam recursiv pentru a plasa reginele ramase
            if solve_n_queens_util(board, row + 1, N):
                return True
            
            # Daca nu putem plasa regina in aceasta pozitie, o scoatem
            board[row][i] = 0
    
    # Daca nu putem plasa regina in nicio pozitie din aceasta coloana, returnam False
    return False

def solve_n_queens(N):
    # Initializam tabla de sah cu toate pozitiile pe 0
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Apelam functia auxiliara pentru a rezolva problema
    if not solve_n_queens_util(board, 0, N):
        print("Nu exista solutie")
        return None
    
    return board
