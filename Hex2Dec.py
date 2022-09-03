standard_hex ={
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def hex2dec(hexadecimal):
    length_hexadecimal = len(hexadecimal)
    sum = 0
    # exponent = length_hexadecimal - 1
    for hex in hexadecimal:
        if hex in standard_hex:
            sum += 16 ** (length_hexadecimal - 1) * standard_hex[hex]
            length_hexadecimal -= 1
        else:
            return "Invalid Hexadecimal"
    return sum


numbers = input("Input at least one hexadecimal number (separate the numbers with a space). \ni.e. 1F 7D FF \n>>> ")
num_list = numbers.split(" ")
for number in num_list:
    print(hex2dec(number))