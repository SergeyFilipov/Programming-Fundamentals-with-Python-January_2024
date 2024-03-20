def odd_even_sum(number):
    odd_digits = 0
    even_digits = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even_digits += int(digit)
        else:
            odd_digits += int(digit)

    return f"Odd sum = {odd_digits}, Even sum = {even_digits}"


number = int(input())

print(odd_even_sum(number))
