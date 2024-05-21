from collections import deque

def person_is_seller(name):
    # Проверяем, заканчивается ли имя на 'm'
    return name[-1] == 'm'

def bfs(graph, start):
    # Создаем новую очередь для поиска
    search_queue = deque()
    # Добавляем всех соседей начальной вершины в очередь
    search_queue += graph[start]
    # Множество для отслеживания уже проверенных людей
    checked = set()
    
    while search_queue:
        # Извлекаем первого человека из очереди
        person = search_queue.popleft()
        # Проверяем, не проверяли ли уже этого человека
        if person not in checked:
            # Если человек - продавец манго, возвращаем True
            if person_is_seller(person):
                return person + " is a mango seller!"
            else:
                # Добавляем всех друзей человека в очередь
                search_queue += graph[person]
                # Помечаем человека как проверенного
                checked.add(person)
    
    # Если ни один продавец манго не найден
    return "No mango seller found."

# Граф друзей
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

# Начинаем поиск с вершины "you"
result = bfs(graph, 'you')
print(result)
