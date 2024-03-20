numbers = input().split()
new_list = []

for number in numbers:
    current_number = int(number)
    new_list.append(current_number)

print(f"The minimum number is {min(new_list)}")
print(f"The maximum number is {max(new_list)}")
print(f"The sum number is: {sum(new_list)}")
