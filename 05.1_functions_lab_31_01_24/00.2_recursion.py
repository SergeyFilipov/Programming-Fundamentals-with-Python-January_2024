def count_numbers(number):
    if number <= 10:
        print(number)
        count_numbers(number + 1)


count_numbers(1)
