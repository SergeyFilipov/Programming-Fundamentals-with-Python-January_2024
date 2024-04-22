import re

food_information = input()
pattern = r"([#|])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, food_information)

total_calories = sum([int(match[3]) for match in matches])

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = match[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
