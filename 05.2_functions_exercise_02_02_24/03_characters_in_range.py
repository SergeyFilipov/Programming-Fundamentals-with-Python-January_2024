def char_range(fist_symbol, second_symbol2):
    result = " "

    for index in range(ord(fist_symbol) + 1, ord(second_symbol2)):
        result += chr(index) + " "
    return result


fist_symbol = input()
second_symbol2 = input()
print(char_range(fist_symbol, second_symbol2))
