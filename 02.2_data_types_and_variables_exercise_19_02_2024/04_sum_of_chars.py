count_of_lines = int(input())
total_sum = 0

for character in range(count_of_lines):
    letters = input()
    total_sum += ord(letters)

print(f"The sum equals: {total_sum}")
