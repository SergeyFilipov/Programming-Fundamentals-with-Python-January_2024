budget = float(input())
price_for_1kg_flour = float(input())
price_one_pack_eggs = price_for_1kg_flour * 0.75
price_1l_milk = price_for_1kg_flour * 1.25
price_250ml_milk = price_1l_milk / 4

price_for_one_loaf = price_one_pack_eggs + price_for_1kg_flour + price_250ml_milk
count_of_loaves = int(budget / price_for_one_loaf)
money_left = budget % price_for_one_loaf
colored_eggs = 0
current_bread_count = count_of_loaves
for loaf in range(1, count_of_loaves + 1):
    colored_eggs += 3
    if loaf % 3 == 0:
        colored_eggs -= loaf - 2

print(f"You made {count_of_loaves} loaves of Easter bread! "
      f"Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
