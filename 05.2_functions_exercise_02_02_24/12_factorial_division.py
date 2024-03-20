def factoriel(number):
    if number == 0:
        return 1
    else:
        return number * factoriel(number - 1)


def factoriel_division_function(number1, number2):
    result1 = factoriel(number1)
    result2 = factoriel(number2)
    division_result = result1 / result2
    return f"{division_result:.2f}"


first_number = int(input())
second_number = int(input())
print(factoriel_division_function(first_number, second_number))
