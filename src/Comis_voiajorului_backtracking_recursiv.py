import sys

def tsp_backtracking(graph, path, visited, cost, current_city, start_city, min_cost, min_path):
    if len(visited) == len(graph):  # Verifica daca toate orasele au fost vizitate
        if cost + graph[current_city][start_city] < min_cost[0]:  # Daca s-a format un ciclu si costul este mai mic decat minimul anterior
            min_cost[0] = cost + graph[current_city][start_city]  # Actualizeaza costul minim
            min_path[0] = path[:] + [start_city]  # Actualizeaza traseul minim
    else:
        for next_city in range(len(graph)):  # Parcurge toate orasele
            if next_city not in visited:  # Verifica daca orasul urmator nu a fost vizitat
                path.append(next_city)  # Adauga orasul urmator in traseu
                visited.add(next_city)  # Marcheaza orasul ca vizitat
                tsp_backtracking(graph, path, visited, cost + graph[current_city][next_city], next_city, start_city, min_cost, min_path)  # Apel recursiv pentru urmatorul oras
                visited.remove(next_city)  # Elimina orasul din lista de orase vizitate pentru a incerca alte posibilitati
                path.pop()  # Scoate orasul din traseu pentru a incerca alte posibilitati

def tsp(graph):
    num_cities = len(graph)  # Numarul total de orase
    min_cost = [sys.maxsize]  # Initial, costul minim este infinit
    min_path = [[]]  # Traseul minim este gol initial
    for start_city in range(num_cities):  # Pentru fiecare oras ca oras de start
        tsp_backtracking(graph, [start_city], {start_city}, 0, start_city, start_city, min_cost, min_path)  # Aplica algoritmul de backtracking
    return min_cost[0], min_path[0]  # Returneaza costul minim si traseul minim gasite
