count_of_lines = int(input())
tank_capacity = 255

for litter_in_tank in range(count_of_lines):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print(f"Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water

print(255 - tank_capacity)
