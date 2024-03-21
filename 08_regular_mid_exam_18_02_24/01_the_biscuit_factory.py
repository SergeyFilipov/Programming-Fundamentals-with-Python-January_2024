import math

biscuits_produced_per_day_by_1_worker = int(input())
count_of_workers_in_the_factory = int(input())
number_of_biscuits_competitive_factory_per_30_day = int(input())
day = 30
production_per_30_days_anna = []

for day in range(1, day + 1):
    if day % 3 == 0:
        production_per_day = biscuits_produced_per_day_by_1_worker * 0.75 * count_of_workers_in_the_factory
        production_per_30_days_anna.append(math.floor(production_per_day))
    else:
        production_per_day = biscuits_produced_per_day_by_1_worker * count_of_workers_in_the_factory
        production_per_30_days_anna.append(production_per_day)

difference_in_biscuits_produced = sum(production_per_30_days_anna) - number_of_biscuits_competitive_factory_per_30_day
percent = (difference_in_biscuits_produced / number_of_biscuits_competitive_factory_per_30_day) * 100

print(f"You have produced {sum(production_per_30_days_anna)} biscuits for the past month.")

if number_of_biscuits_competitive_factory_per_30_day < sum(production_per_30_days_anna):

    print(f"You produce {abs(percent):.2f} percent more biscuits.")
else:
    print(f"You produce {abs(percent):.2f} percent less biscuits.")
