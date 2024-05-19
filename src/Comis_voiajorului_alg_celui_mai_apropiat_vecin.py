def nearest_neighbor(graph, start):
    num_cities = len(graph)  # Numarul total de orase
    visited = set()  # Un set pentru a urmari orasele deja vizitate
    path = [start]  # Lista pentru a stoca traseul parcurgerii
    visited.add(start)  # Adauga orasul de start in setul de orase vizitate
    while len(path) < num_cities:  # Continua pana cand toate orasele sunt vizitate
        current_city = path[-1]  # Orasul curent este ultimul oras adaugat in traseu
        nearest_city = None  # Initial, cel mai apropiat oras este necunoscut
        min_distance = float('inf')  # Initial, distanta minima este infinit
        for next_city in range(num_cities):  # Parcurge toate orasele
            if next_city not in visited and graph[current_city][next_city] < min_distance:
                # Verifica daca orasul urmator nu a fost vizitat si are o distanta mai mica
                nearest_city = next_city  # Actualizeaza cel mai apropiat oras
                min_distance = graph[current_city][next_city]  # Actualizeaza distanta minima
        if nearest_city is not None:  # Daca s-a gasit un oras nevizitat
            path.append(nearest_city)  # Adauga acest oras in traseu
            visited.add(nearest_city)  # Marcheaza orasul ca vizitat
    return path  # Returneaza traseul parcurgerii
