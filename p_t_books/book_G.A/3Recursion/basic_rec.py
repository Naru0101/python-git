def countdown(i):
    print(i)
    if i <= 0:  # Базовый случай
        return
    else:  # Рекурсивный случай
        countdown(i - 1)

countdown(100)