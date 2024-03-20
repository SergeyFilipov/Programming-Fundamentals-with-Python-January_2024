# 1
def is_even(number):
    return number % 2 == 0


numbers = input().split()
even_list = []

for number in numbers:
    new_value = int(number)
    even_list.append(new_value)

even_numbers = list(filter(is_even, even_list))
print(even_numbers)


# 2
number_list = input().split()
even_list = []

for number in number_list:
    new_value = int(number)
    if new_value % 2 == 0:
        even_list.append(new_value)

print(even_list)
