count_string = int(input())
special_word = input()
my_list = []
my_list_special_string = []

for string in range(count_string):
    current_string = input()
    my_list.append(current_string)
    if special_word in current_string:
        my_list_special_string.append(current_string)

print(my_list)
print(my_list_special_string)
