from collections import deque

def person_is_seller(name):
    # Пример: человек считается продавцом манго, если его имя содержит подстроку "mango"
    return "mango" in name.lower()

def search(name):

    search_queue = deque()

    search_queue += graph[name]

    searched = []   # Этот массив используется для отслеживания уже проверенных людей

    while search_queue:

        person = search_queue.popleft()

        if not person in searched:   # Человек проверяется только в том случае, если он не проверялся ранее

            if person_is_seller(person):

                print(person + " is a mango seller!")

                return True

            else:

                search_queue += graph[person]

                searched.append(person)      # Человек помечается как уже проверенный

    return False

# Пример графа друзей
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

search("you")
