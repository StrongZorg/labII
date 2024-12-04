def sequential_coding(phrase):
    # Словарь с фиксированными кодами для символов
    encoding_dict = {
        'к': '00000',
        'а': '00001',
        'ф': '00010',
        'е': '00011',
        'д': '00100',
        'р': '00101',
        ' ': '00110',
        'с': '00111',
        'и': '01000',
        'м': '01001',
        'в': '01010',
        'т': '01011',
        'о': '01100',
        'ч': '01101',
        'н': '01110',
        'у': '01111',
        'г': '10000',
        'л': '10001',
        'ь': '10010',
        'п': '10100',
        'я': '10101',
    }

    encoded_phrase = ""
    for char in phrase:
        if char in encoding_dict:
            encoded_phrase += encoding_dict[char]
        else:
            encoded_phrase += char

    return encoded_phrase

# Исходная фраза
phrase = "кафедра систем автоматического и интеллектуального управления"

# Кодируем фразу
encoded_phrase = sequential_coding(phrase)

# Выводим закодированную фразу
print("Закодированная фраза:")
print(encoded_phrase)