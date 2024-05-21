def knapsack(items, max_weight):
    # items - список кортежей вида (вес, стоимость)
    # max_weight - максимальный вес рюкзака

    # Для хранения максимальной стоимости при каждом возможном весе рюкзака
    dp = [0] * (max_weight * 2 + 1)

    for weight, value in items:
        for w in range(max_weight * 2, int(weight * 2) - 1, -1):
            dp[w] = max(dp[w], dp[w - int(weight * 2)] + value)
    
    return dp[max_weight * 2]

items = [(4, 3000), (3, 2000), (1, 1500), (1, 2000)]
max_weight = 4

print("Максимальная стоимость рюкзака:", knapsack(items, max_weight))