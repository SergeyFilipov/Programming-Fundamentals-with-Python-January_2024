number = int(input())
for current_number in range(1, number + 1):
    current_number_str = str(current_number)
    digit_sum = 0
    for digit in current_number_str:
        digit_sum += int(digit)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
