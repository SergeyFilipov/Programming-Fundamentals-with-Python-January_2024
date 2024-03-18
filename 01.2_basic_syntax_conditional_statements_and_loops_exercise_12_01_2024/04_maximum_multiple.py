divider = int(input())
number = int(input())
for num in range(number, divider - 1, - 1):
    if num % divider == 0:
        print(num)
        break
