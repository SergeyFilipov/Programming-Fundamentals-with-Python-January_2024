# 1
numbers = input().split()
new_list = []

for number in numbers:
    current_number = int(number)
    new_list.append(current_number)
sorted_numbers = sorted(new_list)

print(sorted_numbers)



# 2
numbers = input().split()
new_list = []

for number in numbers:
    current_number = int(number)
    new_list.append(current_number)

print(list(sorted(new_list)))
