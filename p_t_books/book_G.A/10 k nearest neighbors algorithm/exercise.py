#10.1
import numpy as np
from sklearn.prepr0.ocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Пример данных: оценки пользователей по фильмам
user_ratings = {
    'Yogi': [5, 5, 5, 4, 4, 3],
    'Pinky': [5, 4, 3, 5, 4, 3],
    'User1': [1, 2, 1, 3, 2, 4],
    'User2': [2, 1, 2, 1, 3, 2],
    'User3': [4, 3, 5, 2, 1, 4],
    'Priyanka': [4, 5, 3, 2, 4, 5]
}

# Преобразование данных в массив numpy
user_names = list(user_ratings.keys())
ratings_matrix = np.array(list(user_ratings.values()))

# Нормализация оценок пользователей
scaler = StandardScaler()
normalized_ratings = scaler.fit_transform(ratings_matrix.T).T

# Поиск пяти ближайших соседей для Приянки
priyanka_index = user_names.index('Priyanka')
priyanka_ratings = normalized_ratings[priyanka_index].reshape(1, -1)

# Обучение модели k-NN
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(normalized_ratings)

# Поиск ближайших соседей
distances, indices = knn.kneighbors(priyanka_ratings)

# Получение имен ближайших пользователей
nearest_neighbors = [user_names[idx] for idx in indices.flatten() if user_names[idx] != 'Priyanka']

print("Пять ближайших пользователей к Приянке:", nearest_neighbors)

#10.2
