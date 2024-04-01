food_and_quantities = input().split()

finaal_products = dict()

for index in range(0, len(food_and_quantities), 2):
    product = food_and_quantities[index]
    qantity = int(food_and_quantities[index + 1])
    finaal_products[product] = qantity

print(finaal_products)
