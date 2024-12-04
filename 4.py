def calculate_average_information(probabilities, code_lengths):
    average_information = 0.0

    for char, probability in probabilities.items():
        if char in code_lengths:
            code_length = code_lengths[char]
            average_information += probability * code_length

    return average_information

#Таблица вероятностей символов
probabilities = {
    'а': 0.2162,
    'ф': 0.0054,
    'е': 0.1081,
    'д': 0.0811,
    'р': 0.0541,
    ' ': 0.1351,
    'с': 0.0541,
    'и': 0.0811,
    'м': 0.0541,
    'в': 0.0270,
    'т': 0.0541,
    'о': 0.0811,
    'ч': 0.0054,
    'н': 0.0541,
    'у': 0.0270,
    'г': 0.0270,
    'к': 0.0492,
    'л': 0.0270,
    'ь': 0.0270,
    'п': 0.0270,
    'я': 0.0270,
}

#Таблица длин кодов символов
code_lengths = {
    'а': 5,
    'е': 5,
    ' ': 5,
    'и': 5,
    'т': 5,
    'о': 5,
    'л': 5,
    'л': 5,
    'к': 5,
    'с': 5,
    'н': 5,
    'р': 5,
    'м': 5,
    'в': 5,
    'г': 5,
    'у': 5,
    'ф': 5,
    'д': 5,
    'ч': 5,
    'ь': 5,
    'п': 5,
    'я': 5,
}

# Вычисляем среднюю информацию
average_info = calculate_average_information(probabilities, code_lengths)

print(f"Средняя информация на символ: {average_info} бит")