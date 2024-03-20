money = input().split(", ")
count_of_beggars = int(input())
money_int = []
for coins in money:
    money_int.append(int(coins))
final_sums = []
start_index = 0
for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_int), count_of_beggars):
        current_beggar_sum += money_int[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)
