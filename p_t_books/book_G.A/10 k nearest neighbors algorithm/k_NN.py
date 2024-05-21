import numpy as np
from sklearn.neighbors import NearestNeighbors

# Пример данных: координаты пользователей в многомерном пространстве, отражающие их вкусы
user_preferences = {
    'User1': [1.0, 2.0],
    'User2': [1.5, 1.8],
    'User3': [2.0, 1.0],
    'User4': [2.5, 2.0],
    'User5': [3.0, 3.5],
    'User6': [3.5, 4.0],
    'Priyanka': [2.1, 2.1]
}

# Преобразование данных в массив numpy
user_names = list(user_preferences.keys())
user_coords = np.array(list(user_preferences.values()))

# Поиск пяти ближайших соседей для Приянки
priyanka_index = user_names.index('Priyanka')
priyanka_coords = user_coords[priyanka_index].reshape(1, -1)

# Обучение модели k-NN
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(user_coords)

# Поиск ближайших соседей
distances, indices = knn.kneighbors(priyanka_coords)

# Получение имен ближайших пользователей
nearest_neighbors = [user_names[idx] for idx in indices.flatten() if user_names[idx] != 'Priyanka']

print("Пять ближайших пользователей к Приянке:", nearest_neighbors)
