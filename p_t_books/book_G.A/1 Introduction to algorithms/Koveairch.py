import itertools

def tsp_brute_force(graph):
    n = len(graph)
    min_cost = float('inf')
    min_path = None

    for path in itertools.permutations(range(n)):
        cost = 0
        for i in range(n):
            cost += graph[path[i - 1]][path[i]]
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

# Пример графа с расстояниями между городами
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_brute_force(graph)
print("Минимальный путь:", path)
print("Минимальная стоимость:", cost)
