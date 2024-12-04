import re

class Pyramid:
    def __init__(self, pyramid_str):
        self.pyramid_str = pyramid_str

    def compress(self):
        compressed_str = self._compress_level(self.pyramid_str)
        return compressed_str

    def _compress_level(self, pyramid_str):
        if len(pyramid_str) <= 4:
            return pyramid_str

        # Определяем размер стороны меньшей пирамиды
        side_size = int(len(pyramid_str) ** 0.5)
        half_size = side_size // 2

        # Рекурсивное сжатие каждой из четырех меньших пирамид
        top_left = self._compress_level(pyramid_str[:half_size])
        top_right = self._compress_level(pyramid_str[half_size:2 * half_size])
        bottom_left = self._compress_level(pyramid_str[2 * half_size:3 * half_size])
        bottom_right = self._compress_level(pyramid_str[3 * half_size:])

        # !Правка! Добавил re.sub для библиотеки
        compressed_str = re.sub(r'(.)\1*', r'\1', top_left + top_right + bottom_left + bottom_right)

        return compressed_str

    def __str__(self):
        return self.pyramid_str


def read_pyramid_from_file(file_name):
    with open(file_name, 'r') as file:
        pyramid_str = file.read().strip()
    return pyramid_str


def write_pyramid_to_file(file_name, compressed_str):
    with open(file_name, 'w') as file:
        file.write(compressed_str)


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    pyramid_str = read_pyramid_from_file(input_file)
    pyramid = Pyramid(pyramid_str)

    compressed_pyramid_str = pyramid.compress()
    write_pyramid_to_file(output_file, compressed_pyramid_str)


if __name__ == "__main__":
    main()
