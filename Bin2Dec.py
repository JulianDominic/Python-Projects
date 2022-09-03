"""
User can enter up to 8 binary digits in one input field
User must be notified if anything other than a 0 or 1 was entered
User views the results in a single output field containing the decimal (base 10) equivalent of the binary number that was entered
User can enter a variable number of binary digits
"""
def bin2dec(binary_number):
    for digit in binary_number:
        if ("0" != digit) and ("1" != digit):
            print("Invalid Binary number. Only 1's and 0's are allowed.")
            exit()

    amt_bits = len(binary_number)
    max_index = amt_bits - 1
    sum = 0
    i = 0
    while i < amt_bits:
        sum += int(binary_number[max_index - i]) * (2 ** i)
        i += 1
    print(sum)

numbers = input("Input at least one binary number (up to 8 bits, separate the numbers with a space). \ni.e. 10101010 101 100 10 1 \n>>> ")
num_list = numbers.split(" ")
for number in num_list:
    if len(number) <= 8:
        bin2dec(number)
    else:
        print(f"{number} is more than 8 bits!")