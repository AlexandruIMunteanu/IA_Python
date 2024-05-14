import sys

def tsp_backtracking(graph, path, visited, cost, current_city, start_city, min_cost, min_path):
    if len(visited) == len(graph):
        if cost + graph[current_city][start_city] < min_cost[0]:
            min_cost[0] = cost + graph[current_city][start_city]
            min_path[0] = path[:] + [start_city]
    else:
        for next_city in range(len(graph)):
            if next_city not in visited:
                path.append(next_city)
                visited.add(next_city)
                tsp_backtracking(graph, path, visited, cost + graph[current_city][next_city], next_city, start_city, min_cost, min_path)
                visited.remove(next_city)
                path.pop()

def tsp(graph):
    num_cities = len(graph)
    min_cost = [sys.maxsize]
    min_path = [[]]
    for start_city in range(num_cities):
        tsp_backtracking(graph, [start_city], {start_city}, 0, start_city, start_city, min_cost, min_path)
    print("Costul minim:", min_cost[0])
    print("Traseul minim:", min_path[0])
    return min_cost[0], min_path[0]

# Exemplu de input
# graph = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

