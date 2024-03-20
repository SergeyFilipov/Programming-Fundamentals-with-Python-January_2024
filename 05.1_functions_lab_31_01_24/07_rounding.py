number_list = input().split()
rounds_list = []

for number in number_list:
    rounds_list.append(round(float(number)))

print(rounds_list)
