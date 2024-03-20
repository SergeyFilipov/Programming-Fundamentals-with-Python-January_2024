numbers = input().split(", ")
positive_number = []
negative_number = []
even_number = []
odd_number = []

for current_number in numbers:
    if int(current_number) % 2 == 0:
        even_number.append(current_number)
    if int(current_number) % 2 != 0:
        odd_number.append(current_number)
    if int(current_number) < 0:
        negative_number.append(current_number)
    if int(current_number) >= 0:
        positive_number.append(current_number)

positive_numbers = ", ".join(positive_number)
negative_numbers = ", ".join(negative_number)
even_numbers = ", ".join(even_number)
odd_numbers = ", ".join(odd_number)

print(f"Positive: {positive_numbers}")
print(f"Negative: {negative_numbers}")
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")
