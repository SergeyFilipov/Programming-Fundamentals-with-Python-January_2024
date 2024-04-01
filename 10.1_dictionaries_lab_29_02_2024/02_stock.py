food_and_quantities = input().split()
surches_products = input().split()
finaal_products = dict()

for index in range(0, len(food_and_quantities), 2):
    product = food_and_quantities[index]
    qantity = int(food_and_quantities[index + 1])
    finaal_products[product] = qantity

for product in surches_products:
    if product in finaal_products.keys():
        print(f"We have {finaal_products[product]} of {product} left")

    else:
        print(f"Sorry, we don't have {product}")
