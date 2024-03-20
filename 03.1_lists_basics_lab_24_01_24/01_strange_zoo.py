my_list = []

for data in range(3):
    body_parts = input()
    my_list.append(body_parts)
my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)
