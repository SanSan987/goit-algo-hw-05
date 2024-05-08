import timeit

# Алгоритм Бойєра-Мура
def boyer_moore_search(text, pattern):
    def preprocess_bad_char(pattern):
        bad_char = [-1] * 65536  # Збільшений розмір до 65536 для всіх символів Unicode
        for index, char in enumerate(pattern):
            bad_char[ord(char)] = index
        return bad_char

    bad_char = preprocess_bad_char(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    shifts = 0

    while shifts <= text_length - pattern_length:
        j = pattern_length - 1

        while j >= 0 and pattern[j] == text[shifts + j]:
            j -= 1

        if j < 0:
            return shifts  
        else:
            shift_value = bad_char[ord(text[shifts + j])]
            shifts += max(1, j - shift_value if shift_value != -1 else j + 1)

    return -1  

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        length = 0
        lps = [0] * len(pattern)
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1

        if pattern_index == len(pattern):
            return text_index - pattern_index 
        elif text_index < len(text) and pattern[pattern_index] != text[text_index]:
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1

    return -1 

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern):
    base = 256
    prime = 101
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(pattern_length - 1):
        h = (h * base) % prime

    for i in range(pattern_length):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if text[i:i + pattern_length] == pattern:
                return i 

        if i < text_length - pattern_length:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime
            if text_hash < 0:
                text_hash += prime

    return -1 

# Вимірювання часу пошуку
def measure_search_time(search_function, text, pattern):
    return timeit.timeit(lambda: search_function(text, pattern), number=10)

# Читання статей, які були завантажені на компютер
file_path1 = r"C:\Users\sansa\Repository2024\Goit-algo-hw\Article1_BAlgo-5.txt"
file_path2 = r"C:\Users\sansa\Repository2024\Goit-algo-hw\Article2_BAlgo-5.txt"

with open(file_path1, "r", encoding="windows-1251") as file1:
    article1 = file1.read()

with open(file_path2, "r", encoding="windows-1251") as file2:
    article2 = file2.read()

# Попередній перегляд статей
print("Article 1 preview:", article1[:100])
print("Article 2 preview:", article2[:100])

# Випадкові рядки для тестування
existing_substr = "алгоритмів"  # Цей рядок присутній у тексті
nonexistent_substr = "вигаданийрядок"  # Цей рядок не присутній

# Тестування алгоритмів на першій статті
print(f"Алгоритм Бойєра-Мура (існуючий): {measure_search_time(boyer_moore_search, article1, existing_substr)}")
print(f"Алгоритм Бойєра-Мура (неіснуючий): {measure_search_time(boyer_moore_search, article1, nonexistent_substr)}")

print(f"Алгоритм Кнута-Морріса-Пратта (існуючий): {measure_search_time(kmp_search, article1, existing_substr)}")
print(f"Алгоритм Кнута-Морріса-Пратта (неіснуючий): {measure_search_time(kmp_search, article1, nonexistent_substr)}")

print(f"Алгоритм Рабіна-Карпа (існуючий): {measure_search_time(rabin_karp_search, article1, existing_substr)}")
print(f"Алгоритм Рабіна-Карпа (неіснуючий): {measure_search_time(rabin_karp_search, article1, nonexistent_substr)}")

# Тестування алгоритмів на другій статті
print(f"Алгоритм Бойєра-Мура (існуючий): {measure_search_time(boyer_moore_search, article2, existing_substr)}")
print(f"Алгоритм Бойєра-Мура (неіснуючий): {measure_search_time(boyer_moore_search, article2, nonexistent_substr)}")

print(f"Алгоритм Кнута-Морріса-Пратта (існуючий): {measure_search_time(kmp_search, article2, existing_substr)}")
print(f"Алгоритм Кнута-Морріса-Пратта (неіснуючий): {measure_search_time(kmp_search, article2, nonexistent_substr)}")

print(f"Алгоритм Рабіна-Карпа (існуючий): {measure_search_time(rabin_karp_search, article2, existing_substr)}")
print(f"Алгоритм Рабіна-Карпа (неіснуючий): {measure_search_time(rabin_karp_search, article2, nonexistent_substr)}")

#Виведення:
# Article 1 preview: ВИКОРИСТАННЯ АЛГОРИТМІВ У БІБЛІОТЕКАХ МОВ ПРОГРАМУВАННЯ
# Автори публiкації: Коваленко О.О., Корягіна 
# Article 2 preview: Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі
# Автори
# Алгоритм Бойєра-Мура (існуючий): 0.0028459999994083773
# Алгоритм Бойєра-Мура (неіснуючий): 0.0077015999995637685
# Алгоритм Кнута-Морріса-Пратта (існуючий): 0.000811099998827558
# Алгоритм Кнута-Морріса-Пратта (неіснуючий): 0.045794900001055794
# Алгоритм Рабіна-Карпа (існуючий): 0.0007799000013619661
# Алгоритм Рабіна-Карпа (неіснуючий): 0.042946699999447446
# Алгоритм Бойєра-Мура (існуючий): 0.004574599999614293
# Алгоритм Бойєра-Мура (неіснуючий): 0.008490899999742396
# Алгоритм Кнута-Морріса-Пратта (існуючий): 0.011816099999123253
# Алгоритм Кнута-Морріса-Пратта (неіснуючий): 0.06635139999707462
# Алгоритм Рабіна-Карпа (існуючий): 0.011048699998355005
# Алгоритм Рабіна-Карпа (неіснуючий): 0.06308989999888581