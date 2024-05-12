def is_safe(board, row, col, N):
    # Verifică dacă o regină poate fi plasată pe poziția (row, col)
    # Verifică dacă există vreo regină pe aceeași coloană
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Verifică dacă există vreo regină pe diagonala stânga sus
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Verifică dacă există vreo regină pe diagonala dreapta sus
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, N):
    # Dacă toate reginele sunt plasate, True
    if row >= N:
        return True
    
    # Încercăm să plasăm regina pe fiecare coloană în rândul curent
    for i in range(N):
        if is_safe(board, row, i, N):
            # Dacă poziția este sigură, plasăm regina
            board[row][i] = 1
            
            # Apelăm recursiv pentru a plasa reginele rămase
            if solve_n_queens_util(board, row + 1, N):
                return True
            
            # Dacă nu putem plasa regina în această poziție, o scoatem
            board[row][i] = 0
    
    # Dacă nu putem plasa regina în nicio poziție din această coloană, returnăm False
    return False

def solve_n_queens(N):
    # Inițializăm tabla de șah cu toate pozițiile pe 0
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Apelăm funcția auxiliară pentru a rezolva problema
    if not solve_n_queens_util(board, 0, N):
        print("Nu există soluție")
        return False
    
    # Afisăm tabla de șah cu reginele plasate
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 1:
                print(" Q |", end="")
            else:
                print(" - |", end="")
        print("\n+" + "-" * (N * 4 + 1) + "+")
    
    return True
