import sys

Base64_Bit_On_Char = {
    "000000": "A", "010000": "Q", "100000": "g", "110000": "w",
    "000001": "B", "010001": "R", "100001": "h", "110001": "x",
    "000010": "C", "010010": "S", "100010": "i", "110010": "y",
    "000011": "D", "010011": "T", "100011": "j", "110011": "z",
    "000100": "E", "010100": "U", "100100": "k", "110100": "0",
    "000101": "F", "010101": "V", "100101": "l", "110101": "1",
    "000110": "G", "010110": "W", "100110": "m", "110110": "2",
    "000111": "H", "010111": "X", "100111": "n", "110111": "3",
    "001000": "I", "011000": "Y", "101000": "o", "111000": "4",
    "001001": "J", "011001": "Z", "101001": "p", "111001": "5",
    "001010": "K", "011010": "a", "101010": "q", "111010": "6",
    "001011": "L", "011011": "b", "101011": "r", "111011": "7",
    "001100": "M", "011100": "c", "101100": "s", "111100": "8",
    "001101": "N", "011101": "d", "101101": "t", "111101": "9",
    "001110": "O", "011110": "e", "101110": "u", "111110": "+",
    "001111": "P", "011111": "f", "101111": "v", "111111": "/"
}

Base64_Char_On_Bit = {
    "A": "000000", "Q": "010000", "g": "100000", "w": "110000",
    "B": "000001", "R": "010001", "h": "100001", "x": "110001",
    "C": "000010", "S": "010010", "i": "100010", "y": "110010",
    "D": "000011", "T": "010011", "j": "100011", "z": "110011",
    "E": "000100", "U": "010100", "k": "100100", "0": "110100",
    "F": "000101", "V": "010101", "l": "100101", "1": "110101",
    "G": "000110", "W": "010110", "m": "100110", "2": "110110",
    "H": "000111", "X": "010111", "n": "100111", "3": "110111",
    "I": "001000", "Y": "011000", "o": "101000", "4": "111000",
    "J": "001001", "Z": "011001", "p": "101001", "5": "111001",
    "K": "001010", "a": "011010", "q": "101010", "6": "111010",
    "L": "001011", "b": "011011", "r": "101011", "7": "111011",
    "M": "001100", "c": "011100", "s": "101100", "8": "111100",
    "N": "001101", "d": "011101", "t": "101101", "9": "111101",
    "O": "001110", "e": "011110", "u": "101110", "+": "111110",
    "P": "001111", "f": "011111", "v": "101111", "/": "111111"
}

base_6 = 6


def encode(output_file_binary, input_file):
    current_content = ""
    output_file = open(output_file_binary, "w")
    with open(input_file, "rb") as f:
        while True:
            buf = f.read(3)
            if not buf or len(buf) < 3:
                break

            for char in buf:
                b__format = '{0:08b}'.format(char)
                current_content = current_content + b__format

            while len(current_content) > base_6:
                letter = current_content[:base_6]
                output_file.write(Base64_Bit_On_Char.get(letter))
                current_content = current_content[base_6:]

            output_file.write(Base64_Bit_On_Char.get(current_content))
            current_content = ""

    if len(buf) == 1:
        content = '{0:08b}'.format(buf[0])
        output_file.write(Base64_Bit_On_Char.get(content[:base_6]))
        output_file.write(Base64_Bit_On_Char.get(content[base_6:].ljust(base_6, '0')))
        output_file.write('=')
        output_file.write('=')

    if len(buf) == 2:
        content = '{0:08b}'.format(buf[0]) + '{0:08b}'.format(buf[1])
        output_file.write(Base64_Bit_On_Char.get(content[:base_6]))
        content = content[base_6:]
        output_file.write(Base64_Bit_On_Char.get(content[:base_6]))
        output_file.write(Base64_Bit_On_Char.get(content[base_6:].ljust(base_6, '0')))
        output_file.write('=')

    output_file.close()


def decode(output_file_txt, input_file_binary):
    output_file = open(output_file_txt, "w")
    with open(input_file_binary, "rb") as f:
        while True:
            buf = f.read(4).decode("utf-8")

            if not buf:
                break
            if len(buf) != 4:
                raise Exception('The file contains invalid encoding')

            tmp_content = ""
            if "=" not in buf:
                for char in buf:
                    tmp_content += Base64_Char_On_Bit.get(char)

            elif buf.find('=') == 3:  # we have 1 '=' character
                tmp_content += Base64_Char_On_Bit.get(buf[0])
                tmp_content += Base64_Char_On_Bit.get(buf[1])
                tmp_content += Base64_Char_On_Bit.get(buf[2])[:4]

            else:
                tmp_content += Base64_Char_On_Bit.get(buf[0])
                tmp_content += Base64_Char_On_Bit.get(buf[1])[:2]

            n = int('0b' + tmp_content, 2)
            output_file.write(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

    output_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage : python base64.py --encode file.bin file-enc.txt")
        print("        python base64.py --decode file-enc.txt file.bin")
        exit(1)

    if sys.argv[1] == '--encode':
        encode(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == '--decode':
        decode(sys.argv[2], sys.argv[3])
    else:
        print("Wrong usage")
        exit(1)
