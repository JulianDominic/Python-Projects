"""
Decimal to Binary and Hexadecimal converter
Works only for positive numbers
"""
bin_num = ""
def dec2bin(num):
    if num > 1:
        dec2bin(num // 2)
    global bin_num
    bin_num += str(num % 2)
    return bin_num

hex_num = ""
standard_hex ={
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"}
def dec2hex(num):
    if num >= 1:
        dec2hex(num // 16)
    global hex_num
    if num != 0:
        hex_num += standard_hex[num % 16]
    return hex_num
    
numbers = input("Input at least one number (separate the numbers with a space). \ni.e. 69 420 1337 \n>>> ")
num_list = numbers.split(" ")
for number in num_list:
    print(f"{number} has been converted to, \nBinary: {dec2bin(int(number))} \nHexadecimal: {dec2hex(int(number))}")