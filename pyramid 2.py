class Pyramid:
    def __init__(self, base_str):
        self.base_str = base_str
        self.pyramid_str = self.generate_pyramid()

    def generate_pyramid(self):
        length = len(self.base_str)
        if length == 1:
            return self.base_str

        side_length = int(length ** 0.25)
        quarter_length = length // 4

        top_left = Pyramid(self.base_str[:quarter_length]).pyramid_str
        top_right = Pyramid(self.base_str[quarter_length:2 * quarter_length]).pyramid_str
        bottom_left = Pyramid(self.base_str[2 * quarter_length:3 * quarter_length]).pyramid_str
        bottom_right = Pyramid(self.base_str[3 * quarter_length:]).pyramid_str

        return f"{top_left}{top_right}{bottom_left}{bottom_right}"

    def compress_pyramid(self, s):
        if len(s) <= 4:
            return s

        compressed_str = ''
        for i in range(0, len(s), 4):
            block = s[i:i + 4]
            if len(set(block)) == 1:
                compressed_str += block[0]
            else:
                compressed_str += block

        return compressed_str

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

    compressed_pyramid_str = pyramid.compress_pyramid(pyramid.pyramid_str)
    write_pyramid_to_file(output_file, compressed_pyramid_str)

if __name__ == "__main__":
    main()
