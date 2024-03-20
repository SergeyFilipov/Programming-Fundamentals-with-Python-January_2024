count_number = int(input())
numbers = []

for number in range(count_number):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_number = []

if command == "even":
    for even_number in numbers:
        if even_number % 2 == 0:
            filtered_number.append(even_number)

elif command == "odd":
    for odd_number in numbers:
        if odd_number % 2 != 0:
            filtered_number.append(odd_number)

elif command == "negative":
    for negative_number in numbers:
        if negative_number < 0:
            filtered_number.append(negative_number)

elif command == "positive":
    for positive_number in numbers:
        if positive_number >= 0:
            filtered_number.append(positive_number)

print(filtered_number)
