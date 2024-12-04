def shannon_fano_coding(text):
    # Функция для рекурсивного кодирования текста
    if len(text) <= 1:
        return {text: '0'}

    # Сортируем символы по частоте встречаемости
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Разбиваем символы на две группы
    mid = len(sorted_freq) // 2
    group1 = tuple(pair[0] for pair in sorted_freq[:mid])
    group2 = tuple(pair[0] for pair in sorted_freq[mid:])

    # Рекурсивно кодируем каждую группу
    code_dict = {}
    for char, code in shannon_fano_coding(group1).items():
        code_dict[char] = '0' + code
    for char, code in shannon_fano_coding(group2).items():
        code_dict[char] = '1' + code

    return code_dict

# Исходная фраза
phrase = "кафедра систем автоматического и интеллектуального управления"

# Преобразуем фразу в кортеж символов
phrase_chars = tuple(phrase)

# Кодируем фразу
code_dict = shannon_fano_coding(phrase_chars)

# Выводим результат
for char, code in code_dict.items():
    print(f'{char}: {code}')