from sklearn.neighbors import KNeighborsClassifier

# Подготовка данных об апельсинах и грейпфрутах
X_train = [[5.4, 2.3], [6.2, 2.8], [7.5, 3.4], [6.0, 3.0], [6.8, 3.2], [7.2, 3.6]]  # Данные об апельсинах и грейпфрутах (длина, ширина)
y_train = ['апельсин', 'апельсин', 'грейпфрут', 'апельсин', 'грейпфрут', 'грейпфрут']  # Метки классов (апельсин или грейпфрут)

# Создание модели k ближайших соседей
k = 3  # Количество соседей
knn_model = KNeighborsClassifier(n_neighbors=k)

# Обучение модели
knn_model.fit(X_train, y_train)

# Теперь у нас есть обученная модель, которая может классифицировать новые фрукты

# Проверка на новых данных
fruit_to_classify = [[6.5, 3.0]]  # Новый фрукт, который нужно классифицировать (длина, ширина)
predicted_class = knn_model.predict(fruit_to_classify)

# Вывод результата классификации
print("Этот фрукт -", predicted_class[0])
