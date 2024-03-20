number_list = input().split()
abs_list = []

for number in number_list:
    abs_list.append(abs(float(number)))

print(abs_list)
