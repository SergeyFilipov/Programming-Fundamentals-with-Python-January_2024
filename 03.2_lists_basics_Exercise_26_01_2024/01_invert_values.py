list_number = input().split()
opposite_numbers_total = []
min_number = 0

for number in list_number:
    opposite_number = -int(number)
    opposite_numbers_total.append(opposite_number)

print(opposite_numbers_total)
