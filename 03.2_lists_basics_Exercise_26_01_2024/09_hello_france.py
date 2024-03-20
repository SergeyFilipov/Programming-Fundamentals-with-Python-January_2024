collect_of_items = input().split('|')
budget = float(input())

my_items_original_price = []

for current_item in collect_of_items:
    current_items_parts = current_item.split('->')
    current_type = current_items_parts[0]
    current_price = float(current_items_parts[1])

    if current_type == 'Clothes' and current_price <= 50.00:
        if budget >= current_price:
            my_items_original_price.append(current_price)
            budget -= current_price
    elif current_type == 'Shoes' and current_price <= 35.00:
        if budget >= current_price:
            my_items_original_price.append(current_price)
            budget -= current_price
    elif current_type == 'Accessories' and current_price <= 20.50:
        if budget >= current_price:
            my_items_original_price.append(current_price)
            budget -= current_price

my_list_with_new_price = []
for item in my_items_original_price:
    my_list_with_new_price.append(item * 1.40)

profit = sum(my_list_with_new_price) - sum(my_items_original_price)

for new_item in my_list_with_new_price:
    print(f'{new_item:.2f}', end=' ')

print()
print(f'Profit: {profit:.2f}')

if (sum(my_list_with_new_price) + budget) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
