import math

count_people = int(input())
count_days = int(input())
coins = 0

for current_day in range(1, count_days + 1):
    if current_day % 10 == 0:
        count_people -= 2
    if current_day % 15 == 0:
        count_people += 5
    if current_day % 3 == 0:
        coins -= 3 * count_people
    if current_day % 5 == 0:
        coins += 20 * count_people
        if current_day % 3 == 0:
            coins -= 2 * count_people
    coins += 50
    coins -= 2 * count_people
print(f"{count_people} companions received {math.floor(coins / count_people)} coins each.")
