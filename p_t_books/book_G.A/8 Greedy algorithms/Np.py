#/1/
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])

    return dp[n][capacity]

# Пример входных данных
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print(knapsack(weights, values, capacity))  # Вывод: максимальная сумма ценности при данной вместимости

#2/task/
def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover

# Пример входных данных
universe = set(range(1, 11))
subsets = [{1, 2, 3, 4, 5}, {2, 3, 5}, {4, 5, 7}, {6, 7, 8}, {8, 9, 10}]

print(set_cover(universe, subsets))  # Вывод: минимальное покрытие множеством подмножеств
