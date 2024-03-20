def is_perfect_number(number):
    division_sum = 0

    for divisior in range(1, number):
        if number % divisior == 0:
            division_sum += divisior

    if division_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))
