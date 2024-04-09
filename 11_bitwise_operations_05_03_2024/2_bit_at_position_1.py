number = int(input())

bit_at_position_1 = (number >> 1) & 1

bit_number = format(number, '08b')
print(bit_at_position_1)
print(bit_number)
