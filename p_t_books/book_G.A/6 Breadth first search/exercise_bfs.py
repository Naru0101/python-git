from collections import deque

def topological_sort(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        for neighbor in graph[current_node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result

sorted_family_tree = topological_sort(family_tree)
print(sorted_family_tree)

family_tree = {
    "Adam": ["Cain", "Abel"],
    "Eve": ["Cain", "Abel"],
    "Cain": ["Enoch"],
    "Abel": ["Seth"],
    "Enoch": ["Irad"],
    "Seth": ["Enos"],
    "Enos": ["Cainan"],
    "Cainan": ["Mahalaleel"],
    "Mahalaleel": ["Jared"],
    "Jared": ["Enoch", "Methuselah"],
    "Methuselah": ["Lamech"],
    "Lamech": ["Noah"],
    "Noah": ["Shem", "Ham", "Japheth"]
}