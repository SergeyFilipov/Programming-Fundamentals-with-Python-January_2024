the_number_of_orders = int(input())
price_coffee = 0
total_price = 0

for order in range(the_number_of_orders):
    price_per_capsule = float(input())
    if not 0.01 <= price_per_capsule <= 100.00:
        continue
    days = int(input())
    if not 1 <= days <= 31:
        continue
    number_of_capsules = int(input())
    if not 1 <= number_of_capsules <= 2000:
        continue
    price_coffee = price_per_capsule * days * number_of_capsules
    total_price += price_coffee
    print(f"The price for the coffee is: ${price_coffee:.2f}")

print(f"Total: ${total_price:.2f}")
