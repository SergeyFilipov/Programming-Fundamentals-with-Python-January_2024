import re


def process_string(string):
    total = 0
    regex = r'([a-zA-Z])(\d+)([a-zA-Z])'
    matches = re.findall(regex, string)

    for match in matches:
        letter_before, num, letter_after = match
        num = int(num)

        if letter_before.isupper():
            total += num / (ord(letter_before) - ord('A') + 1)
        else:
            total += num * (ord(letter_before) - ord('a') + 1)

        if letter_after.isupper():
            total -= (ord(letter_after) - ord('A') + 1)
        else:
            total += (ord(letter_after) - ord('a') + 1)

    return total


input_string = input().split()
total_sum = sum(process_string(string) for string in input_string)
print(f'{total_sum:.2f}')
