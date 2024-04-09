number = int(input())
position = int(input())

bit_value = (number >> position) & 1

print(bit_value)
