phrase = "кафедра систем автоматического и интеллектуального управления"
total_characters = len(phrase)

# Создадим словарь для подсчета частот символов
character_counts = {}

# Подсчитаем частоту встречаемости каждого символа
for char in phrase:
    if char in character_counts:
        character_counts[char] += 1
    else:
        character_counts[char] = 1

# Вычислим вероятности
character_probabilities = {}
for char, count in character_counts.items():
    probability = count / total_characters
    character_probabilities[char] = probability

# Выведем вероятности
for char, probability in character_probabilities.items():
    print(f"Символ '{char}': Вероятность {probability:.4f}")