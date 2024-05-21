def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования:
print(factorial(5))  # Выведет: 120
