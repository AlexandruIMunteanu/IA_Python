def nearest_neighbor(graph, start):
    
    start = 0
    # Exemplu de input
    graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]]

    num_cities = len(graph)
    visited = set()
    path = [start]
    visited.add(start)
    while len(path) < num_cities:
        current_city = path[-1]
        nearest_city = None
        min_distance = float('inf')
        for next_city in range(num_cities):
            if next_city not in visited and graph[current_city][next_city] < min_distance:
                nearest_city = next_city
                min_distance = graph[current_city][next_city]
        if nearest_city is not None:
            path.append(nearest_city)
            visited.add(nearest_city)
    print("Traseul optim:", path)
    return path

