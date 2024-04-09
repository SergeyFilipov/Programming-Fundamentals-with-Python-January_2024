number = int(input())
binary_digit = int(input())
count_dijit = 0
binary_number = []

while number > 0:
    remainder = number % 2
    binary_number.append(remainder)
    if remainder == binary_digit:
        count_dijit += 1
    number = number // 2

print(count_dijit)  # 3
print(''.join(map(str, reversed(binary_number))))
