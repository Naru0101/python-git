from collections import deque

# Граф представлен в виде словаря смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

def bfs(graph, start, goal):
    # Очередь для поиска в ширину
    queue = deque()
    # Множество для отслеживания посещенных вершин
    visited = set()
    # Начальная вершина и путь до нее
    queue.append((start, [start]))

    while queue:
        # Извлекаем вершину из очереди
        current, path = queue.popleft()
        # Помечаем вершину как посещенную
        visited.add(current)
        # Если мы достигли целевой вершины, возвращаем путь до нее
        if current == goal:
            return path
        # Проходим по соседним вершинам
        for neighbor in graph[current]:
            # Если соседняя вершина еще не посещена, добавляем ее в очередь
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # Если целевая вершина недостижима
    return "Целевая вершина недостижима"

# Пример использования
start_vertex = 'A'
goal_vertex = 'I'
shortest_path = bfs(graph, start_vertex, goal_vertex)
print("Кратчайший путь из вершины", start_vertex, "в вершину", goal_vertex, ":", shortest_path)
