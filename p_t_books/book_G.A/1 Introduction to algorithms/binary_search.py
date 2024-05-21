def binary(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

# Пример использования
my_list = [1, 3, 5, 7, 9]
print(binary(my_list, 3))  # => 1
print(binary(my_list, -1)) # => None
