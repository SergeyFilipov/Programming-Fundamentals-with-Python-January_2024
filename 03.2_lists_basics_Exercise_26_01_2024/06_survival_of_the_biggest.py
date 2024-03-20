string_numbers = input().split()
count_numbers_to_remove = int(input())
my_list = []

for number in string_numbers:
    int_number = int(number)
    my_list.append(int_number)
for current_numbers_remove in range(count_numbers_to_remove):
    my_list.remove(min(my_list))

for index in range(len(my_list)):
    if index < len(my_list) - 1:
        print(my_list[index], end=", ")
    else:
        print(my_list[index], end="")
