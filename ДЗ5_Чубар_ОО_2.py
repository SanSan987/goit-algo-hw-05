def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0   # для підрахування кількості ітерацій
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])

        if arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    # Якщо не знайшли точного значення, повернемо "верхню межу"
    return (iterations, upper_bound)

# Тестуємо:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
target_value = 4.0

result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")  # Кількість ітерацій: 4, Верхня межа: 4.4
